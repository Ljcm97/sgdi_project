from flask import Response, send_file
import pandas as pd
import io
import xml.etree.ElementTree as ET
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def exportar_excel(datos, nombre_archivo):
    """
    Exporta los datos a un archivo Excel
    
    Args:
        datos (dict): Diccionario con encabezados y datos
        nombre_archivo (str): Nombre del archivo sin extensión
    
    Returns:
        Response: Archivo Excel para descargar
    """
    # Crear DataFrame
    df = pd.DataFrame(datos['datos'])
    
    # Crear archivo Excel en memoria
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Reporte')
    
    # Formatear el Excel
    workbook = writer.book
    worksheet = writer.sheets['Reporte']
    
    # Formato para encabezados
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Aplicar formato a encabezados
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        # Ajustar ancho de columna
        column_width = max(len(str(value)), df[value].astype(str).map(len).max())
        worksheet.set_column(col_num, col_num, column_width + 2)
    
    # Cerrar el escritor
    writer.close()
    
    # Configurar la respuesta
    output.seek(0)
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=f"{nombre_archivo}.xlsx"
    )

def exportar_pdf(datos, nombre_archivo, tipo_reporte):
    """
    Exporta los datos a un archivo PDF
    
    Args:
        datos (dict): Diccionario con encabezados y datos
        nombre_archivo (str): Nombre del archivo sin extensión
        tipo_reporte (str): Tipo de reporte
    
    Returns:
        Response: Archivo PDF para descargar
    """
    # Crear un buffer en memoria
    buffer = io.BytesIO()
    
    # Crear el documento PDF
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(letter),
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Contenedor para los elementos del PDF
    elements = []
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Título
    titulo = Paragraph(f"Reporte de {tipo_reporte.capitalize()} - {datetime.now().strftime('%Y-%m-%d')}", styles["Title"])
    elements.append(titulo)
    elements.append(Spacer(1, 12))
    
    # Datos para la tabla
    encabezados = datos['encabezados']
    data = [encabezados]  # Primera fila son los encabezados
    
    # Agregar filas de datos
    for fila in datos['datos']:
        data.append([fila.get(col, '') for col in encabezados])
    
    # Crear la tabla
    tabla = Table(data)
    
    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    
    # Aplicar estilo alternado a las filas
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.add('BACKGROUND', (0, i), (-1, i), colors.lightgrey)
    
    tabla.setStyle(style)
    elements.append(tabla)
    
    # Construir el documento
    doc.build(elements)
    
    # Configurar la respuesta
    buffer.seek(0)
    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f"{nombre_archivo}.pdf"
    )

def exportar_xml(datos, nombre_archivo):
    """
    Exporta los datos a un archivo XML
    
    Args:
        datos (dict): Diccionario con encabezados y datos
        nombre_archivo (str): Nombre del archivo sin extensión
    
    Returns:
        Response: Archivo XML para descargar
    """
    # Crear el elemento raíz
    root = ET.Element('reporte')
    root.set('fecha', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    root.set('nombre', nombre_archivo)
    
    # Agregar las filas
    for fila in datos['datos']:
        row_element = ET.SubElement(root, 'registro')
        
        # Agregar cada campo como un subelemento
        for encabezado in datos['encabezados']:
            field_element = ET.SubElement(row_element, encabezado.replace(' ', '_').lower())
            field_element.text = str(fila.get(encabezado, ''))
    
    # Convertir a string
    xml_str = ET.tostring(root, encoding='utf-8', method='xml')
    
    # Crear respuesta
    return Response(
        xml_str,
        mimetype='application/xml',
        headers={'Content-Disposition': f'attachment;filename={nombre_archivo}.xml'}
    )