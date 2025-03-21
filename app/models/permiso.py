from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Permiso(db.Model, CRUDMixin):
    """Modelo para los permisos del sistema"""
    
    __tablename__ = 'permisos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Permiso {self.nombre}>"