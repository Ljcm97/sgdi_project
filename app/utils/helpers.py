import datetime
import random
import string
from flask import flash, current_app
from app.models.notificacion import Notificacion
from app import db

def generate_radicado():
    """
    Genera un número de radicado único para los documentos.
    
    Returns:
        str: Número de radicado en formato: AAAAMMDD-XXXX (Año, Mes, Día, Número aleatorio)
    """
    # Obtener la fecha actual
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    
    # Generar un número aleatorio de 4 dígitos
    random_num = ''.join(random.choices(string.digits, k=4))
    
    return f"{date_str}-{random_num}"

def crear_notificacion(usuario_id, titulo, mensaje, documento_id=None):
    """
    Crea una nueva notificación para un usuario.
    
    Args:
        usuario_id (int): ID del usuario destinatario.
        titulo (str): Título de la notificación.
        mensaje (str): Mensaje detallado de la notificación.
        documento_id (int, optional): ID del documento relacionado.
        
    Returns:
        Notificacion: La notificación creada.
    """
    notificacion = Notificacion(
        usuario_id=usuario_id,
        titulo=titulo,
        mensaje=mensaje,
        documento_id=documento_id
    )
    db.session.add(notificacion)
    db.session.commit()
    
    return notificacion

def flash_errors(form):
    """
    Muestra todos los errores de validación de un formulario como mensajes flash.
    
    Args:
        form: El formulario con errores de validación.
    """
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text}: {error}", "danger")

def format_date(date):
    """
    Formatea una fecha para su visualización.
    
    Args:
        date (datetime): La fecha a formatear.
        
    Returns:
        str: La fecha formateada como dd/mm/aaaa.
    """
    if date:
        return date.strftime("%d/%m/%Y")
    return ""

def format_datetime(dt):
    """
    Formatea una fecha y hora para su visualización.
    
    Args:
        dt (datetime): La fecha y hora a formatear.
        
    Returns:
        str: La fecha y hora formateada como dd/mm/aaaa HH:MM.
    """
    if dt:
        return dt.strftime("%d/%m/%Y %H:%M")
    return ""

def get_personas_por_area(area_id):
    """
    Obtiene todas las personas que pertenecen a un área.
    
    Args:
        area_id (int): ID del área.
        
    Returns:
        list: Lista de personas en el área.
    """
    from app.models.persona import Persona
    return Persona.query.filter_by(area_id=area_id, activo=True).all()