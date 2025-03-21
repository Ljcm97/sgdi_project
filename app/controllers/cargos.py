from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.cargo import Cargo
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

# Formulario simple para cargos
class CargoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de cargo obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])

cargos_bp = Blueprint('cargos', __name__, url_prefix='/cargos')

@cargos_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todos los cargos"""
    cargos = Cargo.query.all()
    form = CargoForm()
    return render_template('admin/cargos/index.html', cargos=cargos, form=form)

@cargos_bp.route('/crear', methods=['POST'])
@login_required
@admin_required
def crear():
    """Vista para crear un nuevo cargo"""
    form = CargoForm()
    
    if form.validate_on_submit():
        # Verificar si ya existe un cargo con el mismo nombre
        existente = Cargo.query.filter_by(nombre=form.nombre.data).first()
        if existente:
            flash('Ya existe un cargo con este nombre.', 'danger')
            return redirect(url_for('cargos.index'))
        
        # Crear el cargo
        cargo = Cargo(nombre=form.nombre.data)
        db.session.add(cargo)
        db.session.commit()
        
        flash('Cargo creado exitosamente.', 'success')
    else:
        flash_errors(form)
    
    return redirect(url_for('cargos.index'))

@cargos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar un cargo existente"""
    cargo = Cargo.query.get_or_404(id)
    form = CargoForm(obj=cargo)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Verificar si ya existe otro cargo con el mismo nombre
            existente = Cargo.query.filter(Cargo.nombre == form.nombre.data, Cargo.id != id).first()
            if existente:
                flash('Ya existe otro cargo con este nombre.', 'danger')
                return redirect(url_for('cargos.index'))
            
            # Actualizar el cargo
            form.populate_obj(cargo)
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