from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from sqlalchemy import func, and_, or_, desc
from datetime import datetime, timedelta
from app import db
from app.models.documento import Documento
from app.models.movimiento import Movimiento
from app.models.area import Area
from app.models.estado_documento import EstadoDocumento
from app.utils.auth import permission_required
from app.utils.helpers import format_date

reportes_bp = Blueprint('reportes', __name__, url_prefix='/reportes')

@reportes_bp.route('/')
@login_required
@permission_required('ver_reportes')
def index():
    """Vista principal de reportes"""
    return render_template('reportes/index.html')

@reportes_bp.route('/por-area')
@login_required
@permission_required('ver_reportes')
def por_area():
    """Reporte de documentos por área"""
    areas = Area.query.all()
    
    # Filtrar según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador' or current_user.rol.nombre == 'Recepción':
        # Pueden ver todas las áreas
        pass
    else:
        # Solo pueden ver su área
        areas = [current_user.persona.area]
    
    # Obtener estadísticas por área
    resultados = []
    for area in areas:
        # Contar documentos por estado
        stats = db.session.query(
            EstadoDocumento.nombre.label('estado'),
            EstadoDocumento.color.label('color'),
            func.count(Documento.id).label('cantidad')
        ).join(
            Documento, Documento.estado_actual_id == EstadoDocumento.id
        ).filter(
            Documento.area_destino_id == area.id
        ).group_by(
            EstadoDocumento.nombre, EstadoDocumento.color
        ).all()
        
        # Formatear resultados
        estados = [{'estado': s.estado, 'color': s.color, 'cantidad': s.cantidad} for s in stats]
        
        # Calcular total
        total = sum(e['cantidad'] for e in estados)
        
        resultados.append({
            'area': area.nombre,
            'estados': estados,
            'total': total
        })
    
    return render_template('reportes/por_area.html', resultados=resultados)

@reportes_bp.route('/por-estado')
@login_required
@permission_required('ver_reportes')
def por_estado():
    """Reporte de documentos por estado"""
    estados = EstadoDocumento.query.all()
    
    # Crear consulta base según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador' or current_user.rol.nombre == 'Recepción':
        # Pueden ver todos los documentos
        base_query = Documento.query
    else:
        # Solo pueden ver documentos de su área
        base_query = Documento.query.filter(Documento.area_destino_id == current_user.persona.area_id)
    
    # Obtener estadísticas por estado
    resultados = []
    for estado in estados:
        # Contar documentos en este estado
        cantidad = base_query.filter(Documento.estado_actual_id == estado.id).count()
        
        # Obtener documentos recientes en este estado (últimos 5)
        documentos = base_query.filter(
            Documento.estado_actual_id == estado.id
        ).order_by(
            Documento.fecha_recepcion.desc()
        ).limit(5).all()
        
        resultados.append({
            'estado': estado.nombre,
            'color': estado.color,
            'cantidad': cantidad,
            'documentos': documentos
        })
    
    return render_template('reportes/por_estado.html', resultados=resultados)

@reportes_bp.route('/tiempo-procesamiento')
@login_required
@permission_required('ver_reportes')
def tiempo_procesamiento():
    """Reporte de tiempo de procesamiento de documentos"""
    # Obtener parámetros de filtro
    dias = request.args.get('dias', '30')
    try:
        dias = int(dias)
    except ValueError:
        dias = 30
    
    # Calcular fecha límite
    fecha_limite = datetime.now() - timedelta(days=dias)
    
    # Crear consulta base según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador' or current_user.rol.nombre == 'Recepción':
        # Pueden ver todos los documentos
        base_query = db.session.query(Documento)
    else:
        # Solo pueden ver documentos de su área
        base_query = db.session.query(Documento).filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        )
    
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
                              mensaje="No se encontraron estados de finalización o archivado en el sistema.")
    
    documentos = base_query.filter(
        Documento.estado_actual_id.in_(estados_finales),
        Documento.creado_en >= fecha_limite
    ).all()
    
    # Calcular tiempos de procesamiento
    resultados = []
    for doc in documentos:
        # Obtener primer y último movimiento
        primer_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora).first()
        ultimo_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora.desc()).first()
        
        if primer_mov and ultimo_mov:
            # Calcular duración en horas
            duracion = ultimo_mov.fecha_hora - primer_mov.fecha_hora
            horas = duracion.total_seconds() / 3600
            
            resultados.append({
                'documento': doc,
                'inicio': primer_mov.fecha_hora,
                'fin': ultimo_mov.fecha_hora,
                'duracion_horas': round(horas, 2),
                'duracion_dias': round(horas / 24, 2)
            })
    
    # Ordenar por duración (mayor a menor)
    resultados.sort(key=lambda x: x['duracion_horas'], reverse=True)
    
    return render_template('reportes/tiempo_procesamiento.html', 
                          resultados=resultados,
                          dias=dias)

@reportes_bp.route('/datos-grafico')
@login_required
@permission_required('ver_reportes')
def datos_grafico():
    """API para obtener datos para gráficos en formato JSON"""
    tipo = request.args.get('tipo', 'area')
    
    if tipo == 'area':
        # Datos para gráfico por área
        areas = Area.query.all()
        
        # Filtrar según el rol del usuario
        if not (current_user.rol.nombre == 'Superadministrador' or current_user.rol.nombre == 'Recepción'):
            areas = [current_user.persona.area]
        
        datos = []
        for area in areas:
            # Contar total de documentos
            total = Documento.query.filter(Documento.area_destino_id == area.id).count()
            
            # Contar por estados
            estados = db.session.query(
                EstadoDocumento.nombre,
                EstadoDocumento.color,
                func.count(Documento.id).label('cantidad')
            ).join(
                Documento, Documento.estado_actual_id == EstadoDocumento.id
            ).filter(
                Documento.area_destino_id == area.id
            ).group_by(
                EstadoDocumento.nombre, EstadoDocumento.color
            ).all()
            
            # Añadir a resultados
            datos.append({
                'area': area.nombre,
                'total': total,
                'estados': [{'nombre': e.nombre, 'color': e.color, 'cantidad': e.cantidad} for e in estados]
            })
        
        return jsonify(datos)
    
    elif tipo == 'estado':
        # Datos para gráfico por estado
        # Crear consulta base según el rol del usuario
        if current_user.rol.nombre == 'Superadministrador' or current_user.rol.nombre == 'Recepción':
            # Pueden ver todos los documentos
            base_query = Documento.query
        else:
            # Solo pueden ver documentos de su área
            base_query = Documento.query.filter(Documento.area_destino_id == current_user.persona.area_id)
        
        # Contar documentos por estado
        estados = db.session.query(
            EstadoDocumento.nombre,
            EstadoDocumento.color,
            func.count(Documento.id).label('cantidad')
        ).join(
            Documento, Documento.estado_actual_id == EstadoDocumento.id
        ).filter(
            Documento.id.in_(base_query.with_entities(Documento.id))
        ).group_by(
            EstadoDocumento.nombre, EstadoDocumento.color
        ).all()
        
        datos = [{'nombre': e.nombre, 'color': e.color, 'cantidad': e.cantidad} for e in estados]
        return jsonify(datos)
    
    elif tipo == 'tiempo':
        # Datos para gráfico de tiempo
        # Obtener parámetros de filtro
        dias = request.args.get('dias', '30')
        try:
            dias = int(dias)
        except ValueError:
            dias = 30
        
        # Calcular fecha límite
        fecha_limite = datetime.now() - timedelta(days=dias)
        
        # Obtener documentos finalizados por día
        if current_user.rol.nombre == 'Superadministrador' or current_user.rol.nombre == 'Recepción':
            # Pueden ver todos los documentos
            base_query = Documento.query
        else:
            # Solo pueden ver documentos de su área
            base_query = Documento.query.filter(
                or_(
                    Documento.area_destino_id == current_user.persona.area_id,
                    Documento.persona_destino_id == current_user.persona_id
                )
            )
        
        # Agrupar por día
        resultados = db.session.query(
            func.date(Movimiento.fecha_hora).label('fecha'),
            func.count(Movimiento.id).label('cantidad')
        ).join(
            Documento, Documento.id == Movimiento.documento_id
        ).filter(
            Movimiento.fecha_hora >= fecha_limite,
            Documento.id.in_(base_query.with_entities(Documento.id))
        ).group_by(
            func.date(Movimiento.fecha_hora)
        ).order_by(
            func.date(Movimiento.fecha_hora)
        ).all()
        
        datos = [{'fecha': r.fecha.strftime('%Y-%m-%d'), 'cantidad': r.cantidad} for r in resultados]
        return jsonify(datos)
    
    return jsonify([])