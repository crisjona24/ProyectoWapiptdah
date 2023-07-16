//Función que permite ver la clave en el login
function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const btnShowPassword = document.querySelector(".btn-show-password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        btnShowPassword.innerHTML = '<i class="fa fa-eye-slash"></i>';
    } else {
        passwordInput.type = "password";
        btnShowPassword.innerHTML = '<i class="fa fa-eye"></i>';
    }
}
