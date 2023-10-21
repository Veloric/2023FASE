(function addResetBtn() {
    let resetBtn = document.getElementById('resetBtn');
    resetBtn.addEventListener('click', resetContactForm);
})();

function resetContactForm() {
    let contactForm = document.getElementById("contactForm");
    for (let i = 0; i < contactForm.elements.length - 2; i++) {
        contactForm.elements[i].value = '';
    }
}