let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centrado", targets: [0, 1, 2, 3] },
        { orderable: false, targets: [2, 3] },
        { width: "10%", targets: [3] },
        { searchable: false, targets: [0] }
    ],
    pageLength: 25,
    destroy: true,
    language: {
        lengthMenu: "Mostrar _MENU_ registros por página",
        zeroRecords: "Ningún usuario encontrado",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Ningún usuario encontrado",
        infoFiltered: "(filtrados desde _MAX_ registros totales)",
        search: "Buscar:",
        loadingRecords: "Cargando...",
        paginate: {
            first: "Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
}

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    dataTable = $("#listadopaciente").DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

window.addEventListener("load", async () => {
    await initDataTable();
});