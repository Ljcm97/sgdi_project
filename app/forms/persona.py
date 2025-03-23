from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, Length
from app.models.zona_economica import ZonaEconomica
from app.models.unidad import Unidad
from app.models.area import Area
from app.models.cargo import Cargo

class PersonaForm(FlaskForm):
    """Formulario para crear y editar personas"""
    
    nombres_apellidos = StringField('Nombres y Apellidos', validators=[
        DataRequired(message='Nombres y apellidos son obligatorios'),
        Length(max=255, message='Nombres y apellidos demasiado largos')
    ])
    
    email = StringField('Email', validators=[
        Optional(),
        Email(message='Formato de email inválido'),
        Length(max=255, message='Email demasiado largo')
    ])
    
    telefono = StringField('Teléfono', validators=[
        Optional(),
        Length(max=50, message='Número de teléfono demasiado largo')
    ])
    
    zona_economica_id = SelectField('Zona Económica', 
                                    coerce=int,
                                    validators=[DataRequired(message='Zona económica obligatoria')])
    
    unidad_id = SelectField('Nombre de Unidad', 
                            coerce=int,
                            validators=[DataRequired(message='Unidad obligatoria')])
    
    area_id = SelectField('Área', 
                          coerce=int,
                          validators=[DataRequired(message='Área obligatoria')])
    
    cargo_id = SelectField('Cargo', 
                           coerce=int,
                           validators=[DataRequired(message='Cargo obligatorio')])
    
    activo = BooleanField('Activo', default=True)
    
    submit = SubmitField('Guardar')
    
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        
        # Cargar opciones para los selectores sin opciones vacías
        self.zona_economica_id.choices = [(z.id, z.nombre) for z in ZonaEconomica.query.order_by(ZonaEconomica.nombre).all()]
        self.unidad_id.choices = [(u.id, u.nombre) for u in Unidad.query.order_by(Unidad.nombre).all()]
        self.area_id.choices = [(a.id, a.nombre) for a in Area.query.order_by(Area.nombre).all()]
        self.cargo_id.choices = [(c.id, c.nombre) for c in Cargo.query.order_by(Cargo.nombre).all()]
