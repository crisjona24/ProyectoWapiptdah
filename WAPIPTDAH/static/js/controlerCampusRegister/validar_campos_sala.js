var anota = document.getElementById('indicaciones');

//Verificación previa al envio
function enviar() {
    if (anota.value === null || anota.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else {
        return true;
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
