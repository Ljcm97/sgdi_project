from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.cargo import Cargo
from app.models.area import Area
from app.models.persona import Persona  # Añade esta línea también
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from wtforms import StringField, TextAreaField, BooleanField, SelectMultipleField
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
    areas = SelectMultipleField('Áreas', coerce=int, validators=[
        DataRequired(message='Seleccione al menos un área')
    ])
    activo = BooleanField('Activo', default=True)
    
    def __init__(self, *args, **kwargs):
        super(CargoForm, self).__init__(*args, **kwargs)
        # Cargar las áreas disponibles
        self.areas.choices = [(a.id, a.nombre) for a in Area.query.order_by(Area.nombre).all()]

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
    area_id = request.args.get('area_id', 0, type=int)
    
    # Crear la consulta base
    query = Cargo.query

    # Aplicar filtro de búsqueda si existe
    if search:
        query = query.filter(Cargo.nombre.ilike(f'%{search}%'))

    if area_id > 0:
        query = query.filter(Cargo.area_id == area_id)
    
    # Ordenar por nombre
    query = query.order_by(Cargo.nombre)
    

    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'cargos.index')
    cargos = pagination.items
    
    # Obtener información de áreas para cada cargo
    cargos_con_areas = []
    for cargo in cargos:
        areas_del_cargo = db.session.query(Area.nombre).join(
            Persona, Persona.area_id == Area.id
        ).filter(
            Persona.cargo_id == cargo.id
        ).distinct().all()
        
        areas_nombres = [area[0] for area in areas_del_cargo]
        cargos_con_areas.append({
            'cargo': cargo,
            'areas': ', '.join(areas_nombres) if areas_nombres else 'No asignado'
        })
    
    form = CargoForm()
    return render_template('admin/cargos/index.html', 
                          cargos_con_areas=cargos_con_areas, 
                          pagination=pagination,
                          area_id=area_id,
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
        
        # Asignar el cargo a las áreas seleccionadas
        zona_economica_id = 1  # ID de la zona económica principal
        unidad_id = 1  # ID de la unidad principal
        
        for area_id in form.areas.data:
            area = Area.query.get(area_id)
            if area:
                # Crear una persona modelo (inactiva) que establece la relación entre área y cargo
                persona_modelo = Persona(
                    nombres_apellidos=f"Modelo - {area.nombre} - {cargo.nombre}",
                    zona_economica_id=zona_economica_id,
                    unidad_id=unidad_id,
                    area_id=area_id,
                    cargo_id=cargo.id,
                    activo=False  # Inactivo para que no aparezca en selecciones
                )
                db.session.add(persona_modelo)
        
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
    
    # Obtener las áreas actuales del cargo
    areas_actuales = db.session.query(Area.id).join(
        Persona, Persona.area_id == Area.id
    ).filter(
        Persona.cargo_id == cargo.id
    ).distinct().all()
    
    areas_ids = [area[0] for area in areas_actuales]
    
    form = CargoForm(obj=cargo)
    # Solo establecer los datos de áreas en GET
    if request.method == 'GET':
        form.areas.data = areas_ids
    
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
        
        # Actualizar las áreas asociadas
        # 1. Obtener áreas seleccionadas y actuales
        nuevas_areas = set(form.areas.data)
        actuales_areas = set(areas_ids)
        
        # 2. Áreas a eliminar (están en actuales pero no en nuevas)
        areas_a_eliminar = actuales_areas - nuevas_areas
        
        # 3. Áreas a añadir (están en nuevas pero no en actuales)
        areas_a_agregar = nuevas_areas - actuales_areas
        
        # 4. Eliminar relaciones existentes
        for area_id in areas_a_eliminar:
            personas_modelo = Persona.query.filter_by(
                area_id=area_id,
                cargo_id=cargo.id,
                activo=False  # Solo las personas modelo inactivas
            ).all()
            
            for persona in personas_modelo:
                db.session.delete(persona)
        
        # 5. Crear nuevas relaciones
        zona_economica_id = 1  # ID de la zona económica principal
        unidad_id = 1  # ID de la unidad principal
        
        for area_id in areas_a_agregar:
            area = Area.query.get(area_id)
            if area:
                persona_modelo = Persona(
                    nombres_apellidos=f"Modelo - {area.nombre} - {cargo.nombre}",
                    zona_economica_id=zona_economica_id,
                    unidad_id=unidad_id,
                    area_id=area_id,
                    cargo_id=cargo.id,
                    activo=False
                )
                db.session.add(persona_modelo)
        
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