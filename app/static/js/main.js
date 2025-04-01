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

// Función para manejar el cambio dinámico del selector de personas según el área
function setupDynamicPersonaSelector() {
    const areaSelect = document.getElementById('area_destino_id');
    const personaSelect = document.getElementById('persona_destino_id');
    
    if (areaSelect && personaSelect) {
        areaSelect.addEventListener('change', function() {
            const areaId = this.value;
            if (areaId) {
                fetch(`/documentos/get_personas/${areaId}`)
                    .then(response => response.json())
                    .then(data => {
                        // Limpiar select actual
                        personaSelect.innerHTML = '';
                        
                        // Agregar nuevas opciones
                        data.forEach(persona => {
                            const option = document.createElement('option');
                            option.value = persona.id;
                            option.textContent = persona.nombre;
                            personaSelect.appendChild(option);
                        });
                    })
                    .catch(error => console.error('Error al cargar personas:', error));
            }
        });
    }
}

// Inicializar todas las funciones cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function() {
    initTooltips();
    setupConfirmations();
    setupAutoCloseAlerts();
    setupDynamicPersonaSelector();
});

// Función para actualizar los contadores del dashboard si están presentes en la página
function actualizarContadoresDashboard() {
    // Verificar si estamos en la página del dashboard
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

// Agregar al DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
    initTooltips();
    setupConfirmations();
    setupAutoCloseAlerts();
    setupDynamicPersonaSelector();
    
    // Configurar actualización periódica de contadores si estamos en el dashboard
    if (document.getElementById('contador-pendientes')) {
        setInterval(actualizarContadoresDashboard, 30000); // Cada 30 segundos
    }
});