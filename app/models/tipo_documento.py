from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class TipoDocumento(db.Model, CRUDMixin):
    """Modelo para los tipos de documento"""
    
    __tablename__ = 'tipos_documento'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Documentos asociados a este tipo
    documentos = db.relationship('Documento', backref='tipo_documento', lazy=True)
    
    def __repr__(self):
        return f"<TipoDocumento {self.nombre}>"