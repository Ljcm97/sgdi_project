from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from app.models.documento import Documento
from app.models.estado_documento import EstadoDocumento
from sqlalchemy import or_

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    """Vista del dashboard principal"""
    # Obtener estados para filtrar
    estado_recibido = EstadoDocumento.query.filter_by(nombre='Recibido').first()
    estado_en_proceso = EstadoDocumento.query.filter_by(nombre='En proceso').first()
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    # Contar documentos pendientes (recibidos + en proceso)
    pendientes_query = Documento.query.filter(
        Documento.estado_actual_id.in_([estado_recibido.id, estado_en_proceso.id])
    )
    
    # Contar documentos finalizados (incluye los archivados)
    finalizados_query = Documento.query.filter(
        Documento.estado_actual_id.in_([
            estado_finalizado.id if estado_finalizado else None,
            estado_archivado.id if estado_archivado else None
        ])
    )
    
    # Filtrar según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador':
        # Superadministrador ve todos los documentos
        pass
    elif current_user.rol.nombre == 'Recepción':
        # Recepción ve los documentos que ha registrado
        pendientes_query = pendientes_query.filter_by(registrado_por_id=current_user.id)
        finalizados_query = finalizados_query.filter_by(registrado_por_id=current_user.id)
    else:
        # Usuario regular ve los documentos de su área o asignados a él
        pendientes_query = pendientes_query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        )
        finalizados_query = finalizados_query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        )
    
    # Contar los documentos
    documentos_pendientes = pendientes_query.count()
    documentos_finalizados = finalizados_query.count()
    
    # Obtener documentos recientes (últimos 5)
    documentos_recientes = pendientes_query.order_by(Documento.creado_en.desc()).limit(5).all()
    
    # Preparar IDs de estado para filtros en la búsqueda
    estado_pendiente_id = ",".join([str(estado_recibido.id), str(estado_en_proceso.id)])
    
    # Incluir estado finalizado y archivado
    estado_finalizado_ids = []
    if estado_finalizado:
        estado_finalizado_ids.append(str(estado_finalizado.id))
    if estado_archivado:
        estado_finalizado_ids.append(str(estado_archivado.id))
    
    estado_finalizado_id = ",".join(estado_finalizado_ids)
    
    return render_template('dashboard.html',
                          documentos_pendientes=documentos_pendientes,
                          documentos_finalizados=documentos_finalizados,
                          documentos_recientes=documentos_recientes,
                          estado_pendiente_id=estado_pendiente_id,
                          estado_finalizado_id=estado_finalizado_id)

@dashboard_bp.route('/contador-documentos')
@login_required
def contador_documentos():
    """API para obtener contador de documentos pendientes y finalizados"""
    # Obtener estados para filtrar
    estado_recibido = EstadoDocumento.query.filter_by(nombre='Recibido').first()
    estado_en_proceso = EstadoDocumento.query.filter_by(nombre='En proceso').first()
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    # Contar documentos pendientes (recibidos + en proceso)
    pendientes_query = Documento.query.filter(
        Documento.estado_actual_id.in_([estado_recibido.id, estado_en_proceso.id])
    )
    
    # Contar documentos finalizados (incluye los archivados)
    finalizados_query = Documento.query.filter(
        Documento.estado_actual_id.in_([
            estado_finalizado.id if estado_finalizado else None,
            estado_archivado.id if estado_archivado else None
        ])
    )
    
    # Filtrar según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador':
        # Superadministrador ve todos los documentos
        pass
    elif current_user.rol.nombre == 'Recepción':
        # Recepción ve los documentos que ha registrado
        pendientes_query = pendientes_query.filter_by(registrado_por_id=current_user.id)
        finalizados_query = finalizados_query.filter_by(registrado_por_id=current_user.id)
    else:
        # Usuario regular ve los documentos de su área o asignados a él
        pendientes_query = pendientes_query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        )
        finalizados_query = finalizados_query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        )
    
    # Contar los documentos
    documentos_pendientes = pendientes_query.count()
    documentos_finalizados = finalizados_query.count()
    
    # Devolver los datos en formato JSON
    return jsonify({
        'documentos_pendientes': documentos_pendientes,
        'documentos_finalizados': documentos_finalizados
    })
