let listElements = document.querySelectorAll('.list__button--click');

listElements.forEach(listElement => {
    listElement.addEventListener('click', () => {

        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;
        if (menu.clientHeight == "0") {
            height = menu.scrollHeight;
        }

        menu.style.height = `${height}px`;

    })
});

/* Funcion para cambiar el color de fondo */
function cambiarColorFondo() {
    var select = document.getElementById("colorSelect");
    var colorSeleccionado = select.value;
    var section = document.getElementById("mysection");
    section.style.backgroundColor = colorSeleccionado;
}