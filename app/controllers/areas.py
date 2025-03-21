from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.area import Area
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

# Formulario simple para áreas
class AreaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de área obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])

areas_bp = Blueprint('areas', __name__, url_prefix='/areas')

@areas_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las áreas"""
    areas = Area.query.all()
    form = AreaForm()
    return render_template('admin/areas/index.html', areas=areas, form=form)

@areas_bp.route('/crear', methods=['POST'])
@login_required
@admin_required
def crear():
    """Vista para crear una nueva área"""
    form = AreaForm()
    
    if form.validate_on_submit():
        # Verificar si ya existe un área con el mismo nombre
        existente = Area.query.filter_by(nombre=form.nombre.data).first()
        if existente:
            flash('Ya existe un área con este nombre.', 'danger')
            return redirect(url_for('areas.index'))
        
        # Crear el área
        area = Area(nombre=form.nombre.data)
        db.session.add(area)
        db.session.commit()
        
        flash('Área creada exitosamente.', 'success')
    else:
        flash_errors(form)
    
    return redirect(url_for('areas.index'))

@areas_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar un área existente"""
    area = Area.query.get_or_404(id)
    form = AreaForm(obj=area)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Verificar si ya existe otra área con el mismo nombre
            existente = Area.query.filter(Area.nombre == form.nombre.data, Area.id != id).first()
            if existente:
                flash('Ya existe otra área con este nombre.', 'danger')
                return redirect(url_for('areas.index'))
            
            # Actualizar el área
            form.populate_obj(area)
            db.session.commit()
            
            flash('Área actualizada exitosamente.', 'success')
            return redirect(url_for('areas.index'))
        else:
            flash_errors(form)
    
    return render_template('admin/areas/editar.html', form=form, area=area)

@areas_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar un área"""
    area = Area.query.get_or_404(id)
    
    # Verificar si hay personas asociadas a esta área
    if area.personas:
        flash('No se puede eliminar esta área porque hay personas asociadas a ella.', 'danger')
        return redirect(url_for('areas.index'))
    
    # Verificar si hay documentos asociados a esta área
    if area.documentos_asignados:
        flash('No se puede eliminar esta área porque hay documentos asociados a ella.', 'danger')
        return redirect(url_for('areas.index'))
    
    # Eliminar el área
    db.session.delete(area)
    db.session.commit()
    
    flash('Área eliminada exitosamente.', 'success')
    return redirect(url_for('areas.index'))