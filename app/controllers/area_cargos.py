from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required
from app import db
from app.models.area import Area
from app.models.cargo import Cargo
from app.models.persona import Persona
from app.utils.decorators import admin_required
from app.utils.helpers import flash_errors
from sqlalchemy import func

# Crear un formulario para asignar cargos a áreas
from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class AsignacionCargoAreaForm(FlaskForm):
    """Formulario para asignar cargos a áreas"""
    area_id = SelectField('Área', coerce=int, validators=[DataRequired(message='Área obligatoria')])
    cargos = SelectMultipleField('Cargos', coerce=int, validators=[DataRequired(message='Seleccione al menos un cargo')])
    submit = SubmitField('Guardar Asignación')

    def __init__(self, *args, **kwargs):
        super(AsignacionCargoAreaForm, self).__init__(*args, **kwargs)
        
        # Cargar áreas disponibles
        self.area_id.choices = [(a.id, a.nombre) for a in Area.query.order_by(Area.nombre).all()]
        
        # Cargar todos los cargos
        self.cargos.choices = [(c.id, c.nombre) for c in Cargo.query.order_by(Cargo.nombre).all()]


# Blueprint para gestionar cargos por área
area_cargos_bp = Blueprint('area_cargos', __name__, url_prefix='/area-cargos')

@area_cargos_bp.route('/')
@login_required
@admin_required
def index():
    """Vista para gestionar las asignaciones de cargos a áreas"""
    form = AsignacionCargoAreaForm()
    
    # Inicializar form.cargos.data como una lista vacía en lugar de None
    if form.cargos.data is None:
        form.cargos.data = []
    
    # Obtener todas las áreas para mostrar en la tabla
    areas = Area.query.order_by(Area.nombre).all()
    
    # Obtener personas agrupadas por área para extraer los cargos
    areas_con_cargos = []
    
    for area in areas:
        # Obtener personas con esta área
        personas = Persona.query.filter_by(area_id=area.id).all()
        
        # Extraer cargos únicos
        cargos_ids = set(p.cargo_id for p in personas)
        cargos = Cargo.query.filter(Cargo.id.in_(cargos_ids)).order_by(Cargo.nombre).all()
        
        # Añadir a la lista
        areas_con_cargos.append({
            'area': area,
            'cargos': cargos
        })
    
    return render_template('admin/area_cargos/index.html', 
                          form=form, 
                          areas_con_cargos=areas_con_cargos)

@area_cargos_bp.route('/get-cargos-area/<int:area_id>')
@login_required
@admin_required
def get_cargos_area(area_id):
    """API para obtener los cargos de un área específica"""
    # Obtener personas con esta área
    personas = Persona.query.filter_by(area_id=area_id).all()
    
    # Extraer cargos únicos
    cargos_ids = set(p.cargo_id for p in personas)
    
    return jsonify(list(cargos_ids))

@area_cargos_bp.route('/asignar', methods=['POST'])
@login_required
@admin_required
def asignar():
    """Vista para asignar cargos a un área"""
    form = AsignacionCargoAreaForm()
    
    if form.validate_on_submit():
        area_id = form.area_id.data
        cargo_ids = form.cargos.data
        
        try:
            # Verificar si el área existe
            area = Area.query.get_or_404(area_id)
            
            # Verificar que los cargos existan
            cargos = Cargo.query.filter(Cargo.id.in_(cargo_ids)).all()
            if len(cargos) != len(cargo_ids):
                flash('Algunos cargos seleccionados no existen.', 'danger')
                return redirect(url_for('area_cargos.index'))
            
            # Crear una persona "modelo" para cada cargo que no exista ya para esa área
            # Esto establecerá la relación entre el área y los cargos
            
            # Primero, obtener los cargos que ya están asignados
            personas_existentes = Persona.query.filter_by(area_id=area_id).all()
            cargos_existentes = [p.cargo_id for p in personas_existentes]
            
            # Agregar aprendiz SENA si no existe ya
            aprendiz_sena = Cargo.query.filter_by(nombre='APRENDIZ SENA').first()
            if aprendiz_sena and aprendiz_sena.id not in cargo_ids and aprendiz_sena.id not in cargos_existentes:
                cargo_ids.append(aprendiz_sena.id)
            
            # Crear personas modelo para los nuevos cargos
            for cargo_id in cargo_ids:
                if cargo_id not in cargos_existentes:
                    # Buscar datos por defecto necesarios
                    zona_economica_id = 1  # ID de la zona económica principal
                    unidad_id = 1  # ID de la unidad principal
                    
                    cargo = Cargo.query.get(cargo_id)
                    
                    # Crear una persona modelo (inactiva para que no interfiera pero establezca la relación)
                    persona_modelo = Persona(
                        nombres_apellidos=f"Modelo - {area.nombre} - {cargo.nombre}",
                        zona_economica_id=zona_economica_id,
                        unidad_id=unidad_id,
                        area_id=area_id,
                        cargo_id=cargo_id,
                        activo=False  # Inactivo para que no aparezca en selecciones
                    )
                    db.session.add(persona_modelo)
            
            db.session.commit()
            flash(f'Cargos asignados correctamente al área {area.nombre}.', 'success')
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al asignar cargos: {str(e)}', 'danger')
        
    else:
        flash_errors(form)
    
    return redirect(url_for('area_cargos.index'))

@area_cargos_bp.route('/quitar-cargo/<int:area_id>/<int:cargo_id>')
@login_required
@admin_required
def quitar_cargo(area_id, cargo_id):
    """Vista para quitar un cargo de un área"""
    # Verificar si hay personas activas con este cargo en esta área
    personas_activas = Persona.query.filter_by(area_id=area_id, cargo_id=cargo_id, activo=True).all()
    
    if personas_activas:
        flash('No se puede quitar este cargo porque hay personas activas asignadas a él en esta área.', 'danger')
        return redirect(url_for('area_cargos.index'))
    
    # Eliminar las personas modelo (inactivas) que establecen la relación
    personas_modelo = Persona.query.filter_by(area_id=area_id, cargo_id=cargo_id, activo=False).all()
    
    for persona in personas_modelo:
        db.session.delete(persona)
    
    db.session.commit()
    
    area = Area.query.get(area_id)
    cargo = Cargo.query.get(cargo_id)
    flash(f'Cargo "{cargo.nombre}" eliminado del área "{area.nombre}".', 'success')
    
    return redirect(url_for('area_cargos.index'))