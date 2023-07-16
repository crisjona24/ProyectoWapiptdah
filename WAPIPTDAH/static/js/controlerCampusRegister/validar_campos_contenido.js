var nombre = document.getElementById('nombre');
var contenido = document.getElementById('contenido');
var descripcion = document.getElementById('descripcion');
var dominio = document.getElementById('dominio');

function enviar() {
    if (nombre.value === null || nombre.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (contenido.value === null || contenido.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (descripcion.value === null || descripcion.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (dominio.value === null || dominio.value === '') {
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
        text: "Ingresa una descripción corta para el contenido",
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