// Función para controlar la entrada de solo números
function soloNumeros(event) {
    var charCode = event.keyCode;
    if (charCode < 48 || charCode > 57) {
        return false;
    }
}