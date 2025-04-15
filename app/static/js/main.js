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
        $("#persona_destino_id").html('<option value="">Seleccione persona</option>');
        $("#persona_destino_id").prop('disabled', true);
        return;
    }

    $("#persona_destino_id").prop('disabled', false);

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

// Inicializar Select2 para todos los selectores
function inicializarSelect2() {
    $('select.form-select').select2({
        placeholder: "Seleccione una opción",
        allowClear: true,
        width: '100%',
        language: {
            noResults: function() {
                return "No se encontraron resultados";
            },
            searching: function() {
                return "Buscando...";
            }
        }
    });
}

// Validar formulario antes de enviar
function validarFormulario(form) {
    let esValido = true;
    let primerInvalido = null;

    // Validar inputs requeridos
    $(form).find('input, select, textarea').each(function() {
        const esRequerido = $(this).prop('required');
        const tipo = $(this).attr('type');
        const valor = $(this).val();

        if (esRequerido && (!valor || valor === "")) {
            $(this).addClass('is-invalid');
            if (!primerInvalido) primerInvalido = this;
            esValido = false;
        } else {
            $(this).removeClass('is-invalid');
        }
    });

    // Validar campos Select2 que son requeridos
    $(form).find('select.form-select[required]').each(function() {
        const valor = $(this).val();
        const $select2Container = $(this).next('.select2-container');

        if (!valor || valor === "") {
            $select2Container.addClass('is-invalid');
            if (!primerInvalido) primerInvalido = this;
            esValido = false;
        } else {
            $select2Container.removeClass('is-invalid');
        }
    });

    if (!esValido && primerInvalido) {
        primerInvalido.focus();
    }

    return esValido;
}

// Asegurarse de que Select2 sincronice sus valores antes de enviar el formulario
$('form').on('submit', function(e) {
    const form = this;

    // Sincronizar select2
    $(form).find('select.form-select').each(function() {
        const val = $(this).val();
        $(this).val(val).trigger('change');
    });

    // Validar antes de enviar
    if (!validarFormulario(form)) {
        e.preventDefault();
        e.stopPropagation();
    }
});

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

    // Inicializar Select2
    inicializarSelect2();
});

// Reinicializar Select2 después de mostrar modales o acordeones
$('.accordion-button, [data-bs-toggle="modal"]').on('click', function() {
    setTimeout(function() {
        inicializarSelect2();
    }, 200);
});

// Asegurarse de que Select2 se ajuste al tamaño del contenedor en resize
$(window).on('resize', function() {
    $('select.form-select').each(function() {
        $(this).select2({
            placeholder: "Seleccione una opción",
            allowClear: true,
            width: '100%'
        });
    });
});

// Inicializar todos los selectores después de cargar la página (extra por seguridad)
$(document).ready(function() {
    // Pequeña pausa para asegurarse de que todo está listo
    setTimeout(function() {
        $('select.form-select').select2({
            placeholder: "Seleccione una opción",
            allowClear: true,
            width: '100%'
        });
    }, 100);
});
