from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Area(db.Model, CRUDMixin):
    """Modelo para las áreas de la empresa"""
    
    __tablename__ = 'areas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Documentos asignados a esta área
    documentos_asignados = db.relationship('Documento', 
                                          foreign_keys='Documento.area_destino_id',
                                          backref='area_destino', 
                                          lazy=True)
    
    def __repr__(self):
        return f"<Area {self.nombre}>"
    
    @classmethod
    def get_active_areas(cls):
        """Obtener todas las áreas activas"""
        return cls.query.filter_by(activo=True).order_by(cls.nombre).all()