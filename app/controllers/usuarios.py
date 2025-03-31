from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.usuario import Usuario
from app.models.persona import Persona
from app.models.rol import Rol
from app.forms.usuario import UsuarioForm
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from sqlalchemy import func

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todos los usuarios"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    query = Usuario.query.order_by(Usuario.username)
    pagination = Pagination(query, page, per_page, 'usuarios.index')
    usuarios = pagination.items

    return render_template('admin/usuarios/index.html', 
                           usuarios=usuarios, 
                           pagination=pagination)

@usuarios_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear un nuevo usuario"""
    form = UsuarioForm()
    
    if form.validate_on_submit():
        username_normalizado = form.username.data.strip().lower()

        existente = Usuario.query.filter(func.lower(Usuario.username) == username_normalizado).first()
        if existente:
            flash('Ya existe un usuario con este nombre de usuario.', 'danger')
            return redirect(url_for('usuarios.crear'))

        persona = Persona.query.get(form.persona_id.data)
        if hasattr(persona, 'usuario') and persona.usuario:
            flash('Esta persona ya tiene un usuario asociado.', 'danger')
            return redirect(url_for('usuarios.crear'))

        if form.password.data:
            usuario = Usuario.crear_usuario(
                username=username_normalizado,
                password=form.password.data,
                persona_id=form.persona_id.data,
                rol_id=form.rol_id.data
            )
            usuario.activo = form.activo.data
            db.session.commit()
            
            flash('Usuario creado exitosamente.', 'success')
            return redirect(url_for('usuarios.index'))
        else:
            form.password.errors.append('La contraseña es obligatoria para crear un usuario.')

    if form.errors:
        flash_errors(form)
    
    return render_template('admin/usuarios/crear.html', form=form)

@usuarios_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar un usuario existente"""
    usuario = Usuario.query.get_or_404(id)
    form = UsuarioForm(obj=usuario)

    form.password.validators = []

    if form.validate_on_submit():
        username_normalizado = form.username.data.strip().lower()

        existente = Usuario.query.filter(
            func.lower(Usuario.username) == username_normalizado, 
            Usuario.id != id
        ).first()
        if existente:
            flash('Ya existe otro usuario con este nombre de usuario.', 'danger')
            return redirect(url_for('usuarios.editar', id=id))

        usuario.username = username_normalizado
        usuario.persona_id = form.persona_id.data
        usuario.rol_id = form.rol_id.data
        usuario.activo = form.activo.data

        if form.password.data:
            usuario.actualizar_password(form.password.data)

        db.session.commit()
        
        flash('Usuario actualizado exitosamente.', 'success')
        return redirect(url_for('usuarios.index'))

    if form.errors:
        flash_errors(form)
    
    return render_template('admin/usuarios/editar.html', form=form, usuario=usuario)

@usuarios_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar un usuario"""
    usuario = Usuario.query.get_or_404(id)

    if usuario.id == current_user.id:
        flash('No puedes eliminar tu propio usuario.', 'danger')
        return redirect(url_for('usuarios.index'))

    if usuario.rol.nombre == 'Superadministrador' and Usuario.query.filter_by(rol_id=usuario.rol_id).count() <= 1:
        flash('No se puede eliminar el único usuario superadministrador del sistema.', 'danger')
        return redirect(url_for('usuarios.index'))

    db.session.delete(usuario)
    db.session.commit()

    flash('Usuario eliminado exitosamente.', 'success')
    return redirect(url_for('usuarios.index'))

@usuarios_bp.route('/toggle-estado/<int:id>')
@login_required
@admin_required
def toggle_estado(id):
    """Vista para activar/desactivar un usuario"""
    usuario = Usuario.query.get_or_404(id)

    if usuario.id == current_user.id:
        flash('No puedes desactivar tu propio usuario.', 'danger')
        return redirect(url_for('usuarios.index'))

    if usuario.rol.nombre == 'Superadministrador' and Usuario.query.filter_by(rol_id=usuario.rol_id, activo=True).count() <= 1 and usuario.activo:
        flash('No se puede desactivar el único usuario superadministrador activo del sistema.', 'danger')
        return redirect(url_for('usuarios.index'))

    usuario.activo = not usuario.activo
    db.session.commit()

    estado = "activado" if usuario.activo else "desactivado"
    flash(f'Usuario {estado} exitosamente.', 'success')
    return redirect(url_for('usuarios.index'))

@usuarios_bp.route('/cambiar-password/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def cambiar_password(id):
    """Vista para cambiar la contraseña de un usuario"""
    usuario = Usuario.query.get_or_404(id)

    from wtforms import PasswordField, SubmitField
    from wtforms.validators import DataRequired, Length, EqualTo
    from flask_wtf import FlaskForm
    from app.utils.password_validators import validate_password_complexity
    
    class CambiarPasswordForm(FlaskForm):
        password = PasswordField('Nueva contraseña', validators=[ 
            DataRequired(message='La nueva contraseña es obligatoria'),
            Length(min=8, message='La contraseña debe tener al menos 8 caracteres'),
            validate_password_complexity
        ])
        confirm_password = PasswordField('Confirmar contraseña', validators=[ 
            DataRequired(message='Debe confirmar la contraseña'),
            EqualTo('password', message='Las contraseñas no coinciden')
        ])
        submit = SubmitField('Cambiar Contraseña')

    form = CambiarPasswordForm()

    if form.validate_on_submit():
        try:
            usuario.actualizar_password(form.password.data)
            flash('Contraseña actualizada exitosamente.', 'success')
            return redirect(url_for('usuarios.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    if form.errors:
        flash_errors(form)

    return render_template('admin/usuarios/cambiar_password.html', form=form, usuario=usuario)
