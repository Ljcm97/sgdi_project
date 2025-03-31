import re
from wtforms.validators import ValidationError

def validate_password_complexity(form, field):
    """
    Valida que la contraseña tenga la complejidad requerida:
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial
    - Longitud mínima 8 caracteres (esto ya se valida con Length)
    """
    password = field.data
    
    error_message = "La contraseña debe contener una combinación de letras mayúsculas, minúsculas, números y símbolos."
    
    # Verificar que cumpla con todos los requisitos
    if not (re.search(r"[A-Z]", password) and  # mayúsculas
            re.search(r"[a-z]", password) and  # minúsculas
            re.search(r"[0-9]", password) and  # números
            re.search(r"[ !@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password)):  # caracteres especiales
        raise ValidationError(error_message)