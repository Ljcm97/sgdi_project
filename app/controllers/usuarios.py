from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from app import db
from app.models.usuario import Usuario
from app.models.persona import Persona
from app.models.rol import Rol
from app.forms.usuario import UsuarioForm
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todos los usuarios"""
    usuarios = Usuario.query.all()
    return render_template('admin/usuarios/index.html', usuarios=usuarios)

@usuarios_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear un nuevo usuario"""
    form = UsuarioForm()
    
    if form.validate_on_submit():
        # Verificar si ya existe un usuario con el mismo username
        existente = Usuario.query.filter_by(username=form.username.data).first()
        if existente:
            flash('Ya existe un usuario con este nombre de usuario.', 'danger')
            return redirect(url_for('usuarios.crear'))
        
        # Verificar si la persona ya tiene un usuario asociado
        persona = Persona.query.get(form.persona_id.data)
        if hasattr(persona, 'usuario') and persona.usuario:
            flash('Esta persona ya tiene un usuario asociado.', 'danger')
            return redirect(url_for('usuarios.crear'))
        
        # Crear el usuario
        if form.password.data:
            usuario = Usuario.crear_usuario(
                username=form.username.data,
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
    
    # Si hay errores de validación, mostrarlos
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
    
    # La contraseña no es obligatoria para editar
    form.password.validators = []
    
    if form.validate_on_submit():
        # Verificar si ya existe otro usuario con el mismo username
        existente = Usuario.query.filter(Usuario.username == form.username.data, Usuario.id != id).first()
        if existente:
            flash('Ya existe otro usuario con este nombre de usuario.', 'danger')
            return redirect(url_for('usuarios.editar', id=id))
        
        # Actualizar los datos básicos del usuario
        usuario.username = form.username.data
        usuario.persona_id = form.persona_id.data
        usuario.rol_id = form.rol_id.data
        usuario.activo = form.activo.data
        
        # Actualizar la contraseña solo si se proporciona una nueva
        if form.password.data:
            usuario.password = usuario.actualizar_password(form.password.data)
        
        db.session.commit()
        
        flash('Usuario actualizado exitosamente.', 'success')
        return redirect(url_for('usuarios.index'))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('admin/usuarios/editar.html', form=form, usuario=usuario)

@usuarios_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar un usuario"""
    usuario = Usuario.query.get_or_404(id)
    
    # No permitir eliminar al propio usuario actual
    if usuario.id == current_user.id:
        flash('No puedes eliminar tu propio usuario.', 'danger')
        return redirect(url_for('usuarios.index'))
    
    # No permitir eliminar al superadministrador del sistema
    if usuario.rol.nombre == 'Superadministrador' and Usuario.query.filter_by(rol_id=usuario.rol_id).count() <= 1:
        flash('No se puede eliminar el único usuario superadministrador del sistema.', 'danger')
        return redirect(url_for('usuarios.index'))
    
    # Eliminar el usuario
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
    
    # No permitir desactivar al propio usuario actual
    if usuario.id == current_user.id:
        flash('No puedes desactivar tu propio usuario.', 'danger')
        return redirect(url_for('usuarios.index'))
    
    # No permitir desactivar al superadministrador del sistema
    if usuario.rol.nombre == 'Superadministrador' and Usuario.query.filter_by(rol_id=usuario.rol_id, activo=True).count() <= 1 and usuario.activo:
        flash('No se puede desactivar el único usuario superadministrador activo del sistema.', 'danger')
        return redirect(url_for('usuarios.index'))
    
    # Cambiar el estado
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
    
    class CambiarPasswordForm(FlaskForm):
        password = PasswordField('Nueva contraseña', validators=[
            DataRequired(message='La nueva contraseña es obligatoria'),
            Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
        ])
        confirm_password = PasswordField('Confirmar contraseña', validators=[
            DataRequired(message='Debe confirmar la contraseña'),
            EqualTo('password', message='Las contraseñas no coinciden')
        ])
        submit = SubmitField('Cambiar Contraseña')
    
    form = CambiarPasswordForm()
    
    if form.validate_on_submit():
        usuario.actualizar_password(form.password.data)
        flash('Contraseña actualizada exitosamente.', 'success')
        return redirect(url_for('usuarios.index'))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('admin/usuarios/cambiar_password.html', form=form, usuario=usuario)