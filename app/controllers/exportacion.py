from flask import Blueprint, send_file, jsonify, Response
from flask_login import login_required
from app.utils.auth import permission_required
import io
import pandas as pd
from app.utils.exportacion import exportar_excel, exportar_pdf, exportar_xml

exportacion_bp = Blueprint('exportacion', __name__, url_prefix='/exportacion')

@exportacion_bp.route('/excel/<tipo_reporte>')
@login_required
@permission_required('Ver reportes')
def excel(tipo_reporte):
    """Exporta los datos del reporte a Excel"""
    # Esta es una ruta alternativa que redirecciona a reportes.exportar
    from app.controllers.reportes import exportar
    return exportar('excel')

@exportacion_bp.route('/pdf/<tipo_reporte>')
@login_required
@permission_required('Ver reportes')
def pdf(tipo_reporte):
    """Exporta los datos del reporte a PDF"""
    # Esta es una ruta alternativa que redirecciona a reportes.exportar
    from app.controllers.reportes import exportar
    return exportar('pdf')

@exportacion_bp.route('/xml/<tipo_reporte>')
@login_required
@permission_required('Ver reportes')
def xml(tipo_reporte):
    """Exporta los datos del reporte a XML"""
    # Esta es una ruta alternativa que redirecciona a reportes.exportar
    from app.controllers.reportes import exportar
    return exportar('xml')

