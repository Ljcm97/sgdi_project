from flask import Blueprint, render_template, redirect, url_for, jsonify, flash
from flask_login import login_required, current_user
from app.models.notificacion import Notificacion
from app.models.documento import Documento
from app.utils.decorators import has_document_access

notificaciones_bp = Blueprint('notificaciones', __name__, url_prefix='/notificaciones')

@notificaciones_bp.route('/')
@login_required
def index():
    """Vista para mostrar todas las notificaciones del usuario"""
    notificaciones = Notificacion.query.filter_by(usuario_id=current_user.id).order_by(Notificacion.creado_en.desc()).all()
    return render_template('notificaciones/index.html', notificaciones=notificaciones)


@notificaciones_bp.route('/marcar-leida/<int:id>')
@login_required
def marcar_leida(id):
    """Vista para marcar una notificación como leída"""
    notificacion = Notificacion.query.filter_by(id=id, usuario_id=current_user.id).first_or_404()
    notificacion.marcar_como_leida()
    
    # Redirigir al documento si existe
    if notificacion.documento_id:
        try:
            documento = Documento.query.get(notificacion.documento_id)
            
            # Verificar si el documento existe y si el usuario tiene acceso
            if documento and has_document_access(documento):
                return redirect(url_for('documentos.detalle', id=notificacion.documento_id))
            else:
                flash('No tienes acceso al documento relacionado.', 'warning')
                return redirect(url_for('notificaciones.index'))
        except Exception as e:
            flash('Error al acceder al documento: ' + str(e), 'danger')
            return redirect(url_for('notificaciones.index'))
    
    return redirect(url_for('notificaciones.index'))


@notificaciones_bp.route('/marcar-todas-leidas')
@login_required
def marcar_todas_leidas():
    """Vista para marcar todas las notificaciones como leídas"""
    notificaciones = Notificacion.query.filter_by(usuario_id=current_user.id, leida=False).all()
    
    for notificacion in notificaciones:
        notificacion.marcar_como_leida()
    
    return redirect(url_for('notificaciones.index'))


@notificaciones_bp.route('/no-leidas')
@login_required
def no_leidas():
    """API para obtener el número de notificaciones no leídas"""
    cantidad = Notificacion.query.filter_by(usuario_id=current_user.id, leida=False).count()
    return jsonify({'cantidad': cantidad})


@notificaciones_bp.route('/recientes')
@login_required
def recientes():
    """API para obtener las notificaciones recientes no leídas"""
    notificaciones = Notificacion.query.filter_by(
        usuario_id=current_user.id, 
        leida=False
    ).order_by(
        Notificacion.creado_en.desc()
    ).limit(5).all()
    
    # Asegúrate de que no haya duplicados por ID
    unique_notifs = {}
    for notif in notificaciones:
        if notif.id not in unique_notifs:
            unique_notifs[notif.id] = notif
    
    result = []
    for notif_id, notif in unique_notifs.items():
        item = {
            'id': notif.id,
            'titulo': notif.titulo,
            'mensaje': notif.mensaje,
            'creado_en': notif.creado_en.strftime('%d/%m/%Y %H:%M'),
            'documento_id': notif.documento_id
        }
        
        # Agregar información del documento si existe
        if notif.documento_id:
            doc = Documento.query.get(notif.documento_id)
            if doc:
                item['radicado'] = doc.radicado
        
        result.append(item)
    
    return jsonify(result)

