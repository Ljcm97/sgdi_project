from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Movimiento(db.Model, CRUDMixin):
    """Modelo para los movimientos de documentos"""
    
    __tablename__ = 'movimientos'
    
    id = db.Column(db.Integer, primary_key=True)
    documento_id = db.Column(db.Integer, db.ForeignKey('documentos.id'), nullable=False)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    usuario_origen_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    area_origen_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    persona_origen_id = db.Column(db.Integer, db.ForeignKey('personas.id'), nullable=False)
    area_destino_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    persona_destino_id = db.Column(db.Integer, db.ForeignKey('personas.id'), nullable=False)
    estado_documento_id = db.Column(db.Integer, db.ForeignKey('estados_documento.id'), nullable=False)
    observaciones = db.Column(db.Text)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    usuario_origen = db.relationship('Usuario', backref=db.backref('movimientos_originados', lazy=True))
    area_origen = db.relationship('Area', foreign_keys=[area_origen_id])
    persona_origen = db.relationship('Persona', foreign_keys=[persona_origen_id])
    area_destino = db.relationship('Area', foreign_keys=[area_destino_id])
    persona_destino = db.relationship('Persona', foreign_keys=[persona_destino_id])
    
    def __repr__(self):
        return f"<Movimiento {self.id} del documento {self.documento_id}>"