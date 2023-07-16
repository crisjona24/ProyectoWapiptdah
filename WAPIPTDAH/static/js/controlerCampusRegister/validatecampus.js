var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var correo = document.getElementById('correo');
var fecha = document.getElementById('fecha');
var celular = document.getElementById('celular');
var cedula = document.getElementById('cedula');
var direccion = document.getElementById('direccion');
var actividad = document.getElementById('actividad');

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
    } else if (fecha.value === null || fecha.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (celular.value === null || celular.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (cedula.value === null || cedula.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (direccion.value === null || direccion.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else if (actividad.value === null || actividad.value === '') {
        Swal.fire('Campos restantes!');
        return false;
    } else {
        return true;
    }
};