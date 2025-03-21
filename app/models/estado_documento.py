from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class EstadoDocumento(db.Model, CRUDMixin):
    """Modelo para los estados de documento"""
    
    __tablename__ = 'estados_documento'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    color = db.Column(db.String(7), nullable=False)  # Formato HEX: #RRGGBB
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Documentos en este estado
    documentos = db.relationship('Documento', 
                                foreign_keys='Documento.estado_actual_id',
                                backref='estado_actual', 
                                lazy=True)
    
    # Movimientos asociados a este estado
    movimientos = db.relationship('Movimiento', backref='estado_documento', lazy=True)
    
    def __repr__(self):
        return f"<EstadoDocumento {self.nombre}>"