var anotaciones = document.getElementById('anotaciones');
var calificacion = document.getElementById('calificacion');

//Verificación previa al envio
function enviar() {
    if (anotaciones.value === null || anotaciones.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (calificacion.value === null || calificacion.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else {
        return true;
    }
};

//Motrar mensajes de información
var isInfoShown = false;

function info() {
    if (!isInfoShown) {
        Swal.fire({
            title: 'Atencion!',
            text: "La calificación debe de ser: Bueno, Regular, Muy bueno, Incumple",
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

//Función de validación de entrada de solo letras
function validateInput(event) {
    const input = event.target;
    const regex = /^[a-zA-Z]+$/; // Expresión regular para aceptar solo letras

    if (!regex.test(input.value)) {
        input.value = input.value.replace(/[^a-zA-Z]/g, ''); // Eliminar caracteres no permitidos
    }
}