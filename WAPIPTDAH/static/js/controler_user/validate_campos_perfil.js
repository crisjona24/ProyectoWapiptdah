function validar_eliminacion_paciente() {
    Swal.fire({
        title: '¿Seguro de eliminar el perfil?',
        text: 'Estás a punto de eliminar el perfil',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Eliminar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(
                'Eliminado!',
                'El perfil ha sido eliminado',
                'success'
            ).then(() => {
                var slug = document.getElementById("slug").value;
                var dominio = "/wapiptdah/";
                var url = "paciente/eliminar_paciente_d/";
                // Redirigir a una URL específica después de la confirmación
                window.location.href = dominio + url + slug + "/";
            });
        }
    });
}


function editar_perfil_paciente() {
    Swal.fire({
        title: '¿Seguro de editar el perfil?',
        text: 'Estás a punto de editar el perfil',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Editar'
    }).then((result) => {
        if (result.isConfirmed) {
            var slug = document.getElementById("slug").value;
            var dominio = "/wapiptdah/";
            var url = "paciente/editar_paciente/";
            // Redirigir a una URL específica después de la confirmación
            window.location.href = dominio + url + slug + "/";
        }
    });
}

function validar_eliminacion_tecnico() {
    Swal.fire({
        title: '¿Seguro de eliminar el perfil?',
        text: 'Estás a punto de eliminar el perfil',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Eliminar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(
                'Eliminado!',
                'El perfil ha sido eliminado',
                'success'
            ).then(() => {
                var slug = document.getElementById("slug").value;
                var dominio = "/wapiptdah/";
                var url = "tecnico/eliminar_usuariotecnico_d/";
                // Redirigir a una URL específica después de la confirmación
                window.location.href = dominio + url + slug + "/";
            });
        }
    });
}


function editar_perfil_tecnico() {
    Swal.fire({
        title: '¿Seguro de editar el perfil?',
        text: 'Estás a punto de editar el perfil',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Editar'
    }).then((result) => {
        if (result.isConfirmed) {
            var slug = document.getElementById("slug").value;
            var dominio = "/wapiptdah/";
            var url = "tecnico/editar_tecnico/";
            // Redirigir a una URL específica después de la confirmación
            window.location.href = dominio + url + slug + "/";
        }
    });
}

function validar_eliminacion_comun() {
    Swal.fire({
        title: '¿Seguro de eliminar el perfil?',
        text: 'Estás a punto de eliminar el perfil',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Eliminar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(
                'Eliminado!',
                'El perfil ha sido eliminado',
                'success'
            ).then(() => {
                var slug = document.getElementById("slug").value;
                var dominio = "/wapiptdah/";
                var url = "comun/eliminar_usuariocomun_d/";
                // Redirigir a una URL específica después de la confirmación
                window.location.href = dominio + url + slug + "/";;
            });
        }
    });
}


function editar_perfil_comun() {
    Swal.fire({
        title: '¿Seguro de editar el perfil?',
        text: 'Estás a punto de editar el perfil',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Editar'
    }).then((result) => {
        if (result.isConfirmed) {
            var slug = document.getElementById("slug").value;
            var dominio = "/wapiptdah/";
            var url = "comun/editar_comun/";
            // Redirigir a una URL específica después de la confirmación
            window.location.href = dominio + url + slug + "/";
        }
    });
}

