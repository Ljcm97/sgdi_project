from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.unidad import Unidad
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func

# Formulario simple para unidades
class UnidadForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de unidad obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])

unidades_bp = Blueprint('unidades', __name__, url_prefix='/unidades')

@unidades_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las unidades"""
    # Obtener unidades ordenadas alfabéticamente por nombre
    unidades = Unidad.query.order_by(Unidad.nombre).all()
    form = UnidadForm()
    return render_template('admin/unidades/index.html', unidades=unidades, form=form)

@unidades_bp.route('/crear', methods=['POST'])
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
        
        # Crear la unidad
        unidad = Unidad(nombre=nombre_normalizado)
        db.session.add(unidad)
        db.session.commit()
        
        flash('Unidad creada exitosamente.', 'success')
    else:
        flash_errors(form)
    
    return redirect(url_for('unidades.index'))

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