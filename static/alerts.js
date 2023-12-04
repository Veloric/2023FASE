(function addDismiss() {
    let close = document.querySelector(".close");
    if (close != null) {
        close.addEventListener('click', function() {
            close.parentElement.remove();
        })
    }
})();

(function alertsCSS() {
    let alertDiv = document.querySelector(".alert");
    if (alertDiv != null) {
        alertDiv.style.display = "flex";
        alertDiv.style.justifyContent = "space-between";
    }
})();