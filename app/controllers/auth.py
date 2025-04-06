from flask import Blueprint, render_template, flash, redirect, url_for, request, session, current_app as app
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models.usuario import Usuario
from app.forms.auth import LoginForm, ChangePasswordForm, ResetPasswordRequestForm, ResetPasswordForm
from app.utils.helpers import flash_errors, enviar_email_reset_password
import secrets
from sqlalchemy import func

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Vista para el inicio de sesión"""
    
    # Si el usuario ya está autenticado, redirigir al dashboard
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        # Modificación: Buscar usuario insensible a mayúsculas/minúsculas
        usuario = Usuario.query.filter(
            func.lower(Usuario.username) == func.lower(form.username.data)
        ).first()
        
        if usuario and usuario.verificar_password(form.password.data):
            # Verificar si el usuario está activo
            if not usuario.activo:
                flash('Tu cuenta está desactivada. Contacta al administrador.', 'danger')
                return render_template('login.html', form=form)
            
            # Autenticar al usuario y configurar "recordar sesión"
            remember = form.remember.data if 'remember' in form else False
            login_user(usuario, remember=remember)
            
            # Registrar acceso
            usuario.registrar_acceso()
            
            # Redirigir a la página solicitada o al dashboard
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard.index'))
        else:
            flash('Usuario o contraseña incorrectos. Intenta de nuevo.', 'danger')
    
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """Vista para cerrar sesión"""
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('auth.login'))


@auth_bp.route('/cambiar-password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    """Vista para cambiar la contraseña del usuario actual"""
    
    form = ChangePasswordForm()
    
    if form.validate_on_submit():
        # Verificar la contraseña actual
        if current_user.verificar_password(form.current_password.data):
            try:
                # Actualizar la contraseña
                current_user.actualizar_password(form.new_password.data)
                flash('Tu contraseña ha sido actualizada.', 'success')
                return redirect(url_for('dashboard.index'))
            except ValueError as e:
                flash(str(e), 'danger')
        else:
            flash('La contraseña actual es incorrecta.', 'danger')
    
    return render_template('perfil/cambiar_password.html', form=form)


@auth_bp.route('/olvido-password', methods=['GET', 'POST'])
def olvido_password():
    """Vista para solicitar restablecimiento de contraseña"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    form = ResetPasswordRequestForm()
    
    if form.validate_on_submit():
        # Verifica si el email existe (se une con persona para buscar por email)
        usuario = Usuario.query.join(Usuario.persona).filter(
            Usuario.persona.has(email=form.email.data)
        ).first()
        
        if usuario:
            # Generar token seguro
            token = secrets.token_urlsafe(32)
            
            # Guardar token en la sesión con expiración de 24 horas
            session[f'reset_token_{token}'] = usuario.id
            session.permanent = True
            
            # Construir URL para restablecer contraseña
            reset_url = url_for('auth.reset_password', token=token, _external=True)
            
            # Intentar enviar el correo
            enviado = enviar_email_reset_password(usuario.persona.email, reset_url)
            
            # Registrar intentos para depuración
            print(f"Intento de envío de correo a {usuario.persona.email}. Resultado: {enviado}")
            print(f"Token generado: {token}")
            print(f"URL de restablecimiento: {reset_url}")
            
            # Siempre mostrar mensaje de éxito por seguridad
            flash('Se ha enviado un correo con instrucciones para restablecer tu contraseña (si la dirección existe en nuestro sistema).', 'info')
            return redirect(url_for('auth.login'))
        else:
            # Por seguridad, no indicamos si el email existe o no
            flash('Se ha enviado un correo con instrucciones para restablecer tu contraseña (si la dirección existe en nuestro sistema).', 'info')
            return redirect(url_for('auth.login'))
    
    return render_template('auth/olvido_password.html', form=form)


@auth_bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Vista para restablecer contraseña con token"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    # Verificar token en la sesión
    key = f'reset_token_{token}'
    user_id = session.get(key)
    
    if not user_id:
        print(f"Token inválido o expirado: {token}")
        print(f"Llaves de sesión disponibles: {list(session.keys())}")
        flash('El enlace para restablecer la contraseña es inválido o ha expirado.', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.get(user_id)
    if not usuario:
        flash('Usuario no encontrado.', 'danger')
        return redirect(url_for('auth.login'))
    
    form = ResetPasswordForm()
    
    if form.validate_on_submit():
        try:
            # Actualizar contraseña
            usuario.actualizar_password(form.password.data)
            
            # Eliminar token de la sesión
            session.pop(key, None)
            
            flash('Tu contraseña ha sido restablecida. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))
        except ValueError as e:
            flash(str(e), 'danger')
    
    return render_template('auth/reset_password.html', form=form)
