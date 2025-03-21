from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

class Notificacion(db.Model, CRUDMixin):
    """Modelo para las notificaciones del sistema"""
    
    __tablename__ = 'notificaciones'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    documento_id = db.Column(db.Integer, db.ForeignKey('documentos.id'))
    leida = db.Column(db.Boolean, default=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    def marcar_como_leida(self):
        """Marca la notificación como leída"""
        self.leida = True
        return self.save()
    
    def __repr__(self):
        return f"<Notificacion {self.id} para usuario {self.usuario_id}>"