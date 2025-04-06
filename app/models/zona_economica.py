from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class ZonaEconomica(db.Model, CRUDMixin):
    """Modelo para las zonas económicas de la empresa"""
    
    __tablename__ = 'zonas_economicas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<ZonaEconomica {self.nombre}>"