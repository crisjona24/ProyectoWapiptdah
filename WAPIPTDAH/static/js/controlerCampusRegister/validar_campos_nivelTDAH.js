var nombre = document.getElementById('nombre');
var numcat = document.getElementById('numcat');
var descripcion = document.getElementById('descripcion');
var grado = document.getElementById('grado');

function enviar() {
    if (nombre.value === null || nombre.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (numcat.value === null || numcat.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (descripcion.value === null || descripcion.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (grado.value === null || grado.value === '') {
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
        text: "Ingresa una descripción corta",
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