import datetime
import random
import string
from flask import flash, current_app, render_template
from app.models.notificacion import Notificacion
from app import db, mail
from flask_mail import Message

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
    # Usar datetime.now() para asegurar que tiene la hora correcta
    notificacion = Notificacion(
        usuario_id=usuario_id,
        titulo=titulo,
        mensaje=mensaje,
        documento_id=documento_id,
        creado_en=datetime.datetime.now()  # Asegurar que se usa la hora actual
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

def enviar_email_reset_password(email, reset_url):
    """
    Envía un correo electrónico con el enlace para restablecer la contraseña.
    
    Args:
        email (str): Dirección de correo electrónico del destinatario.
        reset_url (str): URL para restablecer la contraseña.
    """
    try:
        # Crear el mensaje
        msg = Message(
            'SGDI - Restablecer Contraseña',
            recipients=[email]
        )
        
        # Configurar el contenido del mensaje
        msg.body = f"""Para restablecer tu contraseña, visita el siguiente enlace:

{reset_url}

Si no solicitaste el restablecimiento de contraseña, ignora este mensaje.

Este enlace expirará en 24 horas.

Saludos,
SGDI - Sistema de Gestión Documental Interna
Agroindustrial Molino Sonora AP S.A.S
"""
        
        # Enviar el correo electrónico
        mail.send(msg)
        
        return True
    except Exception as e:
        # En un entorno de producción, registra el error en un archivo de registro
        print(f"Error al enviar correo: {str(e)}")
        
        # Para desarrollo, simplemente imprime el enlace en la consola
        print(f"Enlace de restablecimiento (simulado): {reset_url}")
        
        return False
