/**
 * Funciones para manejar alertas con SweetAlert2
 */

// Configuración para confirmar eliminación
function confirmarEliminacion(url, mensaje) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: mensaje || "Esta acción no se puede deshacer.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#dc3545",
        cancelButtonColor: "#6c757d",
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = url;
        }
    });
    return false;
}

// Configuración para mensajes de éxito
function mensajeExito(mensaje) {
    Swal.fire({
        title: "¡Éxito!",
        text: mensaje,
        icon: "success",
        confirmButtonColor: "#28a745",
        timer: 3000
    });
}

// Configuración para mensajes de error
function mensajeError(mensaje) {
    Swal.fire({
        title: "Error",
        text: mensaje,
        icon: "error",
        confirmButtonColor: "#dc3545"
    });
}

// Configuración para mensajes de advertencia
function mensajeAdvertencia(mensaje) {
    Swal.fire({
        title: "Advertencia",
        text: mensaje,
        icon: "warning",
        confirmButtonColor: "#ffc107"
    });
}

// Configuración para mensajes informativos
function mensajeInfo(mensaje) {
    Swal.fire({
        title: "Información",
        text: mensaje,
        icon: "info",
        confirmButtonColor: "#17a2b8"
    });
}

// Función para mostrar mensajes flash con SweetAlert2
function mostrarMensajesFlash(tipo, mensaje) {
    switch (tipo) {
        case 'success':
            mensajeExito(mensaje);
            break;
        case 'danger':
        case 'error':
            mensajeError(mensaje);
            break;
        case 'warning':
            mensajeAdvertencia(mensaje);
            break;
        case 'info':
            mensajeInfo(mensaje);
            break;
        default:
            Swal.fire(mensaje);
    }
}

// Mostrar loading
function mostrarLoading(mensaje = 'Procesando...') {
    Swal.fire({
        title: mensaje,
        allowOutsideClick: false,
        showConfirmButton: false,
        willOpen: () => {
            Swal.showLoading();
        }
    });
}

// Cerrar alerta actual
function cerrarAlerta() {
    Swal.close();
}

// Confirmar acción (para cualquier acción que requiera confirmación)
function confirmarAccion(url, mensaje, titulo = "¿Estás seguro?", textoConfirmar = "Sí, continuar") {
    Swal.fire({
        title: titulo,
        text: mensaje,
        icon: "question",
        showCancelButton: true,
        confirmButtonColor: "#1D2C96",
        cancelButtonColor: "#6c757d",
        confirmButtonText: textoConfirmar,
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = url;
        }
    });
    return false;
}

// Capitaliza la primera letra de un texto
function capitalizarPrimeraLetra(texto) {
    return texto.charAt(0).toUpperCase() + texto.slice(1);
}

// Muestra un formulario de entrada
function mostrarEntrada(titulo, texto, placeholder, callback) {
    Swal.fire({
        title: titulo,
        text: texto,
        input: 'text',
        inputPlaceholder: placeholder,
        showCancelButton: true,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#1D2C96',
        cancelButtonColor: '#6c757d',
    }).then((result) => {
        if (result.isConfirmed && typeof callback === 'function') {
            callback(result.value);
        }
    });
}

// Versión más completa de confirmarAccion que permite callback en lugar de redirección
function confirmarAccionCallback(mensaje, callback, titulo = "¿Estás seguro?", textoConfirmar = "Sí, continuar") {
    Swal.fire({
        title: titulo,
        text: mensaje,
        icon: "question",
        showCancelButton: true,
        confirmButtonColor: "#1D2C96",
        cancelButtonColor: "#6c757d",
        confirmButtonText: textoConfirmar,
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed && typeof callback === 'function') {
            callback();
        }
    });
    return false;
}

// Mostrar notificación tipo toast (más sutil y menos intrusiva)
function mostrarToast(mensaje, tipo = 'success', duracion = 3000) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: duracion,
        timerProgressBar: true
    });
    
    Toast.fire({
        icon: tipo,
        title: mensaje
    });
}