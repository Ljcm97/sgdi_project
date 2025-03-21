from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Unidad(db.Model, CRUDMixin):
    """Modelo para las unidades organizacionales"""
    
    __tablename__ = 'unidades'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Unidad {self.nombre}>"