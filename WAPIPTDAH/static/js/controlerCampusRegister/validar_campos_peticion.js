var motivo = document.getElementById('motivo');
var peticion = document.getElementById('peticion');

function enviar() {
    if (motivo.value === null || motivo.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (peticion.value === null || peticion.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else {
        return true;
    }
};

var isInfoShown = false;

function info() {
    if (!isInfoShown) {
        Swal.fire({
            title: 'Atencion!',
            text: "Ingresa el motivo de esta petición puede ser específico y entendible",
            icon: 'info',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Lo entiendo!'
        });
        isInfoShown = true;
    }
};

// Funcion para verificar si el elemento existe y establecer tiempo de duración en milisegundos
var errorSpan = document.getElementById('error-span');
var duration = 3000; // 3 segundos
if (errorSpan) {
    // Agregar clase para mostrar el span
    errorSpan.classList.add('show');
    // Después de la duración especificada, eliminar la clase para ocultar el span
    setTimeout(function () {
        errorSpan.classList.remove('show');
    }, duration);
}