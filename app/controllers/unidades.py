from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.unidad import Unidad
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func

# Formulario para unidades
class UnidadForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de unidad obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])
    descripcion = TextAreaField('Descripción', validators=[
        Length(max=500, message='Descripción demasiado larga')
    ])
    activo = BooleanField('Activo', default=True)

unidades_bp = Blueprint('unidades', __name__, url_prefix='/unidades')

@unidades_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las unidades"""
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('search', '')
    
    # Crear la consulta base
    query = Unidad.query
    
    # Aplicar filtro de búsqueda si existe
    if search:
        query = query.filter(Unidad.nombre.ilike(f'%{search}%'))
    
    # Ordenar por nombre
    query = query.order_by(Unidad.nombre)
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'unidades.index')
    unidades = pagination.items
    
    form = UnidadForm()
    return render_template('admin/unidades/index.html', 
                          unidades=unidades, 
                          pagination=pagination,
                          form=form,
                          search=search)

@unidades_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear una nueva unidad"""
    form = UnidadForm()
    
    if form.validate_on_submit():
        # Normalizar el nombre (convertir a mayúsculas para comparación)
        nombre_normalizado = form.nombre.data.strip().upper()
        
        # Verificar si ya existe una unidad con el mismo nombre
        existente = Unidad.query.filter(func.upper(Unidad.nombre) == nombre_normalizado).first()
        if existente:
            flash('Ya existe una unidad con este nombre.', 'danger')
            return redirect(url_for('unidades.index'))
        
        # Crear la unidad con los nuevos campos
        unidad = Unidad(
            nombre=nombre_normalizado,
            descripcion=form.descripcion.data,
            activo=form.activo.data
        )
        db.session.add(unidad)
        db.session.commit()
        
        flash('Unidad creada exitosamente.', 'success')
        return redirect(url_for('unidades.index'))
    else:
        flash_errors(form)
    
    return render_template('admin/unidades/crear.html', form=form)

@unidades_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar una unidad existente"""
    unidad = Unidad.query.get_or_404(id)
    form = UnidadForm(obj=unidad)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Normalizar el nombre (convertir a mayúsculas para comparación)
            nombre_normalizado = form.nombre.data.strip().upper()
            
            # Verificar si ya existe otra unidad con el mismo nombre
            existente = Unidad.query.filter(func.upper(Unidad.nombre) == nombre_normalizado, Unidad.id != id).first()
            if existente:
                flash('Ya existe otra unidad con este nombre.', 'danger')
                return redirect(url_for('unidades.index'))
            
            # Actualizar la unidad
            unidad.nombre = nombre_normalizado
            unidad.descripcion = form.descripcion.data
            unidad.activo = form.activo.data
            db.session.commit()
            
            flash('Unidad actualizada exitosamente.', 'success')
            return redirect(url_for('unidades.index'))
        else:
            flash_errors(form)
    
    return render_template('admin/unidades/editar.html', form=form, unidad=unidad)

@unidades_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar una unidad"""
    unidad = Unidad.query.get_or_404(id)
    
    # Verificar si hay personas asociadas a esta unidad
    if unidad.personas:
        flash('No se puede eliminar esta unidad porque hay personas asociadas a ella.', 'danger')
        return redirect(url_for('unidades.index'))
    
    # Eliminar la unidad
    db.session.delete(unidad)
    db.session.commit()
    
    flash('Unidad eliminada exitosamente.', 'success')
    return redirect(url_for('unidades.index'))

@unidades_bp.route('/toggle-estado/<int:id>')
@login_required
@admin_required
def toggle_estado(id):
    """Vista para activar/desactivar una unidad"""
    unidad = Unidad.query.get_or_404(id)
    
    # Cambiar el estado
    unidad.activo = not unidad.activo
    db.session.commit()
    
    estado = "activada" if unidad.activo else "desactivada"
    flash(f'Unidad {estado} exitosamente.', 'success')
    return redirect(url_for('unidades.index'))
