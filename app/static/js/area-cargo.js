/**
 * Funcionalidad para cargar cargos según el área seleccionada
 */
document.addEventListener('DOMContentLoaded', function() {
    // Capturar selectores
    const areaSelect = document.getElementById('area_id');
    const cargoSelect = document.getElementById('cargo_id');
    
    // Si ambos elementos existen en la página
    if (areaSelect && cargoSelect) {
        // Guardar todos los cargos iniciales para usarlos luego
        const allCargos = Array.from(cargoSelect.options).map(option => {
            return {
                id: option.value,
                nombre: option.text,
                selected: option.selected
            };
        });
        
        // Función para cargar los cargos según el área
        function cargarCargosPorArea(areaId, cargoSeleccionado = null) {
            // Primero, limpiar el select de cargos
            cargoSelect.innerHTML = '';
            
            // Si no hay área seleccionada
            if (!areaId) {
                cargoSelect.innerHTML = '<option value="">Seleccione cargo</option>';
                return;
            }
            
            // Obtener cargos para esta área mediante AJAX
            fetch(`/personas/get_cargos_por_area/${areaId}`)
                .then(response => response.json())
                .then(data => {
                    // Opción por defecto
                    let options = '<option value="">Seleccione cargo</option>';
                    
                    // Ordenar alfabéticamente
                    data.sort((a, b) => a.nombre.localeCompare(b.nombre));
                    
                    // Agregar cada cargo
                    data.forEach(cargo => {
                        const selected = (cargoSeleccionado && cargo.id == cargoSeleccionado) ? 'selected' : '';
                        options += `<option value="${cargo.id}" ${selected}>${cargo.nombre}</option>`;
                    });
                    
                    // Actualizar el select
                    cargoSelect.innerHTML = options;
                })
                .catch(error => {
                    console.error('Error al cargar cargos:', error);
                    // En caso de error, mostrar todos los cargos
                    cargarTodosLosCargos();
                });
        }
        
        // Función para cargar todos los cargos (fallback)
        function cargarTodosLosCargos() {
            cargoSelect.innerHTML = '<option value="">Seleccione cargo</option>';
            allCargos.forEach(cargo => {
                if (cargo.id) {
                    const selected = cargo.selected ? 'selected' : '';
                    cargoSelect.innerHTML += `<option value="${cargo.id}" ${selected}>${cargo.nombre}</option>`;
                }
            });
        }
        
        // Evento de cambio en el área
        areaSelect.addEventListener('change', function() {
            cargarCargosPorArea(this.value);
        });
        
        // Cargar cargos iniciales si hay un área seleccionada
        if (areaSelect.value) {
            // Obtener el cargo seleccionado inicialmente, si existe
            const cargoSeleccionado = cargoSelect.value;
            cargarCargosPorArea(areaSelect.value, cargoSeleccionado);
        }
    }
});