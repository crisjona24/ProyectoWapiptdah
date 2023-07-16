function actualizarRuta() {
    var select = document.getElementById("actividad");
    var valorSeleccionado = select.value;

    // Actualizar la ruta del formulario según el valor seleccionado
    if (valorSeleccionado === "UsuarioComun") {
      document.getElementById("myForm").action = "/registrarComun/";
    } else if (valorSeleccionado === "UsuarioTecnico") {
      document.getElementById("myForm").action = "/registrarTecnico/";
    } else if (valorSeleccionado === "Paciente") {
      document.getElementById("myForm").action = "/registrarPaciente/";
    }
  }