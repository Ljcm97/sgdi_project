from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.cargo import Cargo
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func


class CargoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de cargo obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])
    descripcion = TextAreaField('Descripción', validators=[
        Length(max=500, message='Descripción demasiado larga')
    ])
    activo = BooleanField('Activo', default=True)

cargos_bp = Blueprint('cargos', __name__, url_prefix='/cargos')

@cargos_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todos los cargos"""
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('search', '')
    
    # Crear la consulta base
    query = Cargo.query

    # Aplicar filtro de búsqueda si existe
    if search:
        query = query.filter(Cargo.nombre.ilike(f'%{search}%'))
    
    # Ordenar por nombre
    query = query.order_by(Cargo.nombre)
    
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'cargos.index')
    cargos = pagination.items
    
    form = CargoForm()
    return render_template('admin/cargos/index.html', 
                          cargos=cargos, 
                          pagination=pagination,
                          form=form,
                          search=search)

@cargos_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear un nuevo cargo"""
    form = CargoForm()
    
    if form.validate_on_submit():
        # Normalizar el nombre (convertir a mayúsculas)
        nombre_normalizado = form.nombre.data.strip().upper()
        
        # Verificar si ya existe un cargo con el mismo nombre
        existente = Cargo.query.filter(func.upper(Cargo.nombre) == nombre_normalizado).first()
        if existente:
            flash('Ya existe un cargo con este nombre.', 'danger')
            return redirect(url_for('cargos.index'))
        
        # Crear el cargo
        cargo = Cargo(
            nombre=nombre_normalizado,
            descripcion=form.descripcion.data,
            activo=form.activo.data
        )
        db.session.add(cargo)
        db.session.commit()
        
        flash('Cargo creado exitosamente.', 'success')
        return redirect(url_for('cargos.index'))
    else:
        flash_errors(form)
    
    return render_template('admin/cargos/crear.html', form=form)

@cargos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar un cargo existente"""
    cargo = Cargo.query.get_or_404(id)
    form = CargoForm(obj=cargo)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Normalizar el nombre (convertir a mayúsculas)
            nombre_normalizado = form.nombre.data.strip().upper()
            
            # Verificar si ya existe otro cargo con el mismo nombre
            existente = Cargo.query.filter(func.upper(Cargo.nombre) == nombre_normalizado, Cargo.id != id).first()
            if existente:
                flash('Ya existe otro cargo con este nombre.', 'danger')
                return redirect(url_for('cargos.index'))
            
            # Actualizar el cargo
            cargo.nombre = nombre_normalizado
            cargo.descripcion = form.descripcion.data
            cargo.activo = form.activo.data
            db.session.commit()
            
            flash('Cargo actualizado exitosamente.', 'success')
            return redirect(url_for('cargos.index'))
        else:
            flash_errors(form)
    
    return render_template('admin/cargos/editar.html', form=form, cargo=cargo)

@cargos_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar un cargo"""
    cargo = Cargo.query.get_or_404(id)
    
    # Verificar si hay personas asociadas a este cargo
    if cargo.personas:
        flash('No se puede eliminar este cargo porque hay personas asociadas a él.', 'danger')
        return redirect(url_for('cargos.index'))
    
    # Eliminar el cargo
    db.session.delete(cargo)
    db.session.commit()
    
    flash('Cargo eliminado exitosamente.', 'success')
    return redirect(url_for('cargos.index'))

@cargos_bp.route('/toggle-estado/<int:id>')
@login_required
@admin_required
def toggle_estado(id):
    """Vista para activar/desactivar un cargo"""
    cargo = Cargo.query.get_or_404(id)
    
    # Cambiar el estado
    cargo.activo = not cargo.activo
    db.session.commit()
    
    estado = "activado" if cargo.activo else "desactivado"
    flash(f'Cargo {estado} exitosamente.', 'success')
    return redirect(url_for('cargos.index'))