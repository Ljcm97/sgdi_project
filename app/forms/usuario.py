from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, EqualTo
from app.models.persona import Persona
from app.models.rol import Rol

class UsuarioForm(FlaskForm):
    """Formulario para crear y editar usuarios"""
    
    username = StringField('Nombre de Usuario', validators=[
        DataRequired(message='Nombre de usuario obligatorio'),
        Length(min=3, max=50, message='El usuario debe tener entre 3 y 50 caracteres')
    ])
    
    password = PasswordField('Contraseña', validators=[
        Optional(),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    
    persona_id = SelectField('Persona', 
                           coerce=int,
                           validators=[DataRequired(message='Persona obligatoria')])
    
    rol_id = SelectField('Rol', 
                        coerce=int,
                        validators=[DataRequired(message='Rol obligatorio')])
    
    activo = BooleanField('Activo', default=True)
    
    submit = SubmitField('Guardar')
    
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        
        # Cargar opciones para los selectores
        self.persona_id.choices = [(p.id, p.nombre_completo) for p in Persona.query.filter_by(activo=True).all()]
        self.rol_id.choices = [(r.id, r.nombre) for r in Rol.query.all()]