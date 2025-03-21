from flask import Blueprint, render_template, redirect, url_for, flash, request
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

personas_bp = Blueprint('personas', __name__, url_prefix='/personas')

@personas_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para listar todas las personas"""
    personas = Persona.query.all()
    return render_template('admin/personas/index.html', personas=personas)

@personas_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    """Vista para crear una nueva persona"""
    form = PersonaForm()
    
    if form.validate_on_submit():
        # Crear la persona
        persona = Persona(
            nombres_apellidos=form.nombres_apellidos.data,
            email=form.email.data,
            telefono=form.telefono.data,
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
        # Actualizar la persona
        form.populate_obj(persona)
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
    
    # Cambiar el estado
    persona.activo = not persona.activo
    db.session.commit()
    
    estado = "activada" if persona.activo else "desactivada"
    flash(f'Persona {estado} exitosamente.', 'success')
    return redirect(url_for('personas.index'))

@personas_bp.route('/get-by-area/<int:area_id>')
@login_required
def get_by_area(area_id):
    """API para obtener las personas de un área específica en formato JSON"""
    personas = Persona.query.filter_by(area_id=area_id, activo=True).all()
    personas_json = [{'id': p.id, 'nombre': p.nombre_completo} for p in personas]
    return jsonify(personas_json)