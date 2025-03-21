from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

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
        DataRequired(message='Debe confirmar la contraseña')
    ])
    
    submit = SubmitField('Cambiar Contraseña')
    
    def validate(self):
        """Validación personalizada para el formulario"""
        if not super().validate():
            return False
        
        if self.new_password.data != self.confirm_password.data:
            self.confirm_password.errors.append('Las contraseñas no coinciden')
            return False
        
        if self.current_password.data == self.new_password.data:
            self.new_password.errors.append('La nueva contraseña debe ser diferente a la actual')
            return False
        
        return True