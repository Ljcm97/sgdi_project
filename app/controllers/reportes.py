from flask import Blueprint, render_template, jsonify, request, session, send_file
from flask_login import login_required, current_user
from sqlalchemy import func, and_, or_, desc, extract, case, text
from datetime import datetime, timedelta, date
from calendar import monthrange
import io
import json
import pandas as pd
from app import db
from app.models.documento import Documento
from app.models.movimiento import Movimiento
from app.models.area import Area
from app.models.estado_documento import EstadoDocumento
from app.models.tipo_documento import TipoDocumento
from app.models.transportadora import Transportadora
from app.utils.auth import permission_required
from app.utils.helpers import format_date
from app.utils.estadisticas import calcular_tiempo_procesamiento, calcular_tendencias
from app.utils.exportacion import exportar_excel, exportar_pdf, exportar_xml

reportes_bp = Blueprint('reportes', __name__, url_prefix='/reportes')

@reportes_bp.route('/')
@login_required
@permission_required('Ver reportes')
def index():
    """Vista principal de reportes - Dashboard analítico"""
    # Estadísticas generales para el dashboard
    total_documentos = Documento.query.count()
    
    # Obtener estados para contar documentos
    estados = EstadoDocumento.query.all()
    stats_estados = {}
    
    for estado in estados:
        count = Documento.query.filter_by(estado_actual_id=estado.id).count()
        if count > 0:  # Solo incluir estados con documentos
            stats_estados[estado.nombre] = {
                'count': count,
                'color': estado.color,
                'percentage': round((count / total_documentos * 100) if total_documentos > 0 else 0, 1)
            }
    
    # Documentos procesados en el último mes
    fecha_inicio = datetime.now() - timedelta(days=30)
    docs_recientes = Documento.query.filter(Documento.creado_en >= fecha_inicio).count()
    
    # Tiempo promedio de procesamiento (últimos 30 días)
    tiempo_promedio = calcular_tiempo_procesamiento(dias=30)
    
    return render_template('reportes/index.html', 
                          total_documentos=total_documentos,
                          stats_estados=stats_estados,
                          docs_recientes=docs_recientes,
                          tiempo_promedio=tiempo_promedio)

@reportes_bp.route('/por-area')
@login_required
@permission_required('Ver reportes')
def por_area():
    """Reporte de documentos por área con filtros dinámicos"""
    # Obtener filtros opcionales
    filtros = obtener_filtros_request()
    guardar_filtros_session(filtros)
    
    # Filtrar según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    query = aplicar_filtros_a_query(query_base, filtros)
    
    # Obtener estadísticas por área
    areas = Area.query.all()
    resultados = []
    
    for area in areas:
        # Contar documentos por estado para esta área
        stats = db.session.query(
            EstadoDocumento.nombre.label('estado'),
            EstadoDocumento.color.label('color'),
            func.count(Documento.id).label('cantidad')
        ).join(
            Documento, Documento.estado_actual_id == EstadoDocumento.id
        ).filter(
            Documento.area_destino_id == area.id,
            Documento.id.in_(query.with_entities(Documento.id))
        ).group_by(
            EstadoDocumento.nombre, EstadoDocumento.color
        ).all()
        
        # Formatear resultados
        estados = [{'estado': s.estado, 'color': s.color, 'cantidad': s.cantidad} for s in stats]
        
        # Calcular total
        total = sum(e['cantidad'] for e in estados)
        
        # Solo incluir áreas con documentos
        if total > 0:
            resultados.append({
                'area': area.nombre,
                'estados': estados,
                'total': total
            })
    
    # Ordenar por total de documentos (descendente)
    resultados = sorted(resultados, key=lambda x: x['total'], reverse=True)
    
    return render_template('reportes/por_area.html', 
                          resultados=resultados,
                          filtros=filtros)

@reportes_bp.route('/por-estado')
@login_required
@permission_required('Ver reportes')
def por_estado():
    """Reporte de documentos por estado"""
    # Obtener filtros opcionales
    filtros = obtener_filtros_request()
    guardar_filtros_session(filtros)
    
    # Filtrar según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    query = aplicar_filtros_a_query(query_base, filtros)
    
    # Obtener todos los estados
    estados = EstadoDocumento.query.all()
    
    resultados = []
    for estado in estados:
        # Contar documentos en este estado
        estado_query = query.filter(Documento.estado_actual_id == estado.id)
        cantidad = estado_query.count()
        
        # Obtener documentos recientes en este estado
        docs = estado_query.order_by(Documento.fecha_recepcion.desc()).limit(5).all()
        
        # Preparar documentos para serialización
        documentos_serializables = []
        for doc in docs:
            documentos_serializables.append({
                'id': doc.id,
                'radicado': doc.radicado,
                'fecha_recepcion': doc.fecha_recepcion.strftime('%Y-%m-%d %H:%M'),
                'tipo_documento_nombre': doc.tipo_documento.nombre,
                'area_destino_nombre': doc.area_destino.nombre
            })
        
        if cantidad > 0:
            resultados.append({
                'estado': estado.nombre,
                'color': estado.color,
                'cantidad': cantidad,
                'documentos_serializables': documentos_serializables
            })
    
    # Ordenar resultados por cantidad de documentos (descendente)
    resultados = sorted(resultados, key=lambda x: x['cantidad'], reverse=True)
    
    return render_template('reportes/por_estado.html', 
                          resultados=resultados,
                          filtros=filtros)

@reportes_bp.route('/tiempo-procesamiento')
@login_required
@permission_required('Ver reportes')
def tiempo_procesamiento():
    """Reporte de tiempo de procesamiento de documentos"""
    # Obtener parámetros de filtro
    filtros = obtener_filtros_request()
    dias = filtros.get('dias', 30)
    try:
        dias = int(dias)
    except ValueError:
        dias = 30
    
    # Calcular fecha límite
    fecha_limite = datetime.now() - timedelta(days=dias)
    
    # Crear consulta base según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    query = aplicar_filtros_a_query(query_base, filtros)
    
    # Obtener documentos finalizados en el período
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    estados_finales = []
    if estado_finalizado:
        estados_finales.append(estado_finalizado.id)
    if estado_archivado:
        estados_finales.append(estado_archivado.id)
    
    # Si no hay estados finales definidos, mostrar mensaje
    if not estados_finales:
        return render_template('reportes/tiempo_procesamiento.html', 
                              resultados=[],
                              filtros=filtros,
                              mensaje="No se encontraron estados de finalización o archivado en el sistema.")
    
    documentos = query.filter(
        Documento.estado_actual_id.in_(estados_finales),
        Documento.creado_en >= fecha_limite
    ).all()
    
    # Calcular tiempos de procesamiento
    resultados_serializables = []
    
    for doc in documentos:
        # Obtener primer y último movimiento
        primer_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora).first()
        ultimo_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora.desc()).first()
        
        if primer_mov and ultimo_mov:
            # Calcular duración en horas
            duracion = ultimo_mov.fecha_hora - primer_mov.fecha_hora
            horas = duracion.total_seconds() / 3600
            
            resultados_serializables.append({
                'documento_id': doc.id,
                'documento_radicado': doc.radicado,
                'documento_tipo_nombre': doc.tipo_documento.nombre,
                'documento_remitente': doc.remitente,
                'documento_area': doc.area_destino.nombre,
                'inicio': primer_mov.fecha_hora.strftime('%Y-%m-%d %H:%M'),
                'fin': ultimo_mov.fecha_hora.strftime('%Y-%m-%d %H:%M'),
                'duracion_horas': round(horas, 2),
                'duracion_dias': round(horas / 24, 2)
            })
    
    # Ordenar por duración (mayor a menor)
    resultados_serializables.sort(key=lambda x: x['duracion_horas'], reverse=True)
    
    # Calcular estadísticas
    if resultados_serializables:
        tiempo_promedio = sum(r['duracion_horas'] for r in resultados_serializables) / len(resultados_serializables)
        tiempo_minimo = min(r['duracion_horas'] for r in resultados_serializables)
        tiempo_maximo = max(r['duracion_horas'] for r in resultados_serializables)
    else:
        tiempo_promedio = tiempo_minimo = tiempo_maximo = 0
    
    estadisticas = {
        'promedio': round(tiempo_promedio, 2),
        'minimo': round(tiempo_minimo, 2),
        'maximo': round(tiempo_maximo, 2),
        'total_docs': len(resultados_serializables)
    }
    
    return render_template('reportes/tiempo_procesamiento.html', 
                          resultados=resultados_serializables,
                          estadisticas=estadisticas,
                          filtros=filtros,
                          dias=dias)

@reportes_bp.route('/tendencias')
@login_required
@permission_required('Ver reportes')
def tendencias():
    """Reporte de tendencias a lo largo del tiempo"""
    # Obtener filtros
    filtros = obtener_filtros_request()
    
    # Determinar el período solicitado
    periodo = filtros.get('periodo', 'mensual')
    
    # Obtener datos según el período
    if periodo == 'mensual':
        # Datos mensuales para los últimos 12 meses
        datos_tendencia = calcular_tendencias(periodo='mensual', meses=12, filtros=filtros)
    elif periodo == 'semanal':
        # Datos semanales para las últimas 12 semanas
        datos_tendencia = calcular_tendencias(periodo='semanal', semanas=12, filtros=filtros)
    else:  # diario
        # Datos diarios para los últimos 30 días
        datos_tendencia = calcular_tendencias(periodo='diario', dias=30, filtros=filtros)
    
    return render_template('reportes/tendencias.html',
                          datos=datos_tendencia,
                          filtros=filtros,
                          periodo=periodo)

@reportes_bp.route('/personalizado')
@login_required
@permission_required('Ver reportes')
def personalizado():
    """Reporte personalizado con múltiples dimensiones"""
    # Obtener filtros y parámetros de agrupación
    filtros = obtener_filtros_request()
    guardar_filtros_session(filtros)
    
    dimension1 = request.args.get('dimension1', 'area')
    dimension2 = request.args.get('dimension2', 'estado')
    
    # Filtrar según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    query = aplicar_filtros_a_query(query_base, filtros)
    
    # Construir consulta dinámica según las dimensiones seleccionadas
    resultados = generar_reporte_personalizado(query, dimension1, dimension2)
    
    # Obtener opciones para filtros
    areas = Area.query.order_by(Area.nombre).all()
    tipos_documento = TipoDocumento.query.order_by(TipoDocumento.nombre).all()
    estados = EstadoDocumento.query.order_by(EstadoDocumento.nombre).all()
    
    # Obtener valores únicos para dimensión 2
    valores_dim2 = []
    if resultados:
        for dim1 in resultados.values():
            for dim2 in dim1.keys():
                if dim2 not in valores_dim2:
                    valores_dim2.append(dim2)
        valores_dim2 = sorted(valores_dim2)
    
    return render_template('reportes/personalizado.html',
                          resultados=resultados,
                          filtros=filtros,
                          dimension1=dimension1,
                          dimension2=dimension2,
                          areas=areas,
                          tipos_documento=tipos_documento,
                          estados=estados,
                          valores_dim2=valores_dim2)

@reportes_bp.route('/datos-grafico')
@login_required
@permission_required('Ver reportes')
def datos_grafico():
    """API para obtener datos para gráficos en formato JSON"""
    tipo = request.args.get('tipo', 'area')
    filtros = obtener_filtros_request()
    
    # Filtrar según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    query = aplicar_filtros_a_query(query_base, filtros)
    
    if tipo == 'area':
        # Datos para gráfico por área
        datos = datos_grafico_por_area(query)
    elif tipo == 'estado':
        # Datos para gráfico por estado
        datos = datos_grafico_por_estado(query)
    elif tipo == 'tiempo':
        # Datos para gráfico de tiempo
        datos = datos_grafico_tiempo(query, filtros)
    elif tipo == 'tipo_documento':
        # Datos para gráfico por tipo de documento
        datos = datos_grafico_por_tipo_documento(query)
    else:
        datos = []
    
    return jsonify(datos)

@reportes_bp.route('/exportar/<formato>')
@login_required
@permission_required('Ver reportes')
def exportar(formato):
    """Exportar datos de reportes en diferentes formatos"""
    tipo_reporte = request.args.get('tipo', 'area')
    filtros = obtener_filtros_session()
    
    # Filtrar según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    query = aplicar_filtros_a_query(query_base, filtros)
    
    # Obtener datos según el tipo de reporte
    if tipo_reporte == 'area':
        datos = preparar_datos_exportacion_area(query)
        nombre_archivo = f"reporte_por_area_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    elif tipo_reporte == 'estado':
        datos = preparar_datos_exportacion_estado(query)
        nombre_archivo = f"reporte_por_estado_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    elif tipo_reporte == 'tiempo':
        datos = preparar_datos_exportacion_tiempo(query, filtros)
        nombre_archivo = f"reporte_tiempos_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    elif tipo_reporte == 'tendencias':
        periodo = filtros.get('periodo', 'mensual')
        datos = preparar_datos_exportacion_tendencias(periodo, filtros)
        nombre_archivo = f"reporte_tendencias_{periodo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    else:
        # Reporte personalizado
        dimension1 = filtros.get('dimension1', 'area')
        dimension2 = filtros.get('dimension2', 'estado')
        datos = preparar_datos_exportacion_personalizado(query, dimension1, dimension2)
        nombre_archivo = f"reporte_personalizado_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Exportar según el formato solicitado
    if formato == 'excel':
        return exportar_excel(datos, nombre_archivo)
    elif formato == 'pdf':
        return exportar_pdf(datos, nombre_archivo, tipo_reporte)
    elif formato == 'xml':
        return exportar_xml(datos, nombre_archivo)
    else:
        return jsonify({'error': 'Formato no soportado'})

# Funciones auxiliares para los reportes

def obtener_filtros_request():
    """Obtiene los filtros desde la solicitud HTTP"""
    filtros = {}
    
    # Filtros de fecha
    fecha_desde = request.args.get('fecha_desde')
    if fecha_desde:
        try:
            filtros['fecha_desde'] = datetime.strptime(fecha_desde, '%Y-%m-%d')
        except ValueError:
            pass
    
    fecha_hasta = request.args.get('fecha_hasta')
    if fecha_hasta:
        try:
            filtros['fecha_hasta'] = datetime.strptime(fecha_hasta, '%Y-%m-%d')
        except ValueError:
            pass
    
    # Filtros de dimensiones
    for campo in ['area_id', 'estado_id', 'tipo_documento_id', 'transportadora_id']:
        valor = request.args.get(campo)
        if valor and valor != '0':
            try:
                filtros[campo] = int(valor)
            except ValueError:
                pass
    
    # Otros filtros
    for campo in ['tipo', 'dias', 'periodo', 'dimension1', 'dimension2']:
        valor = request.args.get(campo)
        if valor:
            filtros[campo] = valor
    
    return filtros

def guardar_filtros_session(filtros):
    """Guarda los filtros en la sesión para su uso en la exportación"""
    session['filtros_reporte'] = {k: v for k, v in filtros.items() if not isinstance(v, datetime)}
    # Para las fechas, guardamos el string
    if 'fecha_desde' in filtros and isinstance(filtros['fecha_desde'], datetime):
        session['filtros_reporte']['fecha_desde'] = filtros['fecha_desde'].strftime('%Y-%m-%d')
    if 'fecha_hasta' in filtros and isinstance(filtros['fecha_hasta'], datetime):
        session['filtros_reporte']['fecha_hasta'] = filtros['fecha_hasta'].strftime('%Y-%m-%d')

def obtener_filtros_session():
    """Recupera los filtros guardados en la sesión"""
    filtros = session.get('filtros_reporte', {})
    
    # Convertir fechas de string a datetime
    if 'fecha_desde' in filtros:
        try:
            filtros['fecha_desde'] = datetime.strptime(filtros['fecha_desde'], '%Y-%m-%d')
        except (ValueError, TypeError):
            pass
    
    if 'fecha_hasta' in filtros:
        try:
            filtros['fecha_hasta'] = datetime.strptime(filtros['fecha_hasta'], '%Y-%m-%d')
        except (ValueError, TypeError):
            pass
    
    return filtros

def crear_query_base_segun_rol():
    """Crea la consulta base según el rol del usuario"""
    query = Documento.query
    
    # Filtrar según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador':
        # Superadministrador ve todos los documentos
        pass
    elif current_user.rol.nombre == 'Recepción':
        # Recepción ve los documentos que ha registrado
        query = query.filter_by(registrado_por_id=current_user.id)
    else:
        # Usuario regular ve los documentos de su área o asignados a él
        query = query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        )
    
    return query

def aplicar_filtros_a_query(query, filtros):
    """Aplica los filtros especificados a la consulta"""
    # Filtros de fecha
    if 'fecha_desde' in filtros:
        query = query.filter(Documento.fecha_recepcion >= filtros['fecha_desde'])
    
    if 'fecha_hasta' in filtros:
        # Incluir todo el día para fecha_hasta
        fecha_hasta = filtros['fecha_hasta']
        if isinstance(fecha_hasta, datetime):
            fecha_hasta = datetime.combine(fecha_hasta.date(), datetime.max.time())
        query = query.filter(Documento.fecha_recepcion <= fecha_hasta)
    
    # Filtros por ID
    for campo, modelo_campo in [
        ('area_id', Documento.area_destino_id),
        ('estado_id', Documento.estado_actual_id),
        ('tipo_documento_id', Documento.tipo_documento_id),
        ('transportadora_id', Documento.transportadora_id)
    ]:
        if campo in filtros:
            query = query.filter(modelo_campo == filtros[campo])
    
    # Filtro por tipo (ENTRADA/SALIDA)
    if 'tipo' in filtros and filtros['tipo'] in ['ENTRADA', 'SALIDA']:
        query = query.filter(Documento.tipo == filtros['tipo'])
    
    return query

def datos_grafico_por_area(query):
    """Obtiene datos para gráfico por área"""
    areas = Area.query.all()
    
    datos = []
    for area in areas:
        # Contar total de documentos
        total = query.filter(Documento.area_destino_id == area.id).count()
        
        if total > 0:
            # Contar por estados
            estados = db.session.query(
                EstadoDocumento.nombre,
                EstadoDocumento.color,
                func.count(Documento.id).label('cantidad')
            ).join(
                Documento, Documento.estado_actual_id == EstadoDocumento.id
            ).filter(
                Documento.area_destino_id == area.id,
                Documento.id.in_(query.with_entities(Documento.id))
            ).group_by(
                EstadoDocumento.nombre, EstadoDocumento.color
            ).all()
            
            # Añadir a resultados
            datos.append({
                'area': area.nombre,
                'total': total,
                'estados': [{'nombre': e.nombre, 'color': e.color, 'cantidad': e.cantidad} for e in estados]
            })
    
    return datos

def datos_grafico_por_estado(query):
    """Obtiene datos para gráfico por estado"""
    # Contar documentos por estado
    estados = db.session.query(
        EstadoDocumento.nombre,
        EstadoDocumento.color,
        func.count(Documento.id).label('cantidad')
    ).join(
        Documento, Documento.estado_actual_id == EstadoDocumento.id
    ).filter(
        Documento.id.in_(query.with_entities(Documento.id))
    ).group_by(
        EstadoDocumento.nombre, EstadoDocumento.color
    ).all()
    
    return [{'nombre': e.nombre, 'color': e.color, 'cantidad': e.cantidad} for e in estados]

def datos_grafico_tiempo(query, filtros):
    """Obtiene datos para gráfico de tiempo"""
    # Obtener parámetros de filtro
    dias = filtros.get('dias', 30)
    try:
        dias = int(dias)
    except ValueError:
        dias = 30
    
    # Calcular fecha límite
    fecha_limite = datetime.now() - timedelta(days=dias)
    
    # Agrupar por día
    resultados = db.session.query(
        func.date(Movimiento.fecha_hora).label('fecha'),
        func.count(Movimiento.id).label('cantidad')
    ).join(
        Documento, Documento.id == Movimiento.documento_id
    ).filter(
        Movimiento.fecha_hora >= fecha_limite,
        Documento.id.in_(query.with_entities(Documento.id))
    ).group_by(
        func.date(Movimiento.fecha_hora)
    ).order_by(
        func.date(Movimiento.fecha_hora)
    ).all()
    
    return [{'fecha': r.fecha.strftime('%Y-%m-%d'), 'cantidad': r.cantidad} for r in resultados]

def datos_grafico_por_tipo_documento(query):
    """Obtiene datos para gráfico por tipo de documento"""
    # Contar documentos por tipo
    tipos = db.session.query(
        TipoDocumento.nombre,
        func.count(Documento.id).label('cantidad')
    ).join(
        Documento, Documento.tipo_documento_id == TipoDocumento.id
    ).filter(
        Documento.id.in_(query.with_entities(Documento.id))
    ).group_by(
        TipoDocumento.nombre
    ).all()
    
    return [{'nombre': t.nombre, 'cantidad': t.cantidad} for t in tipos]

def generar_reporte_personalizado(query, dimension1, dimension2):
    """Genera un reporte personalizado basado en las dimensiones seleccionadas"""
    # Mapear nombres de dimensiones a columnas de la base de datos
    dimensiones = {
        'area': {'col': Documento.area_destino_id, 'rel': 'area_destino', 'attr': 'nombre'},
        'estado': {'col': Documento.estado_actual_id, 'rel': 'estado_actual', 'attr': 'nombre'},
        'tipo_documento': {'col': Documento.tipo_documento_id, 'rel': 'tipo_documento', 'attr': 'nombre'},
        'transportadora': {'col': Documento.transportadora_id, 'rel': 'transportadora', 'attr': 'nombre'},
        'tipo': {'col': Documento.tipo, 'rel': None, 'attr': None},
        'mes': {'col': func.month(Documento.fecha_recepcion), 'rel': None, 'attr': None},
        'anio': {'col': func.year(Documento.fecha_recepcion), 'rel': None, 'attr': None},
    }
    
    # Validar dimensiones seleccionadas
    if dimension1 not in dimensiones or dimension2 not in dimensiones:
        return []
    
    # Construir consulta dinámica
    dim1 = dimensiones[dimension1]
    dim2 = dimensiones[dimension2]
    
    # Manejamos casos especiales
    if dimension1 == 'mes':
        label1 = func.date_format(Documento.fecha_recepcion, '%Y-%m').label('dim1')
    elif dimension1 == 'anio':
        label1 = func.year(Documento.fecha_recepcion).label('dim1')
    elif dim1['rel'] is None:
        label1 = dim1['col'].label('dim1')
    else:
        # Corrección aquí
        modelo_rel = getattr(Documento, dim1['rel']).prop.mapper.class_
        label1 = getattr(modelo_rel, dim1['attr']).label('dim1')
    
    if dimension2 == 'mes':
        label2 = func.date_format(Documento.fecha_recepcion, '%Y-%m').label('dim2')
    elif dimension2 == 'anio':
        label2 = func.year(Documento.fecha_recepcion).label('dim2')
    elif dim2['rel'] is None:
        label2 = dim2['col'].label('dim2')
    else:
        # Corrección aquí
        modelo_rel = getattr(Documento, dim2['rel']).prop.mapper.class_
        label2 = getattr(modelo_rel, dim2['attr']).label('dim2')
    
    # Realizar la consulta
    resultados = db.session.query(
        label1,
        label2,
        func.count(Documento.id).label('cantidad')
    ).filter(
        Documento.id.in_(query.with_entities(Documento.id))
    ).group_by(
        'dim1', 'dim2'
    ).all()
    
    # Transformar resultados para la visualización
    matriz = {}
    
    for r in resultados:
        dim1_valor = str(r.dim1)
        dim2_valor = str(r.dim2)
        
        if dim1_valor not in matriz:
            matriz[dim1_valor] = {}
        
        matriz[dim1_valor][dim2_valor] = r.cantidad
    
    # Obtener todos los valores únicos de la segunda dimensión
    valores_dim2 = sorted(set(dim2_valor for r in resultados for dim2_valor in [str(r.dim2)]))
    
    return matriz

def preparar_datos_exportacion_area(query):
    """Prepara los datos del reporte por área para exportación"""
    areas = Area.query.all()
    datos = []
    
    # Encabezados
    encabezados = ['Área', 'Estado', 'Cantidad', 'Porcentaje del Área']
    
    for area in areas:
        # Contar total para esta área
        total_area = query.filter(Documento.area_destino_id == area.id).count()
        
        if total_area > 0:
            # Obtener distribución por estados para esta área
            estados = db.session.query(
                EstadoDocumento.nombre,
                func.count(Documento.id).label('cantidad')
            ).join(
                Documento, Documento.estado_actual_id == EstadoDocumento.id
            ).filter(
                Documento.area_destino_id == area.id,
                Documento.id.in_(query.with_entities(Documento.id))
            ).group_by(
                EstadoDocumento.nombre
            ).all()
            
            # Añadir registros para cada estado
            for estado in estados:
                porcentaje = round((estado.cantidad / total_area) * 100, 2)
                datos.append({
                    'Área': area.nombre,
                    'Estado': estado.nombre,
                    'Cantidad': estado.cantidad,
                    'Porcentaje del Área': f"{porcentaje}%"
                })
    
    return {'encabezados': encabezados, 'datos': datos}

def preparar_datos_exportacion_estado(query):
    """Prepara los datos del reporte por estado para exportación"""
    estados = EstadoDocumento.query.all()
    datos = []
    
    # Encabezados
    encabezados = ['Estado', 'Cantidad', 'Porcentaje Total', 'Áreas Principales']
    
    # Total general de documentos
    total_docs = query.count()
    
    for estado in estados:
        # Contar documentos en este estado
        docs_estado = query.filter(Documento.estado_actual_id == estado.id)
        cantidad = docs_estado.count()
        
        if cantidad > 0:
            # Calcular porcentaje
            porcentaje = round((cantidad / total_docs) * 100, 2) if total_docs > 0 else 0
            
            # Obtener las áreas con más documentos en este estado
            areas_top = db.session.query(
                Area.nombre,
                func.count(Documento.id).label('cantidad')
            ).join(
                Documento, Documento.area_destino_id == Area.id
            ).filter(
                Documento.estado_actual_id == estado.id,
                Documento.id.in_(query.with_entities(Documento.id))
            ).group_by(
                Area.nombre
            ).order_by(
                func.count(Documento.id).desc()
            ).limit(3).all()
            
            # Formatear las áreas principales
            areas_principales = ', '.join([f"{a.nombre} ({a.cantidad})" for a in areas_top])
            
            datos.append({
                'Estado': estado.nombre,
                'Cantidad': cantidad,
                'Porcentaje Total': f"{porcentaje}%",
                'Áreas Principales': areas_principales
            })
    
    return {'encabezados': encabezados, 'datos': datos}

def preparar_datos_exportacion_tiempo(query, filtros):
    """Prepara los datos del reporte de tiempos para exportación"""
    # Obtener parámetros de filtro
    dias = filtros.get('dias', 30)
    try:
        dias = int(dias)
    except ValueError:
        dias = 30
    
    # Calcular fecha límite
    fecha_limite = datetime.now() - timedelta(days=dias)
    
    # Obtener documentos finalizados
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    estados_finales = []
    if estado_finalizado:
        estados_finales.append(estado_finalizado.id)
    if estado_archivado:
        estados_finales.append(estado_archivado.id)
    
    documentos = query.filter(
        Documento.estado_actual_id.in_(estados_finales),
        Documento.creado_en >= fecha_limite
    ).all()
    
    # Preprocesar datos
    datos_docs = []
    encabezados = ['Radicado', 'Tipo Documento', 'Remitente', 'Área', 'Fecha Inicio', 'Fecha Fin', 'Duración (h)', 'Duración (días)']
    
    for doc in documentos:
        # Obtener primer y último movimiento
        primer_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora).first()
        ultimo_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora.desc()).first()
        
        if primer_mov and ultimo_mov:
            # Calcular duración
            duracion = ultimo_mov.fecha_hora - primer_mov.fecha_hora
            horas = duracion.total_seconds() / 3600
            dias = horas / 24
            
            datos_docs.append({
                'Radicado': doc.radicado,
                'Tipo Documento': doc.tipo_documento.nombre,
                'Remitente': doc.remitente,
                'Área': doc.area_destino.nombre,
                'Fecha Inicio': primer_mov.fecha_hora.strftime('%Y-%m-%d %H:%M'),
                'Fecha Fin': ultimo_mov.fecha_hora.strftime('%Y-%m-%d %H:%M'),
                'Duración (h)': round(horas, 2),
                'Duración (días)': round(dias, 2)
            })
    
    return {'encabezados': encabezados, 'datos': datos_docs}

def preparar_datos_exportacion_tendencias(periodo, filtros):
    """Prepara los datos de tendencias para exportación"""
    # Obtener los datos de tendencias
    if periodo == 'mensual':
        datos_tendencia = calcular_tendencias(periodo='mensual', meses=12, filtros=filtros)
        encabezados = ['Mes', 'Documentos Recibidos', 'Documentos Finalizados', 'Tiempo Promedio (días)']
    elif periodo == 'semanal':
        datos_tendencia = calcular_tendencias(periodo='semanal', semanas=12, filtros=filtros)
        encabezados = ['Semana', 'Documentos Recibidos', 'Documentos Finalizados', 'Tiempo Promedio (días)']
    else:  # diario
        datos_tendencia = calcular_tendencias(periodo='diario', dias=30, filtros=filtros)
        encabezados = ['Fecha', 'Documentos Recibidos', 'Documentos Finalizados', 'Tiempo Promedio (días)']
    
    # Formatear datos para exportación
    datos_formateados = []
    
    for registro in datos_tendencia:
        datos_formateados.append({
            encabezados[0]: registro['periodo'],
            encabezados[1]: registro['docs_recibidos'],
            encabezados[2]: registro['docs_finalizados'],
            encabezados[3]: round(registro['tiempo_promedio'], 2)
        })
    
    return {'encabezados': encabezados, 'datos': datos_formateados}

def preparar_datos_exportacion_personalizado(query, dimension1, dimension2):
    """Prepara los datos del reporte personalizado para exportación"""
    # Obtener los resultados del reporte personalizado
    resultados = generar_reporte_personalizado(query, dimension1, dimension2)
    
    # Formatear nombres de dimensiones para encabezados
    nombres_dimensiones = {
        'area': 'Área',
        'estado': 'Estado',
        'tipo_documento': 'Tipo de Documento',
        'transportadora': 'Transportadora',
        'tipo': 'Tipo',
        'mes': 'Mes',
        'anio': 'Año'
    }
    
    dim1_nombre = nombres_dimensiones.get(dimension1, dimension1.capitalize())
    dim2_nombre = nombres_dimensiones.get(dimension2, dimension2.capitalize())
    
    # Obtener todos los valores únicos de la segunda dimensión
    valores_dim2 = set()
    for dim1 in resultados:
        for dim2 in resultados[dim1]:
            valores_dim2.add(dim2)
    
    valores_dim2 = sorted(valores_dim2)
    
    # Preparar datos para exportación
    encabezados = [dim1_nombre] + [f"{dim2_nombre}: {valor}" for valor in valores_dim2] + ['Total']
    
    datos = []
    for dim1 in sorted(resultados.keys()):
        fila = {dim1_nombre: dim1}
        total_fila = 0
        
        for dim2 in valores_dim2:
            cantidad = resultados[dim1].get(dim2, 0)
            fila[f"{dim2_nombre}: {dim2}"] = cantidad
            total_fila += cantidad
        
        fila['Total'] = total_fila
        datos.append(fila)
    
    return {'encabezados': encabezados, 'datos': datos}

