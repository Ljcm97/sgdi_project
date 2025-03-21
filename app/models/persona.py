from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Persona(db.Model, CRUDMixin):
    """Modelo para las personas del sistema"""
    
    __tablename__ = 'personas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombres_apellidos = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    telefono = db.Column(db.String(50))
    zona_economica_id = db.Column(db.Integer, db.ForeignKey('zonas_economicas.id'), nullable=False)
    unidad_id = db.Column(db.Integer, db.ForeignKey('unidades.id'), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargos.id'), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    zona_economica = db.relationship('ZonaEconomica', backref=db.backref('personas', lazy=True))
    unidad = db.relationship('Unidad', backref=db.backref('personas', lazy=True))
    area = db.relationship('Area', backref=db.backref('personas', lazy=True))
    cargo = db.relationship('Cargo', backref=db.backref('personas', lazy=True))
    
    # Documentos asignados a esta persona
    documentos_asignados = db.relationship('Documento', 
                                           foreign_keys='Documento.persona_destino_id',
                                           backref='persona_destino', 
                                           lazy=True)
    
    def __repr__(self):
        return f"<Persona {self.nombres_apellidos}>"
    
    @property
    def nombre_completo(self):
        """Devuelve el nombre completo de la persona"""
        return self.nombres_apellidos
    
    @property
    def info_completa(self):
        """Devuelve la información completa de la persona con área y cargo"""
        return f"{self.nombres_apellidos} ({self.area.nombre} - {self.cargo.nombre})"