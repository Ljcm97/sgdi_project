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
    estado_recepcionado = EstadoDocumento.query.filter_by(nombre='Recepcionado').first()
    estado_recibido = EstadoDocumento.query.filter_by(nombre='Recibido').first()
    estado_en_proceso = EstadoDocumento.query.filter_by(nombre='En proceso').first()
    estado_transferido = EstadoDocumento.query.filter_by(nombre='Documento Transferido').first()
    estado_rechazado = EstadoDocumento.query.filter_by(nombre='Rechazado').first()
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()

    # Crear lista de IDs de estados pendientes
    estados_pendientes = []
    if estado_recepcionado:
        estados_pendientes.append(estado_recepcionado.id)
    if estado_recibido:
        estados_pendientes.append(estado_recibido.id)
    if estado_en_proceso:
        estados_pendientes.append(estado_en_proceso.id)
    if estado_transferido:
        estados_pendientes.append(estado_transferido.id)
    if estado_rechazado:
        estados_pendientes.append(estado_rechazado.id)

    pendientes_query = Documento.query.filter(
        Documento.estado_actual_id.in_(estados_pendientes)
    )

    # Crear lista de IDs de estados finalizados
    estados_finalizados = []
    if estado_finalizado:
        estados_finalizados.append(estado_finalizado.id)
    if estado_archivado:
        estados_finalizados.append(estado_archivado.id)

    finalizados_query = Documento.query.filter(
        Documento.estado_actual_id.in_(estados_finalizados)
    )

    # Filtrar según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador':
        pass
    elif current_user.rol.nombre == 'Recepción':
        pendientes_query = pendientes_query.filter_by(registrado_por_id=current_user.id)
        finalizados_query = finalizados_query.filter_by(registrado_por_id=current_user.id)
    else:
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

    documentos_pendientes = pendientes_query.count()
    documentos_finalizados = finalizados_query.count()

    # Obtener documentos recientes (últimos 5) con los filtros aplicados correctamente
    recientes_query = Documento.query

    if current_user.rol.nombre == 'Superadministrador':
        pass
    elif current_user.rol.nombre == 'Recepción':
        recientes_query = recientes_query.filter_by(registrado_por_id=current_user.id)
    else:
        recientes_query = recientes_query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id,
                Documento.ultimo_transferido_por_id == current_user.id
            )
        )

    documentos_recientes = recientes_query.order_by(Documento.creado_en.desc()).limit(5).all()

    # Preparar IDs de estado para filtros en la búsqueda
    estado_pendiente_id = ",".join([str(id) for id in estados_pendientes])
    estado_finalizado_id = ",".join([str(id) for id in estados_finalizados])

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
    estado_recepcionado = EstadoDocumento.query.filter_by(nombre='Recepcionado').first()
    estado_recibido = EstadoDocumento.query.filter_by(nombre='Recibido').first()
    estado_en_proceso = EstadoDocumento.query.filter_by(nombre='En proceso').first()
    estado_transferido = EstadoDocumento.query.filter_by(nombre='Documento Transferido').first()
    estado_rechazado = EstadoDocumento.query.filter_by(nombre='Rechazado').first()
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()

    # Crear lista de IDs de estados pendientes
    estados_pendientes = []
    if estado_recepcionado:
        estados_pendientes.append(estado_recepcionado.id)
    if estado_recibido:
        estados_pendientes.append(estado_recibido.id)
    if estado_en_proceso:
        estados_pendientes.append(estado_en_proceso.id)
    if estado_transferido:
        estados_pendientes.append(estado_transferido.id)
    if estado_rechazado:
        estados_pendientes.append(estado_rechazado.id)

    pendientes_query = Documento.query.filter(
        Documento.estado_actual_id.in_(estados_pendientes)
    )

    # Crear lista de IDs de estados finalizados
    estados_finalizados = []
    if estado_finalizado:
        estados_finalizados.append(estado_finalizado.id)
    if estado_archivado:
        estados_finalizados.append(estado_archivado.id)

    finalizados_query = Documento.query.filter(
        Documento.estado_actual_id.in_(estados_finalizados)
    )

    # Filtrar según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador':
        pass
    elif current_user.rol.nombre == 'Recepción':
        pendientes_query = pendientes_query.filter_by(registrado_por_id=current_user.id)
        finalizados_query = finalizados_query.filter_by(registrado_por_id=current_user.id)
    else:
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

    documentos_pendientes = pendientes_query.count()
    documentos_finalizados = finalizados_query.count()

    return jsonify({
        'documentos_pendientes': documentos_pendientes,
        'documentos_finalizados': documentos_finalizados
    })
