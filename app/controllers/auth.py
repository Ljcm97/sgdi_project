from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models.usuario import Usuario
from app.forms.auth import LoginForm, ChangePasswordForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Vista para el inicio de sesión"""
    
    # Si el usuario ya está autenticado, redirigir al dashboard
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        # Intentar autenticar al usuario
        usuario = Usuario.query.filter_by(username=form.username.data).first()
        
        if usuario and usuario.verificar_password(form.password.data):
            # Verificar si el usuario está activo
            if not usuario.activo:
                flash('Tu cuenta está desactivada. Contacta al administrador.', 'danger')
                return render_template('login.html', form=form)
            
            # Autenticar al usuario
            login_user(usuario, remember=form.remember.data)
            
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
            # Actualizar la contraseña
            current_user.actualizar_password(form.new_password.data)
            flash('Tu contraseña ha sido actualizada.', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('La contraseña actual es incorrecta.', 'danger')
    
    return render_template('perfil/cambiar_password.html', form=form)