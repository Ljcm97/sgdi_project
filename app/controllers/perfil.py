from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms.auth import ChangePasswordForm
from app.utils.helpers import flash_errors

perfil_bp = Blueprint('perfil', __name__, url_prefix='/perfil')

@perfil_bp.route('/')
@login_required
def index():
    """Vista para mostrar el perfil del usuario actual"""
    return render_template('perfil/index.html')

@perfil_bp.route('/cambiar-password', methods=['GET', 'POST'])
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
            return redirect(url_for('perfil.index'))
        else:
            flash('La contraseña actual es incorrecta.', 'danger')
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('perfil/cambiar_password.html', form=form)