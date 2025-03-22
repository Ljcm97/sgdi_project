from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.tipo_documento import TipoDocumento
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func

# Formulario simple para tipos de documento
class TipoDocumentoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de tipo de documento obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])

tipos_documento_bp = Blueprint('tipos_documento', __name__, url_prefix='/tipos-documento')

@tipos_documento_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todos los tipos de documento"""
    # Obtener tipos ordenados alfabéticamente por nombre
    tipos = TipoDocumento.query.order_by(TipoDocumento.nombre).all()
    form = TipoDocumentoForm()
    return render_template('admin/tipos_documento/index.html', tipos=tipos, form=form)

@tipos_documento_bp.route('/crear', methods=['POST'])
@login_required
@admin_required
def crear():
    """Vista para crear un nuevo tipo de documento"""
    form = TipoDocumentoForm()
    
    if form.validate_on_submit():
        # Normalizar el nombre (convertir a mayúsculas para comparación)
        nombre_normalizado = form.nombre.data.strip().title()
        
        # Verificar si ya existe un tipo con el mismo nombre
        existente = TipoDocumento.query.filter(func.upper(TipoDocumento.nombre) == nombre_normalizado.upper()).first()
        if existente:
            flash('Ya existe un tipo de documento con este nombre.', 'danger')
            return redirect(url_for('tipos_documento.index'))
        
        # Crear el tipo de documento
        tipo = TipoDocumento(nombre=nombre_normalizado)
        db.session.add(tipo)
        db.session.commit()
        
        flash('Tipo de documento creado exitosamente.', 'success')
    else:
        flash_errors(form)
    
    return redirect(url_for('tipos_documento.index'))

@tipos_documento_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar un tipo de documento existente"""
    tipo = TipoDocumento.query.get_or_404(id)
    form = TipoDocumentoForm(obj=tipo)
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # Normalizar el nombre (convertir a mayúsculas para comparación)
            nombre_normalizado = form.nombre.data.strip().title()
            
            # Verificar si ya existe otro tipo con el mismo nombre
            existente = TipoDocumento.query.filter(
                func.upper(TipoDocumento.nombre) == nombre_normalizado.upper(), 
                TipoDocumento.id != id
            ).first()
            if existente:
                flash('Ya existe otro tipo de documento con este nombre.', 'danger')
                return redirect(url_for('tipos_documento.index'))
            
            # Actualizar el tipo de documento
            tipo.nombre = nombre_normalizado
            db.session.commit()
            
            flash('Tipo de documento actualizado exitosamente.', 'success')
            return redirect(url_for('tipos_documento.index'))
        else:
            flash_errors(form)
    
    return render_template('admin/tipos_documento/editar.html', form=form, tipo=tipo)

@tipos_documento_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar un tipo de documento"""
    tipo = TipoDocumento.query.get_or_404(id)
    
    # Verificar si hay documentos asociados a este tipo
    if tipo.documentos:
        flash('No se puede eliminar este tipo de documento porque hay documentos asociados a él.', 'danger')
        return redirect(url_for('tipos_documento.index'))
    
    # Eliminar el tipo de documento
    db.session.delete(tipo)
    db.session.commit()
    
    flash('Tipo de documento eliminado exitosamente.', 'success')
    return redirect(url_for('tipos_documento.index'))