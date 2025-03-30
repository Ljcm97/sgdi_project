from datetime import datetime
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models.documento import Documento
from app.models.movimiento import Movimiento
from app.models.persona import Persona
from app.models.area import Area
from app.models.estado_documento import EstadoDocumento
from app.models.usuario import Usuario
from app.forms.documento import DocumentoForm, TransferirDocumentoForm
from app.forms.buscar import BuscarDocumentoForm
from app.utils.auth import permission_required, check_permission
from app.utils.decorators import document_access_required, has_document_access, role_required
from app.utils.helpers import crear_notificacion, flash_errors
from app.utils.pagination import Pagination
from app.utils.exportacion import exportar_excel, exportar_pdf, exportar_xml
from sqlalchemy import or_

documentos_bp = Blueprint('documentos', __name__, url_prefix='/documentos')

@documentos_bp.route('/')
@login_required
@permission_required('Ver documento')
def index():
    """Vista principal que muestra el formulario de registro y la lista de documentos"""
    # Obtener el formulario de registro
    form = DocumentoForm()
    
    # Establecer fecha actual por defecto
    form.fecha_recepcion.data = datetime.now()
    
    # Obtener el formulario de búsqueda
    buscar_form = BuscarDocumentoForm()
    
    # Verificar si hay parámetros de búsqueda
    is_search = any(key for key in request.args.keys() if key != 'page' and key != 'per_page' and request.args.get(key))
    
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Si hay parámetros de búsqueda, realizar búsqueda
    if is_search:
        # Construir la consulta base
        query = Documento.query
        
        # Aplicar filtros si están presentes
        if request.args.get('radicado'):
            query = query.filter(Documento.radicado.like(f'%{request.args.get("radicado")}%'))
        
        if request.args.get('fecha_desde'):
            try:
                fecha_desde = datetime.strptime(request.args.get('fecha_desde'), '%Y-%m-%d')
                query = query.filter(Documento.fecha_recepcion >= fecha_desde)
            except ValueError:
                pass
        
        if request.args.get('fecha_hasta'):
            try:
                fecha_hasta = datetime.strptime(request.args.get('fecha_hasta'), '%Y-%m-%d')
                # Incluir todo el día
                fecha_hasta = datetime.combine(fecha_hasta.date(), datetime.max.time())
                query = query.filter(Documento.fecha_recepcion <= fecha_hasta)
            except ValueError:
                pass
        
        if request.args.get('transportadora_id') and int(request.args.get('transportadora_id')) > 0:
            query = query.filter_by(transportadora_id=request.args.get('transportadora_id'))
        
        if request.args.get('tipo_documento_id') and int(request.args.get('tipo_documento_id')) > 0:
            query = query.filter_by(tipo_documento_id=request.args.get('tipo_documento_id'))
        
        if request.args.get('estado_id') and int(request.args.get('estado_id')) > 0:
            query = query.filter_by(estado_actual_id=request.args.get('estado_id'))
        
        if request.args.get('tipo'):
            query = query.filter_by(tipo=request.args.get('tipo'))
        
        if request.args.get('remitente'):
            query = query.filter(Documento.remitente.like(f'%{request.args.get("remitente")}%'))
        
        # Filtrar según el rol del usuario
        if current_user.rol.nombre == 'Superadministrador':
            # Superadministrador ve todos los documentos
            pass
        elif current_user.rol.nombre == 'Recepción':
            # Recepción ve los documentos que ha registrado
            query = query.filter_by(registrado_por_id=current_user.id)
        else:
            # Usuario regular ve los documentos de su área o asignados a él
            query = query.filter(
                or_(
                    Documento.area_destino_id == current_user.persona.area_id,
                    Documento.persona_destino_id == current_user.persona_id
                )
            )
        
        # Ordenar por fecha de creación (más recientes primero)
        query = query.order_by(Documento.creado_en.desc())
        
        # Paginar los resultados
        pagination = Pagination(query, page, per_page, 'documentos.index')
        documentos = pagination.items
        
        # Pasar los parámetros de búsqueda al formulario para mantenerlos en la interfaz
        for key, value in request.args.items():
            if key in buscar_form._fields:
                field = getattr(buscar_form, key)
                if hasattr(field, 'data'):
                    try:
                        field.data = value
                    except:
                        pass
    else:
        # Si no hay búsqueda, obtener documentos según el rol del usuario
        if current_user.rol.nombre == 'Superadministrador':
            query = Documento.query.order_by(Documento.creado_en.desc())
        elif current_user.rol.nombre == 'Recepción':
            query = Documento.query.filter_by(registrado_por_id=current_user.id).order_by(Documento.creado_en.desc())
        else:
            query = Documento.query.filter(
                or_(
                    Documento.area_destino_id == current_user.persona.area_id,
                    Documento.persona_destino_id == current_user.persona_id
                )
            ).order_by(Documento.creado_en.desc())
        
        # Paginar los resultados
        pagination = Pagination(query, page, per_page, 'documentos.index')
        documentos = pagination.items
    
    return render_template('documentos/index.html', 
                          form=form,
                          buscar_form=buscar_form, 
                          documentos=documentos,
                          pagination=pagination,
                          mostrar_busqueda=False,
                          mostrar_tabla=True,
                          is_search=is_search)

@documentos_bp.route('/procesar', methods=['POST'])
@login_required
@permission_required('Crear documento')
def procesar():
    """Vista para procesar el formulario de registro sin cambiar de página"""
    form = DocumentoForm()
    buscar_form = BuscarDocumentoForm()
    
    if form.validate_on_submit():
        # Obtener el estado inicial (Recibido)
        estado_recibido = EstadoDocumento.query.filter_by(nombre='Recibido').first()
        
        # Crear el documento
        documento = Documento.crear_documento(
            fecha_recepcion=form.fecha_recepcion.data,
            transportadora_id=form.transportadora_id.data,
            numero_guia=form.numero_guia.data,
            remitente=form.remitente.data,
            tipo_documento_id=form.tipo_documento_id.data,
            contenido=form.contenido.data,
            observaciones=form.observaciones.data,
            area_destino_id=form.area_destino_id.data,
            persona_destino_id=form.persona_destino_id.data,
            estado_actual_id=estado_recibido.id,
            tipo=form.tipo.data,
            registrado_por_id=current_user.id
        )
        
        # Crear el movimiento inicial
        movimiento = Movimiento(
            documento_id=documento.id,
            fecha_hora=documento.fecha_recepcion,
            usuario_origen_id=current_user.id,
            area_origen_id=current_user.persona.area_id,
            persona_origen_id=current_user.persona_id,
            area_destino_id=documento.area_destino_id,
            persona_destino_id=documento.persona_destino_id,
            estado_documento_id=estado_recibido.id,
            observaciones='Documento registrado en recepción'
        )
        db.session.add(movimiento)
        
        # Crear notificación para la persona destino
        persona_destino = Persona.query.get(documento.persona_destino_id)
        usuario_destino = Usuario.query.filter_by(persona_id=persona_destino.id).first()
        
        if usuario_destino:
            crear_notificacion(
                usuario_id=usuario_destino.id,
                titulo=f'Nuevo documento asignado - {documento.radicado}',
                mensaje=f'Se te ha asignado un nuevo documento de tipo {documento.tipo_documento.nombre}.',
                documento_id=documento.id
            )
        
        db.session.commit()
        
        flash(f'Documento registrado con éxito. Radicado: {documento.radicado}', 'success')
        
        # Redirigir a la misma página para mantener el formulario activo
        return redirect(url_for('documentos.index'))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Obtener documentos nuevamente para mostrar en la tabla
    if current_user.rol.nombre == 'Superadministrador':
        query = Documento.query.order_by(Documento.creado_en.desc())
    elif current_user.rol.nombre == 'Recepción':
        query = Documento.query.filter_by(registrado_por_id=current_user.id).order_by(Documento.creado_en.desc())
    else:
        query = Documento.query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        ).order_by(Documento.creado_en.desc())
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'documentos.index')
    documentos = pagination.items
    
    return render_template('documentos/index.html', 
                          form=form, 
                          buscar_form=buscar_form,
                          documentos=documentos,
                          pagination=pagination,  # Añadir la variable pagination aquí
                          mostrar_busqueda=False,
                          mostrar_tabla=True)

@documentos_bp.route('/mostrar-busqueda')
@login_required
def mostrar_busqueda():
    """Vista para mostrar los filtros de búsqueda"""
    # Obtener el formulario de registro
    form = DocumentoForm()
    
    # Establecer fecha actual por defecto
    form.fecha_recepcion.data = datetime.now()
    
    # Inicializar el formulario de búsqueda
    buscar_form = BuscarDocumentoForm()
    
    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Obtener documentos según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador':
        query = Documento.query.order_by(Documento.creado_en.desc())
    elif current_user.rol.nombre == 'Recepción':
        query = Documento.query.filter_by(registrado_por_id=current_user.id).order_by(Documento.creado_en.desc())
    else:
        query = Documento.query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        ).order_by(Documento.creado_en.desc())
    
    # Paginar los resultados
    pagination = Pagination(query, page, per_page, 'documentos.index')
    documentos = pagination.items
    
    return render_template('documentos/index.html', 
                         form=form, 
                         buscar_form=buscar_form,
                         documentos=documentos,
                         pagination=pagination,  # Añadir la variable pagination aquí
                         mostrar_busqueda=True,
                         mostrar_tabla=True)

@documentos_bp.route('/registrar', methods=['GET', 'POST'])
@login_required
@permission_required('Crear documento')
def registrar():
    """Vista para registrar un nuevo documento"""
    form = DocumentoForm()
    
    # Establecer fecha actual por defecto
    if request.method == 'GET':
        form.fecha_recepcion.data = datetime.now()
    
    if form.validate_on_submit():
        # Obtener el estado inicial (Recibido)
        estado_recibido = EstadoDocumento.query.filter_by(nombre='Recibido').first()
        
        # Crear el documento
        documento = Documento.crear_documento(
            fecha_recepcion=form.fecha_recepcion.data,
            transportadora_id=form.transportadora_id.data,
            numero_guia=form.numero_guia.data,
            remitente=form.remitente.data,
            tipo_documento_id=form.tipo_documento_id.data,
            contenido=form.contenido.data,
            observaciones=form.observaciones.data,
            area_destino_id=form.area_destino_id.data,
            persona_destino_id=form.persona_destino_id.data,
            estado_actual_id=estado_recibido.id,
            tipo=form.tipo.data,
            registrado_por_id=current_user.id
        )
        
        # Crear el movimiento inicial
        movimiento = Movimiento(
            documento_id=documento.id,
            fecha_hora=documento.fecha_recepcion,
            usuario_origen_id=current_user.id,
            area_origen_id=current_user.persona.area_id,
            persona_origen_id=current_user.persona_id,
            area_destino_id=documento.area_destino_id,
            persona_destino_id=documento.persona_destino_id,
            estado_documento_id=estado_recibido.id,
            observaciones='Documento registrado en recepción'
        )
        db.session.add(movimiento)
        
        # Crear notificación para la persona destino
        persona_destino = Persona.query.get(documento.persona_destino_id)
        usuario_destino = Usuario.query.filter_by(persona_id=persona_destino.id).first()
        
        if usuario_destino:
            crear_notificacion(
                usuario_id=usuario_destino.id,
                titulo=f'Nuevo documento asignado - {documento.radicado}',
                mensaje=f'Se te ha asignado un nuevo documento de tipo {documento.tipo_documento.nombre}.',
                documento_id=documento.id
            )
        
        db.session.commit()
        
        flash(f'Documento registrado con éxito. Radicado: {documento.radicado}', 'success')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('documentos/registro.html', form=form)


@documentos_bp.route('/detalle/<int:id>')
@login_required
@document_access_required
def detalle(id):
    """Vista para ver el detalle de un documento"""
    documento = Documento.query.get_or_404(id)
    
    # Verificar si el usuario tiene acceso al documento
    if not has_document_access(documento):
        flash('No tienes acceso a este documento.', 'danger')
        return redirect(url_for('dashboard.index'))
    
    # Obtener los movimientos del documento
    movimientos = Movimiento.query.filter_by(documento_id=documento.id).order_by(Movimiento.fecha_hora).all()
    
    return render_template('documentos/detalle.html', 
                          documento=documento, 
                          movimientos=movimientos)


@documentos_bp.route('/transferir/<int:id>', methods=['GET', 'POST'])
@login_required
@document_access_required
@permission_required('Transferir documento')
def transferir(id):
    """Vista para transferir un documento"""
    documento = Documento.query.get_or_404(id)
    form = TransferirDocumentoForm()
    
    if form.validate_on_submit():
        # Obtener los objetos necesarios
        area_destino = Area.query.get(form.area_destino_id.data)
        persona_destino = Persona.query.get(form.persona_destino_id.data)
        estado_nuevo = EstadoDocumento.query.get(form.estado_id.data)
        
        # Transferir el documento
        documento.transferir(
            usuario_origen=current_user,
            area_destino=area_destino,
            persona_destino=persona_destino,
            estado_nuevo=estado_nuevo,
            observaciones=form.observaciones.data
        )
        
        # Crear notificación para la persona destino
        usuario_destino = Usuario.query.filter_by(persona_id=persona_destino.id).first()
        
        if usuario_destino:
            crear_notificacion(
                usuario_id=usuario_destino.id,
                titulo=f'Documento transferido - {documento.radicado}',
                mensaje=f'Se te ha transferido un documento de tipo {documento.tipo_documento.nombre}.',
                documento_id=documento.id
            )
        
        flash('Documento transferido exitosamente.', 'success')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)
    
    return render_template('documentos/transferir.html', 
                          documento=documento, 
                          form=form)

@documentos_bp.route('/aceptar/<int:id>')
@login_required
@document_access_required
@permission_required('Aceptar documento')
def aceptar(id):
    """Vista para aceptar un documento"""
    documento = Documento.query.get_or_404(id)
    
    # Verificar si el documento está asignado al usuario actual
    if documento.persona_destino_id != current_user.persona_id:
        flash('No puedes aceptar este documento porque no está asignado a ti.', 'danger')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Obtener el estado "En proceso"
    estado_en_proceso = EstadoDocumento.query.filter_by(nombre='En proceso').first()
    
    # Transferir el documento al mismo usuario pero cambiar el estado
    documento.transferir(
        usuario_origen=current_user,
        area_destino=current_user.persona.area,
        persona_destino=current_user.persona,
        estado_nuevo=estado_en_proceso,
        observaciones='Documento aceptado para procesamiento'
    )
    
    # Notificar a recepción que se aceptó el documento
    usuario_recepcion = documento.registrado_por
    
    crear_notificacion(
        usuario_id=usuario_recepcion.id,
        titulo=f'Documento aceptado - {documento.radicado}',
        mensaje=f'El documento ha sido aceptado por {current_user.persona.nombre_completo}.',
        documento_id=documento.id
    )
    
    flash('Documento aceptado exitosamente.', 'success')
    return redirect(url_for('documentos.detalle', id=documento.id))


@documentos_bp.route('/rechazar/<int:id>')
@login_required
@document_access_required
@permission_required('Rechazar documento')
def rechazar(id):
    """Vista para rechazar un documento"""
    documento = Documento.query.get_or_404(id)
    
    # Verificar si el documento está asignado al usuario actual
    if documento.persona_destino_id != current_user.persona_id:
        flash('No puedes rechazar este documento porque no está asignado a ti.', 'danger')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Transferir el documento de vuelta a recepción
    area_recepcion = Area.query.filter_by(nombre='RECEPCION').first()
    persona_recepcion = Persona.query.filter_by(area_id=area_recepcion.id).first()
    
    if not area_recepcion or not persona_recepcion:
        flash('No se pudo encontrar el área o persona de recepción.', 'danger')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Obtener el estado "Rechazado" (si existe) o "Recibido" (como fallback)
    estado_rechazado = EstadoDocumento.query.filter_by(nombre='Rechazado').first()
    
    # Si no existe el estado "Rechazado", usar "Recibido"
    if not estado_rechazado:
        estado_rechazado = EstadoDocumento.query.filter_by(nombre='Recibido').first()
    
    # Transferir el documento
    documento.transferir(
        usuario_origen=current_user,
        area_destino=area_recepcion,
        persona_destino=persona_recepcion,
        estado_nuevo=estado_rechazado,
        observaciones=f'Documento rechazado por {current_user.persona.nombre_completo}'
    )
    
    # Notificar a recepción que se rechazó el documento
    usuario_recepcion = Usuario.query.filter_by(persona_id=persona_recepcion.id).first()
    
    if usuario_recepcion:
        crear_notificacion(
            usuario_id=usuario_recepcion.id,
            titulo=f'Documento rechazado - {documento.radicado}',
            mensaje=f'El documento ha sido rechazado por {current_user.persona.nombre_completo}.',
            documento_id=documento.id
        )
    
    flash('Documento rechazado exitosamente.', 'success')
    return redirect(url_for('documentos.detalle', id=documento.id))


@documentos_bp.route('/finalizar/<int:id>')
@login_required
@document_access_required
@permission_required('Transferir documento')
def finalizar(id):
    """Vista para finalizar un documento"""
    documento = Documento.query.get_or_404(id)
    
    # Finalizar el documento
    documento.finalizar(current_user)
    
    flash('Documento finalizado exitosamente.', 'success')
    return redirect(url_for('documentos.detalle', id=documento.id))


@documentos_bp.route('/archivar/<int:id>')
@login_required
@document_access_required
@permission_required('Transferir documento')
def archivar(id):
    """Vista para archivar un documento"""
    documento = Documento.query.get_or_404(id)
    
    # Archivar el documento
    documento.archivar(current_user)
    
    flash('Documento archivado exitosamente.', 'success')
    return redirect(url_for('documentos.detalle', id=documento.id))


@documentos_bp.route('/buscar', methods=['GET', 'POST'])
@login_required
def buscar():
    """Vista para buscar documentos"""
    form = BuscarDocumentoForm()
    documentos = []
    
    if form.validate_on_submit() or request.args.get('buscar'):
        # Construir la consulta base
        query = Documento.query
        
        # Aplicar filtros si están presentes
        if form.radicado.data:
            query = query.filter(Documento.radicado.like(f'%{form.radicado.data}%'))
        
        if form.fecha_desde.data:
            query = query.filter(Documento.fecha_recepcion >= form.fecha_desde.data)
        
        if form.fecha_hasta.data:
            query = query.filter(Documento.fecha_recepcion <= form.fecha_hasta.data)
        
        if form.transportadora_id.data and int(form.transportadora_id.data) > 0:
            query = query.filter_by(transportadora_id=form.transportadora_id.data)
        
        if form.tipo_documento_id.data and int(form.tipo_documento_id.data) > 0:
            query = query.filter_by(tipo_documento_id=form.tipo_documento_id.data)
        
        if form.estado_id.data and int(form.estado_id.data) > 0:
            query = query.filter_by(estado_actual_id=form.estado_id.data)
        
        if form.tipo.data:
            query = query.filter_by(tipo=form.tipo.data)
        
        if form.remitente.data:
            query = query.filter(Documento.remitente.like(f'%{form.remitente.data}%'))

            # Filtrar según el rol del usuario
        if current_user.rol.nombre == 'Superadministrador':
            # Superadministrador ve todos los documentos
            pass
        elif current_user.rol.nombre == 'Recepción':
            # Recepción ve los documentos que ha registrado
            query = query.filter_by(registrado_por_id=current_user.id)
        else:
            # Usuario regular ve los documentos de su área o asignados a él
            query = query.filter(
                or_(
                    Documento.area_destino_id == current_user.persona.area_id,
                    Documento.persona_destino_id == current_user.persona_id
                )
            )
        
        # Ejecutar la consulta
        documentos = query.order_by(Documento.creado_en.desc()).all()
    
    return render_template('documentos/buscar.html', 
                          form=form, 
                          documentos=documentos)


@documentos_bp.route('/get_personas/<int:area_id>')
@login_required
def get_personas(area_id):
    """API para obtener las personas de un área específica"""
    personas = Persona.query.filter_by(area_id=area_id, activo=True).order_by(Persona.nombres_apellidos).all()
    personas_json = [{'id': p.id, 'nombre': p.nombre_completo, 'nombres_apellidos': p.nombres_apellidos} for p in personas]
    return jsonify(personas_json)

@documentos_bp.route('/exportar/<formato>')
@login_required
@permission_required('Ver documento')
def exportar(formato):
    """Exportar lista de documentos en diferentes formatos"""
    # Filtrar documentos según el rol del usuario
    if current_user.rol.nombre == 'Superadministrador':
        query = Documento.query
    elif current_user.rol.nombre == 'Recepción':
        query = Documento.query.filter_by(registrado_por_id=current_user.id)
    else:
        query = Documento.query.filter(
            or_(
                Documento.area_destino_id == current_user.persona.area_id,
                Documento.persona_destino_id == current_user.persona_id
            )
        )
    
    # Aplicar filtros si están presentes en los parámetros de la consulta
    if request.args.get('radicado'):
        query = query.filter(Documento.radicado.like(f'%{request.args.get("radicado")}%'))
    
    if request.args.get('fecha_desde'):
        try:
            fecha_desde = datetime.strptime(request.args.get('fecha_desde'), '%Y-%m-%d')
            query = query.filter(Documento.fecha_recepcion >= fecha_desde)
        except ValueError:
            pass
    
    if request.args.get('fecha_hasta'):
        try:
            fecha_hasta = datetime.strptime(request.args.get('fecha_hasta'), '%Y-%m-%d')
            fecha_hasta = datetime.combine(fecha_hasta.date(), datetime.max.time())
            query = query.filter(Documento.fecha_recepcion <= fecha_hasta)
        except ValueError:
            pass
    
    if request.args.get('transportadora_id') and int(request.args.get('transportadora_id')) > 0:
        query = query.filter_by(transportadora_id=request.args.get('transportadora_id'))
    
    if request.args.get('tipo_documento_id') and int(request.args.get('tipo_documento_id')) > 0:
        query = query.filter_by(tipo_documento_id=request.args.get('tipo_documento_id'))
    
    if request.args.get('estado_id') and int(request.args.get('estado_id')) > 0:
        query = query.filter_by(estado_actual_id=request.args.get('estado_id'))
    
    if request.args.get('tipo'):
        query = query.filter_by(tipo=request.args.get('tipo'))
    
    if request.args.get('remitente'):
        query = query.filter(Documento.remitente.like(f'%{request.args.get("remitente")}%'))
    
    # Obtener documentos
    documentos = query.order_by(Documento.creado_en.desc()).all()
    
    # Preparar datos para exportación
    datos = preparar_datos_exportacion_documentos(documentos)
    
    # Nombre de archivo
    nombre_archivo = f"documentos_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Exportar según formato
    if formato == 'excel':
        return exportar_excel(datos, nombre_archivo)
    elif formato == 'pdf':
        return exportar_pdf(datos, nombre_archivo, 'documentos')
    elif formato == 'xml':
        return exportar_xml(datos, nombre_archivo)
    else:
        flash('Formato de exportación no soportado', 'danger')
        return redirect(url_for('documentos.index'))

def preparar_datos_exportacion_documentos(documentos):
    """Prepara los datos de documentos para exportación"""
    # Definir encabezados
    encabezados = ['Radicado', 'Fecha', 'Tipo', 'Remitente', 'Área', 'Estado', 'Registrado por']
    
    # Preparar datos
    datos = []
    for doc in documentos:
        datos.append({
            'Radicado': doc.radicado,
            'Fecha': doc.fecha_recepcion.strftime('%d/%m/%Y %H:%M'),
            'Tipo': doc.tipo_documento.nombre,
            'Remitente': doc.remitente,
            'Área': doc.area_destino.nombre,
            'Estado': doc.estado_actual.nombre,
            'Registrado por': doc.registrado_por.username
        })
    
    return {'encabezados': encabezados, 'datos': datos}