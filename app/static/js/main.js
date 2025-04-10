/**
 * Script principal para SGDI - Sistema de Gestión Documental Interna
 */

// Función para inicializar tooltips de Bootstrap
function initTooltips() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Función para añadir confirmación a enlaces o botones con data-confirm
function setupConfirmations() {
    document.querySelectorAll('[data-confirm]').forEach(function(element) {
        element.addEventListener('click', function(event) {
            if (!confirm(this.getAttribute('data-confirm'))) {
                event.preventDefault();
            }
        });
    });
}

// Función para manejar el cierre automático de alertas
function setupAutoCloseAlerts() {
    const alerts = document.querySelectorAll('.alert:not(.alert-danger):not(.alert-warning)');
    
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const closeButton = alert.querySelector('.btn-close');
            if (closeButton) {
                closeButton.click();
            }
        }, 5000); // Cerrar automáticamente después de 5 segundos
    });
}

// Función para cargar personas de un área (usando jQuery)
function cargarPersonasArea() {
    var areaId = $('#area_destino_id').val();
    if (!areaId) {
        // Si no hay área seleccionada, limpiar y deshabilitar el selector de personas
        $("#persona_destino_id").html('<option value="">Seleccione persona</option>');
        $("#persona_destino_id").prop('disabled', true);
        return;
    }

    // Habilitar el selector de personas
    $("#persona_destino_id").prop('disabled', false);

    // Cargar personas del área seleccionada
    $.ajax({
        url: "/documentos/get_personas/" + areaId,
        type: "GET",
        dataType: "json",
        cache: false,
        success: function(data) {
            var options = '<option value="">Seleccione persona</option>';
            $.each(data, function(index, persona) {
                options += '<option value="' + persona.id + '">' + persona.nombre + '</option>';
            });
            $("#persona_destino_id").html(options);
        },
        error: function(xhr, status, error) {
            console.error("Error al cargar personas:", error);
            $("#persona_destino_id").html('<option value="">Error al cargar personas</option>');
        }
    });
}

// Función para actualizar los contadores del dashboard si están presentes en la página
function actualizarContadoresDashboard() {
    const contadorPendientes = document.getElementById('contador-pendientes');
    const contadorFinalizados = document.getElementById('contador-finalizados');

    if (contadorPendientes && contadorFinalizados) {
        fetch('/contador-documentos')
            .then(response => response.json())
            .then(data => {
                contadorPendientes.textContent = data.documentos_pendientes;
                contadorFinalizados.textContent = data.documentos_finalizados;
            })
            .catch(error => console.error('Error al actualizar contadores:', error));
    }
}

// Inicializar cuando el DOM esté listo
$(document).ready(function() {
    // Tooltips, confirmaciones, alertas
    initTooltips();
    setupConfirmations();
    setupAutoCloseAlerts();

    // Selector dinámico de personas según área
    $("#area_destino_id").on('change', cargarPersonasArea);

    // Si ya hay un área seleccionada al cargar, traer sus personas
    if ($("#area_destino_id").length > 0 && $("#area_destino_id").val()) {
        cargarPersonasArea();
    }

    // Actualización periódica de contadores si estamos en dashboard
    if ($('#contador-pendientes').length > 0) {
        setInterval(actualizarContadoresDashboard, 30000); // Cada 30 segundos
    }
});
