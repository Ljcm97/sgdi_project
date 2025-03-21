# SGDI - Sistema de Gestión Documental Interna

Sistema de Gestión Documental Interna para Agroindustrial Molino Sonora AP S.A.S, desarrollado con Python, Flask, Bootstrap y MySQL.

## Características

- Sistema de autenticación y control de acceso basado en roles
- Gestión de documentos (recepción, asignación, transferencia, finalización)
- Historial de movimientos de documentos
- Sistema de notificaciones en tiempo real
- Reportes estadísticos
- Módulos administrativos para gestión de:
  - Personas
  - Unidades
  - Áreas
  - Cargos
  - Zonas económicas
  - Transportadoras
  - Tipos de documento
  - Estados de documento
  - Usuarios y roles

## Requisitos previos

- Python 3.8 o superior
- MySQL 5.7 o superior
- Pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd sgdi_project
```

2. Crear y activar un entorno virtual:

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Crear archivo `.env` con las variables de entorno necesarias (usa `.env.example` como referencia).

5. Crear la base de datos en MySQL:

```sql
CREATE DATABASE sgdi_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

6. Ejecutar el script SQL para crear la estructura inicial:

```bash
mysql -u <usuario> -p sgdi_db < database/schema.sql
```

7. Inicializar la aplicación:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Ejecución

Para ejecutar la aplicación en modo desarrollo:

```bash
flask run
# o
python run.py
```

La aplicación estará disponible en `http://localhost:5000`

## Credenciales iniciales

- Superadministrador:
  - Usuario: `rbohorquez`
  - Contraseña: `admin123`

- Recepción:
  - Usuario: `yfayad`
  - Contraseña: `recepcion123`

- Usuario estándar:
  - Usuario: `jlozano`
  - Contraseña: `usuario123`

## Estructura del proyecto

- `app/`: Contiene la aplicación principal
  - `static/`: Archivos estáticos (CSS, JS, imágenes)
  - `templates/`: Plantillas HTML
  - `models/`: Modelos de la base de datos
  - `controllers/`: Controladores para manejar las rutas
  - `utils/`: Utilidades y funciones auxiliares
- `migrations/`: Migraciones de la base de datos
- `tests/`: Pruebas unitarias y de integración
- `requirements.txt`: Dependencias del proyecto
- `run.py`: Script para ejecutar la aplicación

## Autor

- Ricardo Alexander Bohórquez Méndez - Analista de Sistemas

## Licencia

Este proyecto es propiedad de Agroindustrial Molino Sonora AP S.A.S. Todos los derechos reservados.