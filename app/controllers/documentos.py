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
    # Verificar explícitamente si el usuario tiene el rol adecuado
    if current_user.rol.nombre != 'Superadministrador' and current_user.rol.nombre != 'Recepción':
        flash('No tienes permiso para registrar documentos.', 'danger')
        return redirect(url_for('documentos.index'))
    
    form = DocumentoForm()
    buscar_form = BuscarDocumentoForm()
    
    if form.validate_on_submit():
        # Obtener el estado inicial (Recepcionado)
        estado_recepcionado = EstadoDocumento.query.filter_by(nombre='Recepcionado').first()
        
        # La fecha de recepción del formulario
        fecha_recepcion = form.fecha_recepcion.data
        
        # Crear el documento usando la misma fecha tanto para recepción como para creado_en
        documento = Documento.crear_documento(
            fecha_recepcion=fecha_recepcion,
            transportadora_id=form.transportadora_id.data,
            numero_guia=form.numero_guia.data,
            remitente=form.remitente.data,
            tipo_documento_id=form.tipo_documento_id.data,
            contenido=form.contenido.data,
            observaciones=form.observaciones.data,
            area_destino_id=form.area_destino_id.data,
            persona_destino_id=form.persona_destino_id.data,
            estado_actual_id=estado_recepcionado.id,
            tipo=form.tipo.data,
            registrado_por_id=current_user.id,
            creado_en=fecha_recepcion  # ¡Establecer explícitamente la fecha de creación!
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
            estado_documento_id=estado_recepcionado.id,
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
                          pagination=pagination,
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
                         pagination=pagination,
                         mostrar_busqueda=True,
                         mostrar_tabla=True)

@documentos_bp.route('/registrar', methods=['GET', 'POST'])
@login_required
@permission_required('Crear documento')
def registrar():
    """Vista para registrar un nuevo documento"""
    # Verificar explícitamente si el usuario tiene el rol adecuado
    if current_user.rol.nombre != 'Superadministrador' and current_user.rol.nombre != 'Recepción':
        flash('No tienes permiso para registrar documentos.', 'danger')
        return redirect(url_for('documentos.index'))
    
    form = DocumentoForm()
    
    # Establecer fecha actual por defecto
    if request.method == 'GET':
        form.fecha_recepcion.data = datetime.now()
    
    if form.validate_on_submit():
        # Obtener el estado inicial (Recepcionado)
        estado_recepcionado = EstadoDocumento.query.filter_by(nombre='Recepcionado').first()
        
        # La fecha de recepción del formulario
        fecha_recepcion = form.fecha_recepcion.data
        
        # Crear el documento
        documento = Documento.crear_documento(
            fecha_recepcion=fecha_recepcion,
            transportadora_id=form.transportadora_id.data,
            numero_guia=form.numero_guia.data,
            remitente=form.remitente.data,
            tipo_documento_id=form.tipo_documento_id.data,
            contenido=form.contenido.data,
            observaciones=form.observaciones.data,
            area_destino_id=form.area_destino_id.data,
            persona_destino_id=form.persona_destino_id.data,
            estado_actual_id=estado_recepcionado.id,
            tipo=form.tipo.data,
            registrado_por_id=current_user.id,
            creado_en=fecha_recepcion  
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
            estado_documento_id=estado_recepcionado.id,
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
    
    # En la vista GET, buscar el estado "Documento Transferido" por defecto
    estado_transferido = EstadoDocumento.query.filter_by(nombre='Documento Transferido').first()
    
    # Si no existe, usar el estado "Recepcionado" como alternativa
    if not estado_transferido:
        estado_transferido = EstadoDocumento.query.filter_by(nombre='Recepcionado').first()
    
    if estado_transferido:
        form.estado_id.data = estado_transferido.id

    if form.validate_on_submit():
        # Obtener los objetos necesarios
        area_destino = Area.query.get(form.area_destino_id.data)
        persona_destino = Persona.query.get(form.persona_destino_id.data)

        # Validaciones de existencia
        if not area_destino or not persona_destino:
            flash('El área o la persona seleccionada no existen.', 'danger')
            return redirect(url_for('documentos.transferir', id=documento.id))
        
        # Validación de transferencia a mismo destino
        if area_destino.id == documento.area_destino_id and persona_destino.id == documento.persona_destino_id:
            flash('No puedes transferir el documento a la misma área y persona.', 'danger')
            return redirect(url_for('documentos.transferir', id=documento.id))
        
        # Usar estado seleccionado si no se encontró el estado por defecto
        if not estado_transferido:
            estado_nuevo = EstadoDocumento.query.get(form.estado_id.data)
        else:
            estado_nuevo = estado_transferido

        # Transferir el documento
        documento.transferir(
            usuario_origen=current_user,
            area_destino=area_destino,
            persona_destino=persona_destino,
            estado_nuevo=estado_nuevo,
            observaciones=form.observaciones.data or "Documento transferido"
        )

        # Crear notificación para la persona destino
        usuario_destino = Usuario.query.filter_by(persona_id=persona_destino.id).first()
        if usuario_destino:
            crear_notificacion(
                usuario_id=usuario_destino.id,
                titulo=f'Documento transferido - {documento.radicado}',
                mensaje=f'Se te ha transferido un documento de tipo {documento.tipo_documento.nombre} por {current_user.persona.nombre_completo}.',
                documento_id=documento.id
            )

        # Notificar también al registrador original
        if documento.registrado_por_id and documento.registrado_por_id != current_user.id:
            crear_notificacion(
                usuario_id=documento.registrado_por_id,
                titulo=f'Documento transferido - {documento.radicado}',
                mensaje=f'El documento ha sido transferido por {current_user.persona.nombre_completo} a {persona_destino.nombre_completo}.',
                documento_id=documento.id
            )

        flash('Documento transferido exitosamente.', 'success')
        return redirect(url_for('documentos.detalle', id=documento.id))

    # Si hay errores de validación, mostrarlos
    if form.errors:
        flash_errors(form)

    return render_template('documentos/transferir.html', documento=documento, form=form)


@documentos_bp.route('/aceptar/<int:id>', methods=['GET', 'POST'])
@login_required
@document_access_required
@permission_required('Aceptar documento')
def aceptar(id):
    """Vista para aceptar un documento"""
    documento = Documento.query.get_or_404(id)

    # Verificar si el documento está asignado al usuario actual
    if documento.persona_destino_id != current_user.persona_id:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'success': False, 
                'message': 'No puedes aceptar este documento porque no está asignado a ti.'
            }), 403
        flash('No puedes aceptar este documento porque no está asignado a ti.', 'danger')
        return redirect(url_for('documentos.detalle', id=documento.id))

    # Obtener el estado "Recibido" primero
    estado_recibido = EstadoDocumento.query.filter_by(nombre='Recibido').first()

    # Si no existe el estado "Recibido", crearlo
    if not estado_recibido:
        estado_recibido = EstadoDocumento(
            nombre='Recibido',
            descripcion='Documento en proceso de recibirse',
            color='#3498db'  # Azul
        )
        db.session.add(estado_recibido)
        db.session.commit()

    # Crear un movimiento para "Recibido"
    movimiento_recibido = Movimiento(
        documento_id=documento.id,
        fecha_hora=datetime.utcnow(),
        usuario_origen_id=current_user.id,
        area_origen_id=current_user.persona.area_id,
        persona_origen_id=current_user.persona_id,
        area_destino_id=current_user.persona.area_id,
        persona_destino_id=current_user.persona_id,
        estado_documento_id=estado_recibido.id,
        observaciones='Recibido del documento'
    )
    db.session.add(movimiento_recibido)
    db.session.commit()

    # Pausa para asegurar timestamps distintos
    import time
    time.sleep(0.5)

    # Obtener el estado "En proceso"
    estado_en_proceso = EstadoDocumento.query.filter_by(nombre='En proceso').first()

    # Transferir el documento al mismo usuario pero cambiar el estado a "En proceso"
    documento.transferir(
        usuario_origen=current_user,
        area_destino=current_user.persona.area,
        persona_destino=current_user.persona,
        estado_nuevo=estado_en_proceso,
        observaciones='Documento aceptado para procesamiento'
    )

    # Notificar al registrador original si no es el actual
    if documento.registrado_por_id and documento.registrado_por_id != current_user.id:
        crear_notificacion(
            usuario_id=documento.registrado_por_id,
            titulo=f'Documento aceptado - {documento.radicado}',
            mensaje=f'El documento ha sido aceptado por {current_user.persona.nombre_completo}.',
            documento_id=documento.id
        )

    # Notificar al último transferidor si no es el actual
    if documento.ultimo_transferido_por_id and documento.ultimo_transferido_por_id != current_user.id:
        crear_notificacion(
            usuario_id=documento.ultimo_transferido_por_id,
            titulo=f'Documento aceptado - {documento.radicado}',
            mensaje=f'El documento ha sido aceptado por {current_user.persona.nombre_completo}.',
            documento_id=documento.id
        )

    # Responder según el tipo de solicitud
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({
            'success': True,
            'message': 'Documento aceptado exitosamente.',
            'redirect': url_for('documentos.detalle', id=documento.id)
        })

    flash('Documento aceptado exitosamente.', 'success')
    return redirect(url_for('documentos.detalle', id=documento.id))


@documentos_bp.route('/rechazar/<int:id>', methods=['GET', 'POST'])
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

    # Si es una solicitud POST, procesar el formulario
    if request.method == 'POST':
        motivo_rechazo = request.form.get('motivo_rechazo', 'No se especificó motivo')

        # Lógica más robusta para determinar el destino del documento rechazado
        area_destino = None
        persona_destino = None
        usuario_destino = None
        usuario_transferidor = None

        # 1. Si el documento fue transferido por alguien, devolvérselo a esa persona
        if documento.ultimo_transferido_por_id:
            usuario_transferidor = Usuario.query.get(documento.ultimo_transferido_por_id)
            if usuario_transferidor and usuario_transferidor.persona and usuario_transferidor.activo:
                area_destino = usuario_transferidor.persona.area
                persona_destino = usuario_transferidor.persona
                usuario_destino = usuario_transferidor

        # 2. Si no se puede devolver al transferidor, intentar con el registrador original
        if area_destino is None or persona_destino is None:
            if documento.registrado_por and documento.registrado_por.persona and documento.registrado_por.activo:
                area_destino = documento.registrado_por.persona.area
                persona_destino = documento.registrado_por.persona
                usuario_destino = documento.registrado_por

        # 3. Si aún no hay destino, buscar a alguien en recepción
        if area_destino is None or persona_destino is None:
            area_recepcion = Area.query.filter_by(nombre='RECEPCION').first()
            usuario_recepcion = Usuario.query.join(Usuario.persona).join(Usuario.rol).filter(
                Persona.area_id == area_recepcion.id if area_recepcion else 0,
                Usuario.activo == True,
                Rol.nombre == 'Recepción'
            ).first()

            if usuario_recepcion and usuario_recepcion.persona:
                area_destino = area_recepcion
                persona_destino = usuario_recepcion.persona
                usuario_destino = usuario_recepcion

        # Si sigue sin encontrar área/persona destino, mostrar error
        if not area_destino or not persona_destino:
            flash('No se pudo encontrar el destino para devolver el documento rechazado.', 'danger')
            return redirect(url_for('documentos.detalle', id=documento.id))

        # Obtener el estado "Rechazado" (si existe) o "Recepcionado" (como fallback)
        estado_rechazado = EstadoDocumento.query.filter_by(nombre='Rechazado').first()
        if not estado_rechazado:
            estado_rechazado = EstadoDocumento.query.filter_by(nombre='Recepcionado').first()

        # Transferir el documento
        documento.transferir(
            usuario_origen=current_user,
            area_destino=area_destino,
            persona_destino=persona_destino,
            estado_nuevo=estado_rechazado,
            observaciones=f'Documento rechazado por {current_user.persona.nombre_completo}. Motivo: {motivo_rechazo}'
        )

        # Notificar al usuario destino
        if usuario_destino:
            crear_notificacion(
                usuario_id=usuario_destino.id,
                titulo=f'Documento rechazado - {documento.radicado}',
                mensaje=f'El documento ha sido rechazado por {current_user.persona.nombre_completo}. Motivo: {motivo_rechazo}',
                documento_id=documento.id
            )

        # También notificar al transferidor si es diferente del usuario destino
        if usuario_transferidor and (not usuario_destino or usuario_transferidor.id != usuario_destino.id):
            crear_notificacion(
                usuario_id=usuario_transferidor.id,
                titulo=f'Documento rechazado - {documento.radicado}',
                mensaje=f'El documento ha sido rechazado por {current_user.persona.nombre_completo}. Motivo: {motivo_rechazo}',
                documento_id=documento.id
            )

        flash('Documento rechazado exitosamente.', 'success')
        return redirect(url_for('dashboard.index'))

    # Si es GET, mostrar el formulario de rechazo
    return render_template('documentos/rechazar.html', documento=documento)


@documentos_bp.route('/finalizar/<int:id>')
@login_required
@document_access_required
@permission_required('Transferir documento')
def finalizar(id):
    """Vista para finalizar un documento"""
    documento = Documento.query.get_or_404(id)
    
    # Obtener el estado "Finalizado"
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    
    # Si no existe el estado, mostrar error
    if not estado_finalizado:
        flash('No se puede finalizar el documento porque no existe el estado "Finalizado".', 'danger')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Transferir el documento al mismo usuario pero cambiar el estado
    documento.transferir(
        usuario_origen=current_user,
        area_destino=documento.area_destino,
        persona_destino=documento.persona_destino,
        estado_nuevo=estado_finalizado,
        observaciones='Documento finalizado'
    )
    
    # MEJORA: Enviar notificaciones a todos los involucrados
    # Notificar al registrador original si es diferente del usuario actual
    if documento.registrado_por_id and documento.registrado_por_id != current_user.id:
        crear_notificacion(
            usuario_id=documento.registrado_por_id,
            titulo=f'Documento finalizado - {documento.radicado}',
            mensaje=f'El documento ha sido finalizado por {current_user.persona.nombre_completo}.',
            documento_id=documento.id
        )
    
    # Notificar al último transferidor si es diferente del usuario actual y del registrador
    if documento.ultimo_transferido_por_id and documento.ultimo_transferido_por_id != current_user.id and documento.ultimo_transferido_por_id != documento.registrado_por_id:
        crear_notificacion(
            usuario_id=documento.ultimo_transferido_por_id,
            titulo=f'Documento finalizado - {documento.radicado}',
            mensaje=f'El documento ha sido finalizado por {current_user.persona.nombre_completo}.',
            documento_id=documento.id
        )
    
    flash('Documento finalizado exitosamente.', 'success')
    return redirect(url_for('documentos.detalle', id=documento.id))


@documentos_bp.route('/archivar/<int:id>')
@login_required
@document_access_required
@permission_required('Transferir documento')
def archivar(id):
    """Vista para archivar un documento"""
    documento = Documento.query.get_or_404(id)
    
    # Verificar que el documento esté en estado Finalizado
    estado_finalizado = EstadoDocumento.query.filter_by(nombre='Finalizado').first()
    if documento.estado_actual_id != estado_finalizado.id:
        flash('Solo se pueden archivar documentos que estén en estado "Finalizado".', 'danger')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Obtener el estado "Archivado"
    estado_archivado = EstadoDocumento.query.filter_by(nombre='Archivado').first()
    
    # Si no existe el estado, mostrar error
    if not estado_archivado:
        flash('No se puede archivar el documento porque no existe el estado "Archivado".', 'danger')
        return redirect(url_for('documentos.detalle', id=documento.id))
    
    # Transferir el documento al mismo usuario pero cambiar el estado
    documento.transferir(
        usuario_origen=current_user,
        area_destino=documento.area_destino,
        persona_destino=documento.persona_destino,
        estado_nuevo=estado_archivado,
        observaciones='Documento archivado'
    )
    
    # MEJORA: Enviar notificaciones a todos los involucrados
    # Notificar al registrador original si es diferente del usuario actual
    if documento.registrado_por_id and documento.registrado_por_id != current_user.id:
        crear_notificacion(
            usuario_id=documento.registrado_por_id,
            titulo=f'Documento archivado - {documento.radicado}',
            mensaje=f'El documento ha sido archivado por {current_user.persona.nombre_completo}.',
            documento_id=documento.id
        )
    
    # Notificar al último transferidor si es diferente del usuario actual y del registrador
    if documento.ultimo_transferido_por_id and documento.ultimo_transferido_por_id != current_user.id and documento.ultimo_transferido_por_id != documento.registrado_por_id:
        crear_notificacion(
            usuario_id=documento.ultimo_transferido_por_id,
            titulo=f'Documento archivado - {documento.radicado}',
            mensaje=f'El documento ha sido archivado por {current_user.persona.nombre_completo}.',
            documento_id=documento.id
        )
    
    flash('Documento archivado exitosamente.', 'success')
    return redirect(url_for('documentos.detalle', id=documento.id))


@documentos_bp.route('/buscar', methods=['GET', 'POST'])
@login_required
def buscar():
    """Vista para buscar documentos"""
    form = BuscarDocumentoForm()
    documentos = []

    # Obtener parámetros de paginación
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Manejar estado_id que podría ser una lista separada por comas
    estado_id = request.args.get('estado_id')
    estados_ids = []

    if request.method == 'GET' and estado_id:
        if ',' in estado_id:
            form.estado_id.data = '0'  # Mostrar "Todos" en la interfaz
            estados_ids = [int(id) for id in estado_id.split(',') if id.isdigit()]
        elif estado_id.isdigit():
            form.estado_id.data = estado_id

    # Determinar si es una búsqueda
    is_search = request.args.get('buscar') or any(
        key for key in request.args.keys() if key not in ['page', 'per_page'] and request.args.get(key)
    ) or form.validate_on_submit()

    if is_search:
        # Construir la consulta base
        query = Documento.query

        # Aplicar filtros
        if form.radicado.data:
            query = query.filter(Documento.radicado.like(f'%{form.radicado.data}%'))
        elif request.args.get('radicado'):
            query = query.filter(Documento.radicado.like(f'%{request.args.get("radicado")}%'))

        if form.fecha_desde.data:
            query = query.filter(Documento.fecha_recepcion >= form.fecha_desde.data)
        elif request.args.get('fecha_desde'):
            try:
                fecha_desde = datetime.strptime(request.args.get('fecha_desde'), '%Y-%m-%d')
                query = query.filter(Documento.fecha_recepcion >= fecha_desde)
            except ValueError:
                pass

        if form.fecha_hasta.data:
            fecha_hasta = datetime.combine(form.fecha_hasta.data, datetime.max.time())
            query = query.filter(Documento.fecha_recepcion <= fecha_hasta)
        elif request.args.get('fecha_hasta'):
            try:
                fecha_hasta = datetime.strptime(request.args.get('fecha_hasta'), '%Y-%m-%d')
                fecha_hasta = datetime.combine(fecha_hasta.date(), datetime.max.time())
                query = query.filter(Documento.fecha_recepcion <= fecha_hasta)
            except ValueError:
                pass

        # Filtrar por estado_id múltiple o único
        if estados_ids:
            query = query.filter(Documento.estado_actual_id.in_(estados_ids))
        elif form.estado_id.data and int(form.estado_id.data) > 0:
            query = query.filter_by(estado_actual_id=form.estado_id.data)
        elif request.args.get('estado_id') and request.args.get('estado_id') != '0':
            query = query.filter_by(estado_actual_id=request.args.get('estado_id'))

        if form.transportadora_id.data and int(form.transportadora_id.data) > 0:
            query = query.filter_by(transportadora_id=form.transportadora_id.data)
        elif request.args.get('transportadora_id') and int(request.args.get('transportadora_id')) > 0:
            query = query.filter_by(transportadora_id=request.args.get('transportadora_id'))

        if form.tipo_documento_id.data and int(form.tipo_documento_id.data) > 0:
            query = query.filter_by(tipo_documento_id=form.tipo_documento_id.data)
        elif request.args.get('tipo_documento_id') and int(request.args.get('tipo_documento_id')) > 0:
            query = query.filter_by(tipo_documento_id=request.args.get('tipo_documento_id'))

        if form.tipo.data:
            query = query.filter_by(tipo=form.tipo.data)
        elif request.args.get('tipo'):
            query = query.filter_by(tipo=request.args.get('tipo'))

        if form.remitente.data:
            query = query.filter(Documento.remitente.like(f'%{form.remitente.data}%'))
        elif request.args.get('remitente'):
            query = query.filter(Documento.remitente.like(f'%{request.args.get("remitente")}%'))

        # Filtrar según el rol del usuario
        if current_user.rol.nombre == 'Superadministrador':
            pass  # Ve todos los documentos
        elif current_user.rol.nombre == 'Recepción':
            query = query.filter_by(registrado_por_id=current_user.id)
        else:
            query = query.filter(
                or_(
                    Documento.area_destino_id == current_user.persona.area_id,
                    Documento.persona_destino_id == current_user.persona_id,
                    Documento.ultimo_transferido_por_id == current_user.id  # Incluir documentos transferidos por el usuario
                )
            )

        # Ordenar por fecha de creación (más recientes primero)
        query = query.order_by(Documento.creado_en.desc())

        # Paginar los resultados
        pagination = Pagination(query, page, per_page, 'documentos.buscar')
        documentos = pagination.items

        # Mantener valores en el formulario si es una búsqueda GET
        if request.method == 'GET' and is_search:
            for key, value in request.args.items():
                if key in form._fields:
                    field = getattr(form, key)
                    if hasattr(field, 'data'):
                        try:
                            if key in ['fecha_desde', 'fecha_hasta'] and value:
                                field.data = datetime.strptime(value, '%Y-%m-%d')
                            else:
                                field.data = value
                        except:
                            pass

        return render_template('documentos/buscar.html',
                               form=form,
                               documentos=documentos,
                               pagination=pagination,
                               is_search=True)

    return render_template('documentos/buscar.html',
                           form=form,
                           documentos=[],
                           pagination=None,
                           is_search=False)@documentos_bp.route('/get_personas/<int:area_id>')


@documentos_bp.route('/get_personas/<int:area_id>')
@login_required
def get_personas(area_id):
    """API para obtener las personas de un área específica"""
    try:
        personas = Persona.query.filter_by(area_id=area_id, activo=True).order_by(Persona.nombres_apellidos).all()
        personas_json = [{'id': p.id, 'nombre': p.nombre_completo} for p in personas]
        return jsonify(personas_json)
    except Exception as e:
        # Registrar el error
        print(f"Error al obtener personas del área {area_id}: {str(e)}")
        return jsonify([]), 500

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
