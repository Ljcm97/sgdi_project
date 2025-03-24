from datetime import datetime, timedelta
from sqlalchemy import func, and_, case, extract, text
from app import db
from app.models.documento import Documento
from app.models.movimiento import Movimiento
from app.models.estado_documento import EstadoDocumento
from app.models.area import Area
from flask_login import current_user
from calendar import monthrange

def calcular_tiempo_procesamiento(dias=30, filtros=None):
    """
    Calcula el tiempo promedio de procesamiento de documentos
    
    Args:
        dias (int): Número de días a considerar
        filtros (dict): Filtros adicionales a aplicar
    
    Returns:
        float: Tiempo promedio en horas
    """
    from app.controllers.reportes import crear_query_base_segun_rol, aplicar_filtros_a_query
    
    # Calcular fecha límite
    fecha_limite = datetime.now() - timedelta(days=dias)
    
    # Crear consulta base según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    if filtros:
        query = aplicar_filtros_a_query(query_base, filtros)
    else:
        query = query_base
    
    # Obtener documentos finalizados
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    estados_finales = []
    if estado_finalizado:
        estados_finales.append(estado_finalizado.id)
    if estado_archivado:
        estados_finales.append(estado_archivado.id)
    
    if not estados_finales:
        return 0
    
    # Filtrar documentos finalizados en el período
    documentos = query.filter(
        Documento.estado_actual_id.in_(estados_finales),
        Documento.creado_en >= fecha_limite
    ).all()
    
    # Calcular tiempo promedio
    tiempos = []
    
    for doc in documentos:
        # Obtener primer y último movimiento
        primer_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora).first()
        ultimo_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora.desc()).first()
        
        if primer_mov and ultimo_mov:
            # Calcular duración en horas
            duracion = ultimo_mov.fecha_hora - primer_mov.fecha_hora
            horas = duracion.total_seconds() / 3600
            tiempos.append(horas)
    
    # Calcular promedio
    if tiempos:
        return sum(tiempos) / len(tiempos)
    else:
        return 0

def calcular_tendencias(periodo='mensual', meses=12, semanas=12, dias=30, filtros=None):
    """
    Calcula tendencias de documentos a lo largo del tiempo
    
    Args:
        periodo (str): 'mensual', 'semanal' o 'diario'
        meses (int): Número de meses a considerar (para período mensual)
        semanas (int): Número de semanas a considerar (para período semanal)
        dias (int): Número de días a considerar (para período diario)
        filtros (dict): Filtros adicionales a aplicar
    
    Returns:
        list: Lista de datos de tendencias
    """
    from app.controllers.reportes import crear_query_base_segun_rol, aplicar_filtros_a_query
    
    # Determinar fecha límite según el período
    now = datetime.now()
    
    if periodo == 'mensual':
        # Retroceder N meses
        if meses > 0:
            year = now.year
            month = now.month - meses
            
            while month <= 0:
                month += 12
                year -= 1
            
            fecha_limite = datetime(year, month, 1)
        else:
            fecha_limite = now
    elif periodo == 'semanal':
        # Retroceder N semanas
        fecha_limite = now - timedelta(weeks=semanas)
    else:  # diario
        # Retroceder N días
        fecha_limite = now - timedelta(days=dias)
    
    # Crear consulta base según el rol del usuario
    query_base = crear_query_base_segun_rol()
    
    # Aplicar filtros adicionales
    if filtros:
        query = aplicar_filtros_a_query(query_base, filtros)
    else:
        query = query_base
    
    # Preparar resultados según el período
    if periodo == 'mensual':
        return calcular_tendencias_mensuales(query, fecha_limite, now)
    elif periodo == 'semanal':
        return calcular_tendencias_semanales(query, fecha_limite, now)
    else:  # diario
        return calcular_tendencias_diarias(query, fecha_limite, now)

def calcular_tendencias_mensuales(query, fecha_inicio, fecha_fin):
    """Calcula tendencias mensuales"""
    # Obtener todos los meses entre las fechas
    resultados = []
    current_date = fecha_inicio
    
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    estados_finales = []
    if estado_finalizado:
        estados_finales.append(estado_finalizado.id)
    if estado_archivado:
        estados_finales.append(estado_archivado.id)
    
    while current_date <= fecha_fin:
        year = current_date.year
        month = current_date.month
        
        # Calcular el primer y último día del mes
        _, last_day = monthrange(year, month)
        mes_inicio = datetime(year, month, 1)
        mes_fin = datetime(year, month, last_day, 23, 59, 59)
        
        # Contar documentos recibidos en el mes
        docs_recibidos = query.filter(
            Documento.fecha_recepcion >= mes_inicio,
            Documento.fecha_recepcion <= mes_fin
        ).count()
        
        # Contar documentos finalizados en el mes
        if estados_finales:
            docs_finalizados = query.join(Movimiento).filter(
                Documento.estado_actual_id.in_(estados_finales),
                Movimiento.fecha_hora >= mes_inicio,
                Movimiento.fecha_hora <= mes_fin,
                Movimiento.estado_documento_id.in_(estados_finales)
            ).distinct(Documento.id).count()
        else:
            docs_finalizados = 0
        
        # Calcular tiempo promedio de procesamiento en el mes
        tiempo_promedio = 0
        documentos_mes = query.filter(
            Documento.fecha_recepcion >= mes_inicio,
            Documento.fecha_recepcion <= mes_fin
        ).all()
        
        tiempos = []
        for doc in documentos_mes:
            if doc.estado_actual_id in estados_finales:
                primer_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora).first()
                ultimo_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora.desc()).first()
                
                if primer_mov and ultimo_mov:
                    duracion = ultimo_mov.fecha_hora - primer_mov.fecha_hora
                    horas = duracion.total_seconds() / 3600
                    tiempos.append(horas)
        
        if tiempos:
            tiempo_promedio = sum(tiempos) / len(tiempos) / 24  # Convertir a días
        
        # Formar el nombre del mes
        nombre_mes = f"{current_date.strftime('%Y-%m')}"
        
        # Añadir a resultados
        resultados.append({
            'periodo': nombre_mes,
            'docs_recibidos': docs_recibidos,
            'docs_finalizados': docs_finalizados,
            'tiempo_promedio': tiempo_promedio
        })
        
        # Avanzar al siguiente mes
        if month == 12:
            current_date = datetime(year + 1, 1, 1)
        else:
            current_date = datetime(year, month + 1, 1)
    
    return resultados

def calcular_tendencias_semanales(query, fecha_inicio, fecha_fin):
    """Calcula tendencias semanales"""
    # Ajustar fecha_inicio al inicio de la semana (lunes)
    dias_al_lunes = fecha_inicio.weekday()
    fecha_inicio = fecha_inicio - timedelta(days=dias_al_lunes)
    
    # Obtener todas las semanas entre las fechas
    resultados = []
    current_date = fecha_inicio
    
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    estados_finales = []
    if estado_finalizado:
        estados_finales.append(estado_finalizado.id)
    if estado_archivado:
        estados_finales.append(estado_archivado.id)
    
    while current_date <= fecha_fin:
        # Calcular el fin de la semana (domingo)
        semana_fin = current_date + timedelta(days=6, hours=23, minutes=59, seconds=59)
        
        # Contar documentos recibidos en la semana
        docs_recibidos = query.filter(
            Documento.fecha_recepcion >= current_date,
            Documento.fecha_recepcion <= semana_fin
        ).count()
        
        # Contar documentos finalizados en la semana
        if estados_finales:
            docs_finalizados = query.join(Movimiento).filter(
                Documento.estado_actual_id.in_(estados_finales),
                Movimiento.fecha_hora >= current_date,
                Movimiento.fecha_hora <= semana_fin,
                Movimiento.estado_documento_id.in_(estados_finales)
            ).distinct(Documento.id).count()
        else:
            docs_finalizados = 0
        
        # Calcular tiempo promedio de procesamiento en la semana
        tiempo_promedio = 0
        documentos_semana = query.filter(
            Documento.fecha_recepcion >= current_date,
            Documento.fecha_recepcion <= semana_fin
        ).all()
        
        tiempos = []
        for doc in documentos_semana:
            if doc.estado_actual_id in estados_finales:
                primer_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora).first()
                ultimo_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora.desc()).first()
                
                if primer_mov and ultimo_mov:
                    duracion = ultimo_mov.fecha_hora - primer_mov.fecha_hora
                    horas = duracion.total_seconds() / 3600
                    tiempos.append(horas)
        
        if tiempos:
            tiempo_promedio = sum(tiempos) / len(tiempos) / 24  # Convertir a días
        
        # Formar el nombre de la semana
        nombre_semana = f"{current_date.strftime('%Y-%m-%d')} al {semana_fin.strftime('%Y-%m-%d')}"
        
        # Añadir a resultados
        resultados.append({
            'periodo': nombre_semana,
            'docs_recibidos': docs_recibidos,
            'docs_finalizados': docs_finalizados,
            'tiempo_promedio': tiempo_promedio
        })
        
        # Avanzar a la siguiente semana
        current_date = semana_fin + timedelta(seconds=1)
    
    return resultados

def calcular_tendencias_diarias(query, fecha_inicio, fecha_fin):
    """Calcula tendencias diarias"""
    # Obtener todos los días entre las fechas
    resultados = []
    current_date = fecha_inicio.replace(hour=0, minute=0, second=0, microsecond=0)
    
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    estados_finales = []
    if estado_finalizado:
        estados_finales.append(estado_finalizado.id)
    if estado_archivado:
        estados_finales.append(estado_archivado.id)
    
    while current_date <= fecha_fin:
        # Calcular el fin del día
        dia_fin = current_date.replace(hour=23, minute=59, second=59)
        
        # Contar documentos recibidos en el día
        docs_recibidos = query.filter(
            Documento.fecha_recepcion >= current_date,
            Documento.fecha_recepcion <= dia_fin
        ).count()
        
        # Contar documentos finalizados en el día
        if estados_finales:
            docs_finalizados = query.join(Movimiento).filter(
                Documento.estado_actual_id.in_(estados_finales),
                Movimiento.fecha_hora >= current_date,
                Movimiento.fecha_hora <= dia_fin,
                Movimiento.estado_documento_id.in_(estados_finales)
            ).distinct(Documento.id).count()
        else:
            docs_finalizados = 0
        
        # Calcular tiempo promedio de procesamiento en el día
        tiempo_promedio = 0
        documentos_dia = query.filter(
            Documento.fecha_recepcion >= current_date,
            Documento.fecha_recepcion <= dia_fin
        ).all()
        
        tiempos = []
        for doc in documentos_dia:
            if doc.estado_actual_id in estados_finales:
                primer_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora).first()
                ultimo_mov = Movimiento.query.filter_by(documento_id=doc.id).order_by(Movimiento.fecha_hora.desc()).first()
                
                if primer_mov and ultimo_mov:
                    duracion = ultimo_mov.fecha_hora - primer_mov.fecha_hora
                    horas = duracion.total_seconds() / 3600
                    tiempos.append(horas)
        
        if tiempos:
            tiempo_promedio = sum(tiempos) / len(tiempos) / 24  # Convertir a días
        
        # Añadir a resultados
        resultados.append({
            'periodo': current_date.strftime('%Y-%m-%d'),
            'docs_recibidos': docs_recibidos,
            'docs_finalizados': docs_finalizados,
            'tiempo_promedio': tiempo_promedio
        })
        
        # Avanzar al siguiente día
        current_date += timedelta(days=1)
    
    return resultados
