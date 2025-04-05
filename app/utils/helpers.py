import datetime
from flask import flash, current_app, render_template
from app.models.notificacion import Notificacion
from app import db, mail
from flask_mail import Message

def generate_radicado():
    """
    Genera un número de radicado único para los documentos.
    
    Returns:
        str: Número de radicado en formato: AAMMDD-XXXX (Año con 2 dígitos, Mes, Día, Número secuencial)
    """
    from app.models.documento import Documento
    from sqlalchemy import func
    
    # Obtener la fecha actual
    now = datetime.datetime.now()
    date_str = now.strftime("%y%m%d")  # Año con 2 dígitos
    
    # Buscar el último radicado para el día actual
    today_prefix = f"{date_str}-"
    
    # Consultar el último radicado del día
    ultimo_radicado = Documento.query.filter(
        Documento.radicado.like(f"{today_prefix}%")
    ).order_by(
        Documento.radicado.desc()
    ).first()
    
    # Determinar el siguiente número secuencial
    if ultimo_radicado:
        try:
            # Extraer el número después del guion
            ultimo_numero = int(ultimo_radicado.radicado.split('-')[1])
            siguiente_numero = ultimo_numero + 1
        except (ValueError, IndexError):
            # Si hay algún error al parsear, comenzar con 0001
            siguiente_numero = 1
    else:
        # Si no hay radicados para hoy, comenzar con 0001
        siguiente_numero = 1
    
    # Formatear el número secuencial con ceros a la izquierda (4 dígitos)
    num_secuencial = f"{siguiente_numero:04d}"
    
    return f"{date_str}-{num_secuencial}"

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
            recipients=[email],
            charset="utf-8"  # Asegura que la codificación sea UTF-8
        )
        
        # Configurar el contenido del mensaje en texto plano
        msg.body = f"""Para restablecer tu contraseña, visita el siguiente enlace:

{reset_url}

Si no solicitaste el restablecimiento de contraseña, ignora este mensaje.

Este enlace expirará en 24 horas.

Saludos,
SGDI - Sistema de Gestión Documental Interna
Agroindustrial Molino Sonora AP S.A.S
"""
        
        # HTML version del correo
        msg.html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px;">
                    <h2 style="color: #1D2C96;">Restablecer Contraseña - SGDI</h2>
                    <p>Para restablecer tu contraseña, haz clic en el siguiente botón:</p>
                    <p style="text-align: center;">
                        <a href="{reset_url}" style="display: inline-block; background-color: #1D2C96; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Restablecer Contraseña</a>
                    </p>
                    <p>Si el botón no funciona, también puedes copiar y pegar el siguiente enlace en tu navegador:</p>
                    <p style="word-break: break-all;"><a href="{reset_url}">{reset_url}</a></p>
                    <p><small>Si no solicitaste el restablecimiento de contraseña, ignora este mensaje.</small></p>
                    <p><small>Este enlace expirará en 24 horas.</small></p>
                    <hr>
                    <p style="font-size: 12px; color: #666; text-align: center;">
                        SGDI - Sistema de Gestión Documental Interna<br>
                        Agroindustrial Molino Sonora AP S.A.S
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Enviar el correo electrónico
        mail.send(msg)
        
        # Para depuración, imprime que se intentó enviar el correo
        print(f"Intentando enviar correo a: {email}")
        print(f"Enlace de restablecimiento: {reset_url}")
        
        return True
    except Exception as e:
        # En un entorno de producción, registra el error en un archivo de registro
        print(f"Error al enviar correo: {str(e)}")
        
        # Para desarrollo, simplemente imprime el enlace en la consola
        print(f"Enlace de restablecimiento (simulado): {reset_url}")
        
        return False
