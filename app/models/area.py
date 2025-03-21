from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Area(db.Model, CRUDMixin):
    """Modelo para las áreas de la empresa"""
    
    __tablename__ = 'areas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Documentos asignados a esta área
    documentos_asignados = db.relationship('Documento', 
                                          foreign_keys='Documento.area_destino_id',
                                          backref='area_destino', 
                                          lazy=True)
    
    def __repr__(self):
        return f"<Area {self.nombre}>"