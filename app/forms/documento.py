from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateTimeField, RadioField, SubmitField
from wtforms.validators import DataRequired, Optional, Length
from app.models.transportadora import Transportadora
from app.models.tipo_documento import TipoDocumento
from app.models.area import Area
from app.models.persona import Persona
from app.models.estado_documento import EstadoDocumento

class DocumentoForm(FlaskForm):
    """Formulario para registrar documentos"""
    
    fecha_recepcion = DateTimeField('Fecha y Hora de Recepción', 
                                 format='%Y-%m-%d %H:%M',
                                 validators=[DataRequired(message='Fecha y hora obligatorias')])
    
    transportadora_id = SelectField('Transportadora', 
                                  coerce=int,
                                  validators=[DataRequired(message='Transportadora obligatoria')])
    
    numero_guia = StringField('Número de Guía', validators=[
        Optional(),
        Length(max=100, message='Número de guía demasiado largo')
    ])
    
    remitente = StringField('Remitente', validators=[
        DataRequired(message='Remitente obligatorio'),
        Length(max=255, message='Nombre de remitente demasiado largo')
    ])
    
    tipo_documento_id = SelectField('Tipo de Documento', 
                                  coerce=int,
                                  validators=[DataRequired(message='Tipo de documento obligatorio')])
    
    contenido = TextAreaField('Contenido', validators=[
        Optional()
    ])
    
    observaciones = TextAreaField('Observaciones', validators=[
        Optional()
    ])
    
    area_destino_id = SelectField('Área Destino', 
                                coerce=int,
                                validators=[DataRequired(message='Área destino obligatoria')])
    
    persona_destino_id = SelectField('Persona Destino', 
                                   coerce=int,
                                   validators=[DataRequired(message='Persona destino obligatoria')])
    
    tipo = RadioField('Tipo', 
                    choices=[('ENTRADA', 'Entrada'), ('SALIDA', 'Salida')],
                    default='ENTRADA',
                    validators=[DataRequired(message='Tipo obligatorio')])
    
    submit = SubmitField('Registrar Documento')
    
    def __init__(self, *args, **kwargs):
        super(DocumentoForm, self).__init__(*args, **kwargs)
        
        # Cargar opciones para los selectores
        self.transportadora_id.choices = [(t.id, t.nombre) for t in Transportadora.query.all()]
        self.tipo_documento_id.choices = [(t.id, t.nombre) for t in TipoDocumento.query.all()]
        self.area_destino_id.choices = [(a.id, a.nombre) for a in Area.query.all()]
        
        # Inicialmente, no se cargan personas hasta que se seleccione un área
        if self.area_destino_id.data:
            self.persona_destino_id.choices = [
                (p.id, p.nombre_completo) 
                for p in Persona.query.filter_by(area_id=self.area_destino_id.data, activo=True).all()
            ]
        else:
            self.persona_destino_id.choices = []


class TransferirDocumentoForm(FlaskForm):
    """Formulario para transferir documentos"""
    
    area_destino_id = SelectField('Área Destino', 
                                coerce=int,
                                validators=[DataRequired(message='Área destino obligatoria')])
    
    persona_destino_id = SelectField('Persona Destino', 
                                   coerce=int,
                                   validators=[DataRequired(message='Persona destino obligatoria')])
    
    estado_id = SelectField('Estado', 
                          coerce=int,
                          validators=[DataRequired(message='Estado obligatorio')])
    
    observaciones = TextAreaField('Observaciones', validators=[
        Optional()
    ])
    
    submit = SubmitField('Transferir Documento')
    
    def __init__(self, *args, **kwargs):
        super(TransferirDocumentoForm, self).__init__(*args, **kwargs)
        
        # Cargar opciones para los selectores
        self.area_destino_id.choices = [(a.id, a.nombre) for a in Area.query.all()]
        self.estado_id.choices = [(e.id, e.nombre) for e in EstadoDocumento.query.all()]
        
        # Inicialmente, no se cargan personas hasta que se seleccione un área
        if self.area_destino_id.data:
            self.persona_destino_id.choices = [
                (p.id, p.nombre_completo) 
                for p in Persona.query.filter_by(area_id=self.area_destino_id.data, activo=True).all()
            ]
        else:
            self.persona_destino_id.choices = []