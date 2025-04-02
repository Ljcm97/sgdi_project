from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class AreaForm(FlaskForm):
    """Formulario para crear y editar áreas"""
    
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Nombre del área obligatorio'),
        Length(max=100, message='Nombre demasiado largo')
    ])
    
    descripcion = TextAreaField('Descripción', validators=[
        Length(max=500, message='Descripción demasiado larga')
    ])
    
    activo = BooleanField('Activo', default=True)
    
    submit = SubmitField('Guardar')