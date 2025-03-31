from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user
from app.utils.auth import check_permission

def role_required(role_name):
    """
    Decorador que verifica si el usuario tiene un rol específico.
    
    Args:
        role_name (str): El nombre del rol requerido.
        
    Returns:
        function: Decorador que redirecciona si el usuario no tiene el rol.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Por favor inicia sesión para acceder.', 'warning')
                return redirect(url_for('auth.login'))
            
            if current_user.rol.nombre != role_name and current_user.rol.nombre != 'Superadministrador':
                flash(f'Se requiere el rol de {role_name} para acceder.', 'danger')
                return redirect(url_for('dashboard.index'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    """
    Decorador que verifica si el usuario es superadministrador.
    
    Returns:
        function: Decorador que redirecciona si el usuario no es superadministrador.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Por favor inicia sesión para acceder.', 'warning')
            return redirect(url_for('auth.login'))
        
        if current_user.rol.nombre != 'Superadministrador':
            flash('Se requiere ser administrador para acceder.', 'danger')
            return redirect(url_for('dashboard.index'))
        
        return f(*args, **kwargs)
    return decorated_function

def has_document_access(document):
    """
    Verifica si el usuario tiene acceso a un documento específico.
    
    Args:
        document: El documento que se va a verificar.
        
    Returns:
        bool: True si el usuario tiene acceso, False en caso contrario.
    """
    # El superadministrador tiene acceso a todos los documentos
    if current_user.rol.nombre == 'Superadministrador':
        return True
    
    # El usuario de recepción tiene acceso a todos los documentos que ha registrado
    if current_user.rol.nombre == 'Recepción' and document.registrado_por_id == current_user.id:
        return True
    
    # El usuario tiene acceso si está asignado al documento en el área actual
    if document.persona_destino_id == current_user.persona_id:
        return True
    
    # El usuario tiene acceso si está en la misma área del documento
    if document.area_destino_id == current_user.persona.area_id:
        # Verificar si tiene permiso para ver documentos del área
        if check_permission('ver_documento') or check_permission('Ver documento'):
            return True
    
    # El usuario tiene acceso si tiene permiso para transferir documentos
    if check_permission('transferir_documento') or check_permission('Transferir documento'):
        return True
    
    return False

def document_access_required(f):
    """
    Decorador que verifica si el usuario tiene acceso a un documento.
    
    Returns:
        function: Decorador que aborta con 403 si el usuario no tiene acceso.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        document_id = kwargs.get('id')
        
        from app.models.documento import Documento
        documento = Documento.query.get_or_404(document_id)
        
        # Verificar acceso con la función has_document_access
        if has_document_access(documento):
            return f(*args, **kwargs)
        
        # Si no tiene acceso, redirigir al dashboard con mensaje
        flash('No tienes permiso para acceder a este documento.', 'danger')
        return redirect(url_for('dashboard.index'))
        
    return decorated_function
