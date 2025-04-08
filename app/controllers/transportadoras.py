from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.transportadora import Transportadora
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func

# Formulario para transportadoras
class TransportadoraForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de transportadora obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])
    descripcion = TextAreaField('Descripción', validators=[
        Length(max=500, message='Descripción demasiado larga')
    ])
    activo = BooleanField('Activo', default=True)
    submit = SubmitField('Guardar')

transportadoras_bp = Blueprint('transportadoras', __name__, url_prefix='/transportadoras')

@transportadoras_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las transportadoras"""
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('search', '')
    
    # Crear la consulta base
    query = Transportadora.query
    
    # Aplicar filtro de búsqueda si existe
    if search:
        query = query.filter(Transportadora.nombre.ilike(f'%{search}%'))
    
    # Ordenar por nombre
    query = query.order_by(Transportadora.nombre)
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'transportadoras.index')
    transportadoras = pagination.items
    
    form = TransportadoraForm()
    return render_template('admin/transportadoras/index.html', 
                          transportadoras=transportadoras, 
                          pagination=pagination,
                          form=form,
                          search=search)

@transportadoras_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear una nueva transportadora"""
    form = TransportadoraForm()
    
    if form.validate_on_submit():
        # Normalizar el nombre (convertir a mayúsculas para comparación)
        nombre_normalizado = form.nombre.data.strip().upper()
        
        # Verificar si ya existe una transportadora con el mismo nombre (insensible a mayúsculas/minúsculas)
        existente = Transportadora.query.filter(func.upper(Transportadora.nombre) == nombre_normalizado).first()
        if existente:
            flash('Ya existe una transportadora con este nombre.', 'danger')
            return redirect(url_for('transportadoras.index'))
        
        # Crear la transportadora
        transportadora = Transportadora(
            nombre=nombre_normalizado,
            descripcion=form.descripcion.data,
            activo=form.activo.data
        )
        db.session.add(transportadora)
        db.session.commit()
        
        flash('Transportadora creada exitosamente.', 'success')
        return redirect(url_for('transportadoras.index'))
    else:
        flash_errors(form)
    
    return render_template('admin/transportadoras/crear.html', form=form)

@transportadoras_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar una transportadora existente"""
    transportadora = Transportadora.query.get_or_404(id)
    form = TransportadoraForm(obj=transportadora)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Normalizar el nombre (convertir a mayúsculas para comparación)
            nombre_normalizado = form.nombre.data.strip().upper()
            
            # Verificar si ya existe otra transportadora con el mismo nombre
            existente = Transportadora.query.filter(
                func.upper(Transportadora.nombre) == nombre_normalizado, 
                Transportadora.id != id
            ).first()
            if existente:
                flash('Ya existe otra transportadora con este nombre.', 'danger')
                return redirect(url_for('transportadoras.index'))
            
            # Actualizar la transportadora
            transportadora.nombre = nombre_normalizado
            transportadora.descripcion = form.descripcion.data
            transportadora.activo = form.activo.data
            db.session.commit()
            
            flash('Transportadora actualizada exitosamente.', 'success')
            return redirect(url_for('transportadoras.index'))
        else:
            flash_errors(form)
    
    return render_template('admin/transportadoras/editar.html', form=form, transportadora=transportadora)

@transportadoras_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar una transportadora"""
    transportadora = Transportadora.query.get_or_404(id)
    
    # Verificar si hay documentos asociados a esta transportadora
    if transportadora.documentos:
        flash('No se puede eliminar esta transportadora porque hay documentos asociados a ella.', 'danger')
        return redirect(url_for('transportadoras.index'))
    
    # Eliminar la transportadora
    db.session.delete(transportadora)
    db.session.commit()
    
    flash('Transportadora eliminada exitosamente.', 'success')
    return redirect(url_for('transportadoras.index'))

@transportadoras_bp.route('/toggle-estado/<int:id>')
@login_required
@admin_required
def toggle_estado(id):
    """Vista para activar/desactivar una transportadora"""
    transportadora = Transportadora.query.get_or_404(id)
    
    # Cambiar el estado
    transportadora.activo = not transportadora.activo
    db.session.commit()
    
    estado = "activada" if transportadora.activo else "desactivada"
    flash(f'Transportadora {estado} exitosamente.', 'success')
    return redirect(url_for('transportadoras.index'))
