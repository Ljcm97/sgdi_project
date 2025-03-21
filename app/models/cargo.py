from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Cargo(db.Model, CRUDMixin):
    """Modelo para los cargos en la empresa"""
    
    __tablename__ = 'cargos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Cargo {self.nombre}>"