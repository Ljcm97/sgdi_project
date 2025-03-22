from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    """Formulario de inicio de sesión"""
    
    username = StringField('Usuario', validators=[
        DataRequired(message='El nombre de usuario es obligatorio'),
        Length(min=3, max=50, message='El usuario debe tener entre 3 y 50 caracteres')
    ])
    
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es obligatoria')
    ])
    
    remember = BooleanField('Recordar sesión')
    
    submit = SubmitField('Iniciar Sesión')


class ChangePasswordForm(FlaskForm):
    """Formulario para cambiar la contraseña"""
    
    current_password = PasswordField('Contraseña actual', validators=[
        DataRequired(message='La contraseña actual es obligatoria')
    ])
    
    new_password = PasswordField('Nueva contraseña', validators=[
        DataRequired(message='La nueva contraseña es obligatoria'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(message='Debe confirmar la contraseña'),
        EqualTo('new_password', message='Las contraseñas no coinciden')
    ])
    
    submit = SubmitField('Cambiar Contraseña')
    
    def validate(self, **kwargs):
        """Validación personalizada para el formulario"""
        if not super().validate(**kwargs):
            return False
        
        if self.current_password.data == self.new_password.data:
            self.new_password.errors.append('La nueva contraseña debe ser diferente a la actual')
            return False
        
        return True


class ResetPasswordRequestForm(FlaskForm):
    """Formulario para solicitar restablecimiento de contraseña"""
    
    email = EmailField('Email', validators=[
        DataRequired(message='El email es obligatorio'),
        Email(message='Ingrese un email válido')
    ])
    
    submit = SubmitField('Solicitar Restablecimiento')


class ResetPasswordForm(FlaskForm):
    """Formulario para restablecer contraseña"""
    
    password = PasswordField('Nueva contraseña', validators=[
        DataRequired(message='La contraseña es obligatoria'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(message='Debe confirmar la contraseña'),
        EqualTo('password', message='Las contraseñas no coinciden')
    ])
    
    submit = SubmitField('Restablecer Contraseña')
