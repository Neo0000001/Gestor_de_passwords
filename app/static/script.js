function togglePassword(id) {
    const field = document.getElementById(`password-${id}`);
    const button = document.getElementById(`toggle-${id}`);
    if (field.textContent.includes('••••')) {
        field.textContent = field.dataset.password;
        button.textContent = "Ocultar";
    } else {
        field.textContent = '••••••••';
        button.textContent = "Mostrar";
    }
}
