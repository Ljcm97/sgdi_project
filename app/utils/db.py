from app import db
from datetime import datetime

class CRUDMixin:
    """Mixin que proporciona métodos CRUD para los modelos"""
    
    @classmethod
    def create(cls, **kwargs):
        """Crea una nueva instancia del modelo y la guarda en la base de datos"""
        instance = cls(**kwargs)
        return instance.save()
    
    def update(self, commit=True, **kwargs):
        """Actualiza los atributos de la instancia con los valores proporcionados"""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            return self.save()
        return self
    
    def save(self, commit=True):
        """Guarda la instancia en la base de datos"""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self
    
    def delete(self, commit=True):
        """Elimina la instancia de la base de datos"""
        db.session.delete(self)
        if commit:
            db.session.commit()