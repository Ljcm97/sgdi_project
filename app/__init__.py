from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from datetime import datetime
from dotenv import load_dotenv
import os

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    from app.config import Config
    app.config.from_object(Config)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key_muy_secreta')
    
    # Cargar configuración desde variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Cargar configuración de correo desde el archivo .env
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))  # Convertir a entero, con valor predeterminado de 587
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() in ('true', 'yes', '1')  # Ajuste para manejar valores booleanos
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
    app.config['MAIL_ASCII_ATTACHMENTS'] = False  # Desactivar la codificación ASCII para archivos adjuntos
    app.config['MAIL_CHARSET'] = 'utf-8'  # Establecer la codificación de caracteres

    # Mostrar detalles de configuración para depuración
    print(f"Configuración de correo: {app.config.get('MAIL_SERVER')}, {app.config.get('MAIL_PORT')}")
    print(f"Usuario de correo: {app.config.get('MAIL_USERNAME')}")
    
    # Inicializar extensiones con la aplicación
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    
    # Configuración del login
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor inicie sesión para acceder a esta página.'
    login_manager.login_message_category = 'info'
    
    # Registro de blueprints
    from app.controllers.auth import auth_bp
    from app.controllers.dashboard import dashboard_bp
    from app.controllers.documentos import documentos_bp
    from app.controllers.personas import personas_bp
    from app.controllers.unidades import unidades_bp
    from app.controllers.areas import areas_bp
    from app.controllers.cargos import cargos_bp
    from app.controllers.zonas_economicas import zonas_economicas_bp
    from app.controllers.transportadoras import transportadoras_bp
    from app.controllers.tipos_documento import tipos_documento_bp
    from app.controllers.estados_documento import estados_documento_bp
    from app.controllers.usuarios import usuarios_bp
    from app.controllers.roles import roles_bp
    from app.controllers.reportes import reportes_bp
    from app.controllers.notificaciones import notificaciones_bp
    from app.controllers.perfil import perfil_bp
    from app.controllers.exportacion import exportacion_bp
    from app.utils.template_filters import template_filters_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(documentos_bp)
    app.register_blueprint(personas_bp)
    app.register_blueprint(unidades_bp)
    app.register_blueprint(areas_bp)
    app.register_blueprint(cargos_bp)
    app.register_blueprint(zonas_economicas_bp)
    app.register_blueprint(transportadoras_bp)
    app.register_blueprint(tipos_documento_bp)
    app.register_blueprint(estados_documento_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(reportes_bp)
    app.register_blueprint(notificaciones_bp)
    app.register_blueprint(perfil_bp)
    app.register_blueprint(exportacion_bp)
    app.register_blueprint(template_filters_bp)

    # Contexto para templates
    @app.context_processor
    def utility_processor():
        def get_year():
            return datetime.now().year
        
        # Importa la función check_permission
        from app.utils.auth import check_permission
        
        # Devuelve un diccionario con todas las funciones que quieres disponibles en las plantillas
        return dict(get_year=get_year, check_permission=check_permission)

    # Manejador de errores
    from app.utils.error_handlers import register_error_handlers
    register_error_handlers(app)
    
    return app
