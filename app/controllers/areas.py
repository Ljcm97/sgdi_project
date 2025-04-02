from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.area import Area
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from sqlalchemy import func

# Formulario para áreas con campos adicionales
class AreaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre de área obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])
    descripcion = TextAreaField('Descripción', validators=[
        Length(max=500, message='Descripción demasiado larga')
    ])
    activo = BooleanField('Activo', default=True)

areas_bp = Blueprint('areas', __name__, url_prefix='/areas')

@areas_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las áreas con estadísticas y búsqueda"""
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Obtener parámetro de búsqueda
    search = request.args.get('search', '')
    
    # Crear la consulta base
    query = Area.query
    
    # Aplicar filtro de búsqueda si existe
    if search:
        query = query.filter(Area.nombre.ilike(f'%{search}%'))
    
    # Ordenar por nombre
    query = query.order_by(Area.nombre)
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'areas.index')
    areas = pagination.items
    
    # Obtener estadísticas
    total_areas = Area.query.count()
    areas_activas = Area.query.filter_by(activo=True).count()
    
    # Obtener áreas con más personal
    from app.models.persona import Persona
    areas_con_mas_personal = db.session.query(
        Area.id,
        Area.nombre,
        func.count(Persona.id).label('total_personas')
    ).outerjoin(
        Persona, Persona.area_id == Area.id
    ).group_by(
        Area.id, Area.nombre
    ).order_by(
        func.count(Persona.id).desc()
    ).limit(5).all()
    
    # Nuevo formulario para crear área
    form = AreaForm()
    
    return render_template('admin/areas/index.html', 
                          areas=areas, 
                          pagination=pagination,
                          form=form,
                          search=search,
                          total_areas=total_areas,
                          areas_activas=areas_activas,
                          areas_con_mas_personal=areas_con_mas_personal)

@areas_bp.route('/crear', methods=['POST'])
@login_required
@admin_required
def crear():
    """Vista para crear una nueva área"""
    form = AreaForm()
    
    if form.validate_on_submit():
        # Normalizar el nombre (convertir a mayúsculas)
        nombre_normalizado = form.nombre.data.strip().upper()
        
        # Verificar si ya existe un área con el mismo nombre
        existente = Area.query.filter(func.upper(Area.nombre) == nombre_normalizado).first()
        if existente:
            flash('Ya existe un área con este nombre.', 'danger')
            return redirect(url_for('areas.index'))
        
        # Crear el área
        area = Area(
            nombre=nombre_normalizado,
            descripcion=form.descripcion.data if hasattr(form, 'descripcion') else None,
            activo=form.activo.data if hasattr(form, 'activo') else True
        )
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
            # Normalizar el nombre (convertir a mayúsculas)
            nombre_normalizado = form.nombre.data.strip().upper()
            
            # Verificar si ya existe otra área con el mismo nombre
            existente = Area.query.filter(
                func.upper(Area.nombre) == nombre_normalizado, 
                Area.id != id
            ).first()
            
            if existente:
                flash('Ya existe otra área con este nombre.', 'danger')
                return render_template('admin/areas/editar.html', form=form, area=area)
            
            # Actualizar el área
            area.nombre = nombre_normalizado
            if hasattr(form, 'descripcion'):
                area.descripcion = form.descripcion.data
            if hasattr(form, 'activo'):
                area.activo = form.activo.data
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
    from app.models.persona import Persona
    if Persona.query.filter_by(area_id=area.id).count() > 0:
        flash('No se puede eliminar esta área porque hay personas asociadas a ella.', 'danger')
        return redirect(url_for('areas.index'))
    
    # Verificar si hay documentos asociados a esta área
    if area.documentos_asignados.count() > 0:
        flash('No se puede eliminar esta área porque hay documentos asociados a ella.', 'danger')
        return redirect(url_for('areas.index'))
    
    # Eliminar el área
    db.session.delete(area)
    db.session.commit()
    
    flash('Área eliminada exitosamente.', 'success')
    return redirect(url_for('areas.index'))

@areas_bp.route('/toggle-estado/<int:id>')
@login_required
@admin_required
def toggle_estado(id):
    """Vista para activar/desactivar un área"""
    area = Area.query.get_or_404(id)
    
    # Cambiar el estado
    area.activo = not area.activo
    db.session.commit()
    
    estado = "activada" if area.activo else "desactivada"
    flash(f'Área {estado} exitosamente.', 'success')
    return redirect(url_for('areas.index'))