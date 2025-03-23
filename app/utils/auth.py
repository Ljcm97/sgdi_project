from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def check_permission(permission):
    """
    Verifica si el usuario actual tiene el permiso especificado.
    Maneja diferentes formatos de permisos (snake_case, capitalizado, etc.)
    
    Args:
        permission (str): El nombre del permiso que se va a verificar.
        
    Returns:
        bool: True si el usuario tiene el permiso, False en caso contrario.
    """
    if not current_user.is_authenticated:
        return False  # Usuario no autenticado no tiene permisos
    
    # Verificar si el usuario tiene un rol asignado
    if not hasattr(current_user, 'rol') or not current_user.rol:
        return False
    
    # Superadministrador tiene todos los permisos
    if current_user.rol.nombre == 'Superadministrador':
        return True
    
    # Normalizar el permiso recibido para diferentes formatos de comparación
    permission_lower = permission.lower()
    permission_snake = permission_lower.replace(' ', '_')
    permission_words = permission_snake.split('_')
    permission_title = ' '.join(word.capitalize() for word in permission_words)
    permission_title_first = permission_words[0].capitalize() + ' ' + ' '.join(permission_words[1:])
    
    # Verificar si el usuario tiene el permiso específico comparando con todos los formatos posibles
    for permiso in current_user.rol.permisos:
        permiso_nombre = permiso.nombre.lower()
        
        # Comparar en diferentes formatos
        if (permission_lower == permiso_nombre or
            permission_snake == permiso_nombre.replace(' ', '_') or
            permission_title.lower() == permiso_nombre or
            permission_title_first.lower() == permiso_nombre):
            return True
            
    return False

def permission_required(permission):
    """
    Decorador que verifica si el usuario tiene un permiso específico.
    
    Args:
        permission (str): El nombre del permiso requerido.
        
    Returns:
        function: Decorador que redirecciona si el usuario no tiene el permiso.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not check_permission(permission):
                flash('No tienes permiso para acceder a esta función.', 'danger')
                return redirect(url_for('dashboard.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def get_user_permissions():
    """
    Obtiene una lista de todos los permisos que tiene el usuario actual.
    
    Returns:
        list: Lista de nombres de permisos.
    """
    if not current_user.is_authenticated:
        return []
    
    # Verificar si el usuario tiene un rol asignado
    if not hasattr(current_user, 'rol') or not current_user.rol:
        return []

    # Superadministrador tiene todos los permisos
    if current_user.rol.nombre == 'Superadministrador':
        from app.models.permiso import Permiso
        return [p.nombre for p in Permiso.query.all()]
    
    # Permisos del rol asignado
    return [p.nombre for p in current_user.rol.permisos]
