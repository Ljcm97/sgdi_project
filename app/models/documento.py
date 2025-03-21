from datetime import datetime
from app import db
from app.utils.db import CRUDMixin
from app.utils.helpers import generate_radicado

class Documento(db.Model, CRUDMixin):
    """Modelo para los documentos del sistema"""
    
    __tablename__ = 'documentos'
    
    id = db.Column(db.Integer, primary_key=True)
    radicado = db.Column(db.String(50), unique=True, nullable=False)
    fecha_recepcion = db.Column(db.DateTime, nullable=False)
    transportadora_id = db.Column(db.Integer, db.ForeignKey('transportadoras.id'), nullable=False)
    numero_guia = db.Column(db.String(100))
    remitente = db.Column(db.String(255), nullable=False)
    tipo_documento_id = db.Column(db.Integer, db.ForeignKey('tipos_documento.id'), nullable=False)
    contenido = db.Column(db.Text)
    observaciones = db.Column(db.Text)
    area_destino_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    persona_destino_id = db.Column(db.Integer, db.ForeignKey('personas.id'), nullable=False)
    estado_actual_id = db.Column(db.Integer, db.ForeignKey('estados_documento.id'), nullable=False)
    tipo = db.Column(db.Enum('ENTRADA', 'SALIDA'), nullable=False)
    registrado_por_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    registrado_por = db.relationship('Usuario', backref=db.backref('documentos_registrados', lazy=True))
    
    # Movimientos del documento
    movimientos = db.relationship('Movimiento', backref='documento', lazy=True, 
                                cascade='all, delete-orphan', order_by='Movimiento.fecha_hora')
    
    # Notificaciones asociadas al documento
    notificaciones = db.relationship('Notificacion', backref='documento', lazy=True,
                                   cascade='all, delete-orphan')
    
    @classmethod
    def crear_documento(cls, **kwargs):
        """Crea un nuevo documento generando el radicado automáticamente"""
        if 'radicado' not in kwargs:
            kwargs['radicado'] = generate_radicado()
        
        return cls.create(**kwargs)
    
    def transferir(self, usuario_origen, area_destino, persona_destino, estado_nuevo, observaciones=None):
        """Transfiere el documento a otra área/persona"""
        from app.models.movimiento import Movimiento
        
        # Crear un nuevo movimiento
        movimiento = Movimiento(
            documento_id=self.id,
            fecha_hora=datetime.utcnow(),
            usuario_origen_id=usuario_origen.id,
            area_origen_id=self.area_destino_id,
            persona_origen_id=self.persona_destino_id,
            area_destino_id=area_destino.id,
            persona_destino_id=persona_destino.id,
            estado_documento_id=estado_nuevo.id,
            observaciones=observaciones
        )
        db.session.add(movimiento)
        
        # Actualizar el documento
        self.area_destino_id = area_destino.id
        self.persona_destino_id = persona_destino.id
        self.estado_actual_id = estado_nuevo.id
        
        db.session.commit()
        return self
    
    def finalizar(self, usuario):
        """Marca el documento como finalizado"""
        from app.models.estado_documento import EstadoDocumento
        estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
        
        return self.transferir(
            usuario_origen=usuario,
            area_destino=self.area_destino,
            persona_destino=self.persona_destino,
            estado_nuevo=estado_finalizado,
            observaciones='Documento finalizado'
        )
    
    def archivar(self, usuario):
        """Marca el documento como archivado"""
        from app.models.estado_documento import EstadoDocumento
        estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
        
        return self.transferir(
            usuario_origen=usuario,
            area_destino=self.area_destino,
            persona_destino=self.persona_destino,
            estado_nuevo=estado_archivado,
            observaciones='Documento archivado'
        )
    
    def __repr__(self):
        return f"<Documento {self.radicado}>"