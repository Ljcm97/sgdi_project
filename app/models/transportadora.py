from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Transportadora(db.Model, CRUDMixin):
    """Modelo para las empresas transportadoras"""
    
    __tablename__ = 'transportadoras'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Documentos asociados a esta transportadora
    documentos = db.relationship('Documento', backref='transportadora', lazy=True)
    
    def __repr__(self):
        return f"<Transportadora {self.nombre}>"