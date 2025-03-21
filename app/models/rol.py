from datetime import datetime
from app import db
from app.utils.db import CRUDMixin

# Tabla de relación muchos a muchos entre roles y permisos
roles_permisos = db.Table('roles_permisos',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('rol_id', db.Integer, db.ForeignKey('roles.id'), nullable=False),
    db.Column('permiso_id', db.Integer, db.ForeignKey('permisos.id'), nullable=False),
    db.Column('creado_en', db.DateTime, default=datetime.utcnow)
)

class Rol(db.Model, CRUDMixin):
    """Modelo para los roles de usuario"""
    
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación muchos a muchos con permisos
    permisos = db.relationship('Permiso', secondary=roles_permisos, 
                               backref=db.backref('roles', lazy='dynamic'))
    
    def agregar_permiso(self, permiso):
        """Agrega un permiso al rol"""
        if permiso not in self.permisos:
            self.permisos.append(permiso)
            return self.save()
        return self
    
    def quitar_permiso(self, permiso):
        """Quita un permiso del rol"""
        if permiso in self.permisos:
            self.permisos.remove(permiso)
            return self.save()
        return self
    
    def tiene_permiso(self, permiso_nombre):
        """Verifica si el rol tiene un permiso específico"""
        return any(p.nombre == permiso_nombre for p in self.permisos)
    
    def __repr__(self):
        return f"<Rol {self.nombre}>"