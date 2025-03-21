from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.rol import Rol
from app.models.permiso import Permiso
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from wtforms import StringField, TextAreaField, SelectMultipleField, widgets, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

# Widget personalizado para selección múltiple con checkboxes
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# Formulario para roles
class RolForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de rol obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])
    descripcion = TextAreaField('Descripción', validators=[
        Length(max=500, message='Descripción demasiado larga')
    ])
    permisos = MultiCheckboxField('Permisos', coerce=int)
    submit = SubmitField('Guardar')
    
    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        self.permisos.choices = [(p.id, p.nombre) for p in Permiso.query.all()]

roles_bp = Blueprint('roles', __name__, url_prefix='/roles')

@roles_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todos los roles"""
    roles = Rol.query.all()
    return render_template('admin/roles/index.html', roles=roles)

@roles_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear un nuevo rol"""
    form = RolForm()
    
    if form.validate_on_submit():
        # Verificar si ya existe un rol con el mismo nombre
        existente = Rol.query.filter_by(nombre=form.nombre.data).first()
        if existente:
            flash('Ya existe un rol con este nombre.', 'danger')
            return redirect(url_for('roles.crear'))
        
        # Crear el rol
        rol = Rol(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data
        )
        db.session.add(rol)
        db.session.commit()
        
        # Asignar permisos
        for permiso_id in form.permisos.data:
            permiso = Permiso.query.get(permiso_id)
            if permiso:
                rol.permisos.append(permiso)
        
        db.session.commit()
        
        flash('Rol creado exitosamente.', 'success')
        return redirect(url_for('roles.index'))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('admin/roles/crear.html', form=form)

@roles_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar un rol existente"""
    rol = Rol.query.get_or_404(id)
    
    # No permitir editar el rol de Superadministrador
    if rol.nombre == 'Superadministrador':
        flash('No se puede editar el rol de Superadministrador.', 'danger')
        return redirect(url_for('roles.index'))
    
    # Prepopular los permisos seleccionados
    permiso_ids = [p.id for p in rol.permisos]
    form = RolForm(obj=rol)
    form.permisos.data = permiso_ids
    
    if form.validate_on_submit():
        # Verificar si ya existe otro rol con el mismo nombre
        existente = Rol.query.filter(Rol.nombre == form.nombre.data, Rol.id != id).first()
        if existente:
            flash('Ya existe otro rol con este nombre.', 'danger')
            return redirect(url_for('roles.editar', id=id))
        
        # Actualizar el rol
        rol.nombre = form.nombre.data
        rol.descripcion = form.descripcion.data
        
        # Actualizar permisos
        rol.permisos = []
        for permiso_id in form.permisos.data:
            permiso = Permiso.query.get(permiso_id)
            if permiso:
                rol.permisos.append(permiso)
        
        db.session.commit()
        
        flash('Rol actualizado exitosamente.', 'success')
        return redirect(url_for('roles.index'))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('admin/roles/editar.html', form=form, rol=rol)

@roles_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar un rol"""
    rol = Rol.query.get_or_404(id)
    
    # No permitir eliminar roles esenciales
    if rol.nombre in ['Superadministrador', 'Recepción', 'Usuario']:
        flash(f'No se puede eliminar el rol esencial de {rol.nombre}.', 'danger')
        return redirect(url_for('roles.index'))
    
    # Verificar si hay usuarios asociados a este rol
    if rol.usuarios:
        flash('No se puede eliminar este rol porque hay usuarios asociados a él.', 'danger')
        return redirect(url_for('roles.index'))
    
    # Eliminar el rol
    db.session.delete(rol)
    db.session.commit()
    
    flash('Rol eliminado exitosamente.', 'success')
    return redirect(url_for('roles.index'))