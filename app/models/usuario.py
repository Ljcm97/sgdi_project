from flask_login import UserMixin
from datetime import datetime
from app import db, login_manager, bcrypt
from app.utils.db import CRUDMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin, CRUDMixin):
    """Modelo para los usuarios del sistema"""
    
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    ultimo_acceso = db.Column(db.DateTime)
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    persona = db.relationship('Persona', backref=db.backref('usuario', uselist=False, lazy=True))
    rol = db.relationship('Rol', backref=db.backref('usuarios', lazy=True))
    notificaciones = db.relationship('Notificacion', backref='usuario', lazy=True)
    
    @property
    def is_active(self):
        return self.activo
    
    def verificar_password(self, password):
        """Verifica si el password proporcionado coincide con el hash almacenado"""
        return bcrypt.check_password_hash(self.password, password)
    
    @classmethod
    def crear_usuario(cls, username, password, persona_id, rol_id):
        """Crea un nuevo usuario con password hasheado"""
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        usuario = cls(
            username=username,
            password=hashed_password,
            persona_id=persona_id,
            rol_id=rol_id
        )
        return usuario.save()
    
    def actualizar_password(self, password):
        """Actualiza el password del usuario"""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        return self.save()
    
    def registrar_acceso(self):
        """Registra la fecha y hora del último acceso"""
        self.ultimo_acceso = datetime.utcnow()
        return self.save()
    
    def tiene_notificaciones_no_leidas(self):
        """Verifica si el usuario tiene notificaciones sin leer"""
        return any(not n.leida for n in self.notificaciones)
    
    def contar_notificaciones_no_leidas(self):
        """Cuenta las notificaciones no leídas del usuario"""
        return sum(1 for n in self.notificaciones if not n.leida)
    
    def __repr__(self):
        return f"<Usuario {self.username}>"