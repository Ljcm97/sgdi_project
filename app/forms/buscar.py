from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, RadioField, SubmitField
from wtforms.validators import Optional
from app.models.transportadora import Transportadora
from app.models.tipo_documento import TipoDocumento
from app.models.estado_documento import EstadoDocumento

class BuscarDocumentoForm(FlaskForm):
    """Formulario para buscar documentos"""
    
    radicado = StringField('Radicado', validators=[Optional()])
    
    fecha_desde = DateField('Fecha Desde', format='%Y-%m-%d', validators=[Optional()])
    
    fecha_hasta = DateField('Fecha Hasta', format='%Y-%m-%d', validators=[Optional()])
    
    transportadora_id = SelectField('Transportadora', 
                                  validators=[Optional()],
                                  default=0)
    
    tipo_documento_id = SelectField('Tipo de Documento', 
                                  validators=[Optional()],
                                  default=0)
    
    estado_id = SelectField('Estado', 
                          validators=[Optional()],
                          default=0)
    
    tipo = RadioField('Tipo', 
                    choices=[('', 'Todos'), ('ENTRADA', 'Entrada'), ('SALIDA', 'Salida')],
                    default='',
                    validators=[Optional()])
    
    remitente = StringField('Remitente/Destinatario', validators=[Optional()])
    
    buscar = SubmitField('Buscar')
    
    limpiar = SubmitField('Limpiar')
    
    def __init__(self, *args, **kwargs):
        super(BuscarDocumentoForm, self).__init__(*args, **kwargs)
        
        # Cargar opciones para los selectores
        self.transportadora_id.choices = [(0, 'Todas')] + [
            (t.id, t.nombre) for t in Transportadora.query.order_by(Transportadora.nombre).all()
        ]
        
        self.tipo_documento_id.choices = [(0, 'Todos')] + [
            (t.id, t.nombre) for t in TipoDocumento.query.order_by(TipoDocumento.nombre).all()
        ]
        
        self.estado_id.choices = [(0, 'Todos')] + [
            (e.id, e.nombre) for e in EstadoDocumento.query.order_by(EstadoDocumento.nombre).all()
        ]
