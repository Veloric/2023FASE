(function addDismiss() {
    let close = document.querySelector(".close");
    close.addEventListener('click', function() {
        close.parentElement.remove();
    })
})();

(function alertsCSS() {
    let alertDiv = document.querySelector(".alert");
    alertDiv.style.display = "flex";
    alertDiv.style.justifyContent = "space-between";
})();