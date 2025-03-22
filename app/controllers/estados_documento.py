from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.estado_documento import EstadoDocumento
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func

# Formulario para estados de documento
class EstadoDocumentoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de estado obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])
    descripcion = TextAreaField('Descripción', validators=[
        Length(max=500, message='Descripción demasiado larga')
    ])
    color = StringField('Color (formato HEX)', validators=[
        DataRequired(message='Color obligatorio'),
        Length(min=7, max=7, message='El color debe tener formato #RRGGBB')
    ])

estados_documento_bp = Blueprint('estados_documento', __name__, url_prefix='/estados-documento')

@estados_documento_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todos los estados de documento"""
    # Obtener estados ordenados alfabéticamente por nombre
    estados = EstadoDocumento.query.order_by(EstadoDocumento.nombre).all()
    form = EstadoDocumentoForm()
    return render_template('admin/estados_documento/index.html', estados=estados, form=form)

@estados_documento_bp.route('/crear', methods=['POST'])
@login_required
@admin_required
def crear():
    """Vista para crear un nuevo estado de documento"""
    form = EstadoDocumentoForm()
    
    if form.validate_on_submit():
        # Normalizar el nombre (convertir a mayúsculas)
        nombre_normalizado = form.nombre.data.strip().title()
        
        # Verificar si ya existe un estado con el mismo nombre
        existente = EstadoDocumento.query.filter(func.upper(EstadoDocumento.nombre) == nombre_normalizado.upper()).first()
        if existente:
            flash('Ya existe un estado de documento con este nombre.', 'danger')
            return redirect(url_for('estados_documento.index'))
        
        # Crear el estado de documento
        estado = EstadoDocumento(
            nombre=nombre_normalizado,
            descripcion=form.descripcion.data,
            color=form.color.data
        )
        db.session.add(estado)
        db.session.commit()
        
        flash('Estado de documento creado exitosamente.', 'success')
    else:
        flash_errors(form)
    
    return redirect(url_for('estados_documento.index'))

@estados_documento_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar un estado de documento existente"""
    estado = EstadoDocumento.query.get_or_404(id)
    form = EstadoDocumentoForm(obj=estado)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Normalizar el nombre (convertir a mayúsculas)
            nombre_normalizado = form.nombre.data.strip().title()
            
            # Verificar si ya existe otro estado con el mismo nombre
            existente = EstadoDocumento.query.filter(
                func.upper(EstadoDocumento.nombre) == nombre_normalizado.upper(), 
                EstadoDocumento.id != id
            ).first()
            if existente:
                flash('Ya existe otro estado de documento con este nombre.', 'danger')
                return redirect(url_for('estados_documento.index'))
            
            # Actualizar el estado de documento
            estado.nombre = nombre_normalizado
            estado.descripcion = form.descripcion.data
            estado.color = form.color.data
            db.session.commit()
            
            flash('Estado de documento actualizado exitosamente.', 'success')
            return redirect(url_for('estados_documento.index'))
        else:
            flash_errors(form)
    
    return render_template('admin/estados_documento/editar.html', form=form, estado=estado)

@estados_documento_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar un estado de documento"""
    estado = EstadoDocumento.query.get_or_404(id)
    
    # Verificar si hay documentos asociados a este estado
    if estado.documentos:
        flash('No se puede eliminar este estado de documento porque hay documentos asociados a él.', 'danger')
        return redirect(url_for('estados_documento.index'))
    
    # Verificar si hay movimientos asociados a este estado
    if estado.movimientos:
        flash('No se puede eliminar este estado de documento porque hay movimientos asociados a él.', 'danger')
        return redirect(url_for('estados_documento.index'))
    
    # Eliminar el estado de documento
    db.session.delete(estado)
    db.session.commit()
    
    flash('Estado de documento eliminado exitosamente.', 'success')
    return redirect(url_for('estados_documento.index'))