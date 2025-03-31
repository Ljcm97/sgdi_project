/**
 * Script principal para el módulo de reportes
 */

// Variables globales para charts
let chartPrincipal = null;
let chartsTendencia = {};
let chartsDistribucion = {};

// Inicializar cuando el documento esté listo
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar selectores de fecha
    inicializarDatepickers();
    
    // Inicializar gráficos si existen contenedores
    inicializarGraficos();
    
    // Configurar filtros
    configurarFiltros();
    
    // Configurar botones de exportación
    configurarExportacion();
});

/**
 * Inicializa los selectores de fecha
 */
function inicializarDatepickers() {
    const fechaInputs = document.querySelectorAll('.fecha-input');
    
    if (fechaInputs.length > 0) {
        fechaInputs.forEach(input => {
            if (typeof flatpickr !== 'undefined') {
                flatpickr(input, {
                    dateFormat: "Y-m-d",
                    locale: "es"
                });
            }
        });
    }
}

/**
 * Inicializa los gráficos principales si existen los contenedores
 */
function inicializarGraficos() {
    // Gráfico principal del dashboard
    const dashboardChart = document.getElementById('dashboardChart');
    if (dashboardChart) {
        inicializarDashboardChart(dashboardChart);
    }
    
    // Gráficos de área
    const areaCharts = document.querySelectorAll('.area-chart');
    if (areaCharts.length > 0) {
        areaCharts.forEach(chart => {
            inicializarAreaChart(chart);
        });
    }
    
    // Gráficos de estado
    const estadoCharts = document.querySelectorAll('.estado-chart');
    if (estadoCharts.length > 0) {
        estadoCharts.forEach(chart => {
            inicializarEstadoChart(chart);
        });
    }
    
    // Gráficos de tiempo
    const tiempoCharts = document.querySelectorAll('.tiempo-chart');
    if (tiempoCharts.length > 0) {
        tiempoCharts.forEach(chart => {
            inicializarTiempoChart(chart);
        });
    }
    
    // Gráficos de tendencias
    const tendenciaCharts = document.querySelectorAll('.tendencia-chart');
    if (tendenciaCharts.length > 0) {
        tendenciaCharts.forEach(chart => {
            inicializarTendenciaChart(chart);
        });
    }
}

/**
 * Inicializa el gráfico principal del dashboard
 */
function inicializarDashboardChart(container) {
    // Obtener datos del atributo data
    const dataAttr = container.getAttribute('data-stats');
    let datos;
    
    try {
        datos = JSON.parse(dataAttr);
    } catch (e) {
        console.error('Error al parsear datos del gráfico:', e);
        return;
    }
    
    if (!datos) return;
    
    // Crear el gráfico
    const ctx = container.getContext('2d');
    chartPrincipal = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: datos.map(d => d.estado),
            datasets: [{
                data: datos.map(d => d.cantidad),
                backgroundColor: datos.map(d => d.color),
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                },
                title: {
                    display: true,
                    text: 'Distribución de Documentos por Estado'
                }
            }
        }
    });
}

/**
 * Inicializa un gráfico de área
 */
function inicializarAreaChart(container) {
    // Obtener ID del área
    const areaId = container.getAttribute('data-area-id');
    const dataAttr = container.getAttribute('data-stats');
    let datos;
    
    try {
        datos = JSON.parse(dataAttr);
    } catch (e) {
        console.error('Error al parsear datos del gráfico:', e);
        return;
    }
    
    if (!datos) return;
    
    // Crear el gráfico
    const ctx = container.getContext('2d');
    chartsDistribucion[`area_${areaId}`] = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: datos.map(d => d.estado),
            datasets: [{
                data: datos.map(d => d.cantidad),
                backgroundColor: datos.map(d => d.color),
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                },
                title: {
                    display: true,
                    text: 'Distribución por Estado'
                }
            }
        }
    });
}

/**
 * Inicializa un gráfico de estado
 */
function inicializarEstadoChart(container) {
    // Obtener ID del estado
    const estadoId = container.getAttribute('data-estado-id');
    const dataAttr = container.getAttribute('data-stats');
    let datos;
    
    try {
        datos = JSON.parse(dataAttr);
    } catch (e) {
        console.error('Error al parsear datos del gráfico:', e);
        return;
    }
    
    if (!datos) return;
    
    // Crear el gráfico
    const ctx = container.getContext('2d');
    chartsDistribucion[`estado_${estadoId}`] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: datos.map(d => d.area),
            datasets: [{
                label: 'Cantidad de documentos',
                data: datos.map(d => d.cantidad),
                backgroundColor: datos.map(d => d.color || '#1D2C96'),
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Distribución por Área'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}

/**
 * Inicializa un gráfico de tiempo
 */
function inicializarTiempoChart(container) {
    // Obtener datos del atributo data
    const dataAttr = container.getAttribute('data-stats');
    let datos;
    
    try {
        datos = JSON.parse(dataAttr);
    } catch (e) {
        console.error('Error al parsear datos del gráfico:', e);
        return;
    }
    
    if (!datos) return;
    
    // Crear el gráfico
    const ctx = container.getContext('2d');
    chartsTendencia['tiempo'] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: datos.map(d => d.rango),
            datasets: [{
                label: 'Cantidad de documentos',
                data: datos.map(d => d.cantidad),
                backgroundColor: [
                    '#28a745',  // Verde para menos de 1 día
                    '#17a2b8',  // Azul para 1-3 días
                    '#ffc107',  // Amarillo para 3-7 días
                    '#dc3545'   // Rojo para más de 7 días
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Distribución por Tiempo de Procesamiento'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}

/**
 * Inicializa un gráfico de tendencias
 */
function inicializarTendenciaChart(container) {
    // Obtener tipo de tendencia
    const tipoTendencia = container.getAttribute('data-tendencia-tipo');
    const dataAttr = container.getAttribute('data-stats');
    let datos;
    
    try {
        datos = JSON.parse(dataAttr);
    } catch (e) {
        console.error('Error al parsear datos del gráfico:', e);
        return;
    }
    
    if (!datos) return;
    
    // Crear el gráfico
    const ctx = container.getContext('2d');
    chartsTendencia[tipoTendencia] = new Chart(ctx, {
        type: 'line',
        data: {
            labels: datos.map(d => d.periodo),
            datasets: [
                {
                    label: 'Documentos Recibidos',
                    data: datos.map(d => d.docs_recibidos),
                    borderColor: '#1D2C96',
                    backgroundColor: 'rgba(29, 44, 150, 0.1)',
                    borderWidth: 2,
                    fill: true
                },
                {
                    label: 'Documentos Finalizados',
                    data: datos.map(d => d.docs_finalizados),
                    borderColor: '#28a745',
                    backgroundColor: 'rgba(40, 167, 69, 0.1)',
                    borderWidth: 2,
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Tendencia de Documentos'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}


function configurarFiltros() {
    // Formulario de filtros
    const formFiltros = document.getElementById('filtros-form');
    
    if (formFiltros) {
        // Botón de limpiar filtros
        const btnLimpiar = document.getElementById('btn-limpiar-filtros');
        if (btnLimpiar) {
            btnLimpiar.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Limpiar los campos del formulario
                const inputs = formFiltros.querySelectorAll('input, select');
                inputs.forEach(input => {
                    if (input.type === 'checkbox') {
                        input.checked = false;
                    } else if (input.type === 'radio') {
                        // Para radio buttons, seleccionar el primero o el valor por defecto
                        if (input.value === '' || input.value === '0' || input.value === 'todos') {
                            input.checked = true;
                        } else {
                            input.checked = false;
                        }
                    } else if (input.type !== 'submit' && input.type !== 'button') {
                        input.value = '';
                    }
                });
                
                // Enviar el formulario
                formFiltros.submit();
            });
        }
    }
}

/**
 * Configurar los botones de exportación
 */
function configurarExportacion() {
    // Botones de exportación
    const btnExportar = document.querySelectorAll('.btn-exportar');
    
    if (btnExportar.length > 0) {
        btnExportar.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Obtener formato y tipo de reporte
                const formato = this.getAttribute('data-formato');
                const tipoReporte = this.getAttribute('data-reporte');
                
                if (formato && tipoReporte) {
                    // Construir URL
                    let url = `/reportes/exportar/${formato}?tipo=${tipoReporte}`;
                    
                    // Obtener filtros activos
                    const formFiltros = document.getElementById('filtros-form');
                    if (formFiltros) {
                        const formData = new FormData(formFiltros);
                        const filtros = Array.from(formData.entries())
                            .filter(entry => entry[1]) // Eliminar valores vacíos
                            .map(entry => `${entry[0]}=${encodeURIComponent(entry[1])}`)
                            .join('&');
                        
                        if (filtros) {
                            url += `&${filtros}`;
                        }
                    }
                    
                    // Redirigir a URL de exportación
                    window.location.href = url;
                }
            });
        });
    }
}