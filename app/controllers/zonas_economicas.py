from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.zona_economica import ZonaEconomica
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func

# Formulario simple para zonas económicas
class ZonaEconomicaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de zona económica obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])

zonas_economicas_bp = Blueprint('zonas_economicas', __name__, url_prefix='/zonas-economicas')

@zonas_economicas_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las zonas económicas"""
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Crear la consulta base
    query = ZonaEconomica.query.order_by(ZonaEconomica.nombre)
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'zonas_economicas.index')
    zonas = pagination.items
    
    form = ZonaEconomicaForm()
    return render_template('admin/zonas_economicas/index.html', 
                          zonas=zonas, 
                          pagination=pagination,
                          form=form)

@zonas_economicas_bp.route('/crear', methods=['POST'])
@login_required
@admin_required
def crear():
    """Vista para crear una nueva zona económica"""
    form = ZonaEconomicaForm()
    
    if form.validate_on_submit():
        # Normalizar el nombre (convertir a mayúsculas para comparación)
        nombre_normalizado = form.nombre.data.strip().upper()
        
        # Verificar si ya existe una zona con el mismo nombre
        existente = ZonaEconomica.query.filter(func.upper(ZonaEconomica.nombre) == nombre_normalizado).first()
        if existente:
            flash('Ya existe una zona económica con este nombre.', 'danger')
            return redirect(url_for('zonas_economicas.index'))
        
        # Crear la zona económica
        zona = ZonaEconomica(nombre=nombre_normalizado)
        db.session.add(zona)
        db.session.commit()
        
        flash('Zona económica creada exitosamente.', 'success')
    else:
        flash_errors(form)
    
    return redirect(url_for('zonas_economicas.index'))

@zonas_economicas_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar una zona económica existente"""
    zona = ZonaEconomica.query.get_or_404(id)
    form = ZonaEconomicaForm(obj=zona)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Normalizar el nombre (convertir a mayúsculas para comparación)
            nombre_normalizado = form.nombre.data.strip().upper()
            
            # Verificar si ya existe otra zona con el mismo nombre
            existente = ZonaEconomica.query.filter(func.upper(ZonaEconomica.nombre) == nombre_normalizado, ZonaEconomica.id != id).first()
            if existente:
                flash('Ya existe otra zona económica con este nombre.', 'danger')
                return redirect(url_for('zonas_economicas.index'))
            
            # Actualizar la zona económica
            zona.nombre = nombre_normalizado
            db.session.commit()
            
            flash('Zona económica actualizada exitosamente.', 'success')
            return redirect(url_for('zonas_economicas.index'))
        else:
            flash_errors(form)
    
    return render_template('admin/zonas_economicas/editar.html', form=form, zona=zona)

@zonas_economicas_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar una zona económica"""
    zona = ZonaEconomica.query.get_or_404(id)
    
    # Verificar si hay personas asociadas a esta zona económica
    if zona.personas:
        flash('No se puede eliminar esta zona económica porque hay personas asociadas a ella.', 'danger')
        return redirect(url_for('zonas_economicas.index'))
    
    # Eliminar la zona económica
    db.session.delete(zona)
    db.session.commit()
    
    flash('Zona económica eliminada exitosamente.', 'success')
    return redirect(url_for('zonas_economicas.index'))
