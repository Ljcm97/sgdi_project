from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.persona import Persona
from app.models.zona_economica import ZonaEconomica
from app.models.unidad import Unidad
from app.models.area import Area
from app.models.cargo import Cargo
from app.forms.persona import PersonaForm
from app.utils.auth import permission_required
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from app.utils.pagination import Pagination
from sqlalchemy import func

personas_bp = Blueprint('personas', __name__, url_prefix='/personas')

@personas_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las personas con paginación y filtros"""
    # Obtener parámetros de búsqueda y filtros
    search = request.args.get('search', '')
    area_id = request.args.get('area_id', 0, type=int)
    
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Crear la consulta base
    query = Persona.query
    
    # Aplicar filtros si existen
    if search:
        # Usar el operador LIKE con comodines para la consulta, pero mantener el valor original
        search_pattern = f"%{search}%"
        query = query.filter(Persona.nombres_apellidos.like(search_pattern) | 
                            Persona.email.like(search_pattern))
    
    if area_id > 0:
        query = query.filter(Persona.area_id == area_id)
    
    # Ordenar resultados
    query = query.order_by(Persona.nombres_apellidos)
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'personas.index')
    personas = pagination.items
    
    # Obtener todas las áreas para el filtro
    areas = Area.query.order_by(Area.nombre).all()
    
    return render_template('admin/personas/index.html', 
                          personas=personas, 
                          pagination=pagination,
                          search=search,  # Pasamos el valor original sin los comodines
                          area_id=area_id,
                          areas=areas)

@personas_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear una nueva persona"""
    form = PersonaForm()
    
    if form.validate_on_submit():
        # Normalizar correo electrónico
        email = form.email.data.strip().lower() if form.email.data else None
        
        # Normalizar nombre (trim y convertir a mayúsculas)
        nombres_apellidos = form.nombres_apellidos.data.strip().upper()
        
        # Verificar si el correo ya existe (si se proporciona)
        if email:
            existente_email = Persona.query.filter(func.lower(Persona.email) == email).first()
            if existente_email:
                flash(f'Ya existe una persona con el correo {email}.', 'danger')
                return render_template('admin/personas/crear.html', form=form)
        
        # Verificar si el nombre y apellido ya existe (convertido a mayúsculas)
        existente_nombre = Persona.query.filter(
            func.upper(Persona.nombres_apellidos) == nombres_apellidos
        ).first()
        if existente_nombre:
            flash(f'Ya existe una persona con el nombre {nombres_apellidos}.', 'danger')
            return render_template('admin/personas/crear.html', form=form)
        
        # Crear la persona
        persona = Persona(
            nombres_apellidos=nombres_apellidos,  # Ya está en mayúsculas
            email=email,
            telefono=form.telefono.data.strip() if form.telefono.data else None,
            zona_economica_id=form.zona_economica_id.data,
            unidad_id=form.unidad_id.data,
            area_id=form.area_id.data,
            cargo_id=form.cargo_id.data,
            activo=form.activo.data
        )
        db.session.add(persona)
        db.session.commit()
        
        flash('Persona creada exitosamente.', 'success')
        return redirect(url_for('personas.index'))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('admin/personas/crear.html', form=form)


@personas_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    """Vista para editar una persona existente"""
    persona = Persona.query.get_or_404(id)
    form = PersonaForm(obj=persona)
    
    if form.validate_on_submit():
        # Normalizar correo electrónico
        email = form.email.data.strip().lower() if form.email.data else None
        
        # Normalizar nombre (trim y convertir a mayúsculas)
        nombres_apellidos = form.nombres_apellidos.data.strip().upper()
        
        # Verificar si el correo ya existe (si se proporciona)
        if email:
            existente_email = Persona.query.filter(
                func.lower(Persona.email) == email,
                Persona.id != id
            ).first()
            if existente_email:
                flash(f'Ya existe otra persona con el correo {email}.', 'danger')
                return render_template('admin/personas/editar.html', form=form, persona=persona)
        
        # Verificar si el nombre y apellido ya existe (comparación en mayúsculas)
        existente_nombre = Persona.query.filter(
            func.upper(Persona.nombres_apellidos) == nombres_apellidos,
            Persona.id != id
        ).first()
        if existente_nombre:
            flash(f'Ya existe otra persona con el nombre {nombres_apellidos}.', 'danger')
            return render_template('admin/personas/editar.html', form=form, persona=persona)
        
        # Actualizar la persona
        persona.nombres_apellidos = nombres_apellidos  # Ya está en mayúsculas
        persona.email = email
        persona.telefono = form.telefono.data.strip() if form.telefono.data else None
        persona.zona_economica_id = form.zona_economica_id.data
        persona.unidad_id = form.unidad_id.data
        persona.area_id = form.area_id.data
        persona.cargo_id = form.cargo_id.data
        persona.activo = form.activo.data
        db.session.commit()
        
        flash('Persona actualizada exitosamente.', 'success')
        return redirect(url_for('personas.index'))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('admin/personas/editar.html', form=form, persona=persona)


@personas_bp.route('/eliminar/<int:id>')
@login_required
@admin_required
def eliminar(id):
    """Vista para eliminar una persona"""
    persona = Persona.query.get_or_404(id)
    
    # Verificar si la persona tiene usuario asociado
    if hasattr(persona, 'usuario') and persona.usuario:
        flash('No se puede eliminar esta persona porque tiene un usuario asociado.', 'danger')
        return redirect(url_for('personas.index'))
    
    # Verificar si la persona tiene documentos asignados
    if persona.documentos_asignados:
        flash('No se puede eliminar esta persona porque tiene documentos asignados.', 'danger')
        return redirect(url_for('personas.index'))
    
    # Eliminar la persona
    db.session.delete(persona)
    db.session.commit()
    
    flash('Persona eliminada exitosamente.', 'success')
    return redirect(url_for('personas.index'))

@personas_bp.route('/toggle-estado/<int:id>')
@login_required
@admin_required
def toggle_estado(id):
    """Vista para activar/desactivar una persona"""
    persona = Persona.query.get_or_404(id)
    
    # Guardar el estado anterior para el mensaje
    estado_anterior = "activa" if persona.activo else "inactiva"
    
    # Cambiar el estado
    persona.activo = not persona.activo
    db.session.commit()
    
    # Determinar el nuevo estado para el mensaje
    estado_actual = "desactivada" if estado_anterior == "activa" else "activada"
    
    flash(f'Persona {estado_actual} exitosamente.', 'success')
    return redirect(url_for('personas.index'))

@personas_bp.route('/get-by-area/<int:area_id>')
@login_required
def get_by_area(area_id):
    """API para obtener las personas de un área específica en formato JSON"""
    personas = Persona.query.filter_by(area_id=area_id, activo=True).all()
    personas_json = [{'id': p.id, 'nombre': p.nombre_completo} for p in personas]
    return jsonify(personas_json)

@personas_bp.route('/get_cargos_por_area/<int:area_id>')
@login_required
def get_cargos_por_area(area_id):
    """API para obtener los cargos asociados a un área específica, incluyendo el cargo APRENDIZ SENA"""
    # Buscar el área para verificar si existe
    area = Area.query.get_or_404(area_id)
    
    # Obtener personas con el área seleccionada
    personas_area = Persona.query.filter_by(area_id=area_id).all()
    
    # Extraer los cargos asociados a estas personas
    cargos_ids = [p.cargo_id for p in personas_area]
    
    # Obtener cargos únicos para esta área
    cargos = Cargo.query.filter(Cargo.id.in_(cargos_ids)).all()
    
    # Añadir el cargo "APRENDIZ SENA" si no está ya incluido
    aprendiz_sena = Cargo.query.filter_by(nombre='APRENDIZ SENA').first()
    if aprendiz_sena and aprendiz_sena.id not in cargos_ids:
        cargos.append(aprendiz_sena)
    
    # Ordenar alfabéticamente
    cargos = sorted(cargos, key=lambda c: c.nombre)
    
    # Crear lista JSON
    cargos_json = [{'id': c.id, 'nombre': c.nombre} for c in cargos]
    
    return jsonify(cargos_json)