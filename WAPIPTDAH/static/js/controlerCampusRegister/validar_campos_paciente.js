var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var correo = document.getElementById('email');
var fecha = document.getElementById('fecha');
var celular = document.getElementById('celular');
var direccion = document.getElementById('direccion');
var clave = document.getElementById('password');
var username = document.getElementById('username');

var antecedente = document.getElementById('antecedente');
var contacto = document.getElementById('contacto');

function enviar() {
    if (nombre.value === null || nombre.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (apellido.value === null || apellido.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (correo.value === null || correo.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (celular.value === null || celular.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (direccion.value === null || direccion.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (fecha.value === null || fecha.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (username.value === null || username.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (clave.value === null || clave.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (antecedente.value === null || antecedente.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (contacto.value === null || contacto.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else {
        return true;
    }
};

// Función para controlar la entrada de solo números
function soloNumeros(event) {
    var charCode = event.keyCode;
    if (charCode < 48 || charCode > 57) {
        return false;
    }
}

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


