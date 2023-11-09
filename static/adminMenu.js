// Add an event listener to check when the user clicks off of the dropdown menu
function getDropdown() {
    let dropdown = document.getElementById("menuSelection");

    dropdown.addEventListener('focusout', function() {
        dropdownValue = dropdown.value;
        hideAllForms();
        showForm(dropdownValue);
    })
}

// Show the form depending on which option is selected in the dropdown menu
function showForm(dropdownValue) {
    let miniDessertsForm = document.getElementById("miniDessertsForm");
    let dessertTrayForm = document.getElementById("dessertTrayForm");
    let pieAndCheesecakeForm = document.getElementById("pieAndCheesecakeForm");
    let cupcakeForm = document.getElementById("cupcakeForm");
    let dietaryForm = document.getElementById("dietaryForm");
    let signatureFlavorCakeForm = document.getElementById("signatureFlavorCakeForm");
    let cakeForm = document.getElementById("cakeForm");

    let array = [miniDessertsForm, dessertTrayForm, pieAndCheesecakeForm, cupcakeForm, dietaryForm, signatureFlavorCakeForm, cakeForm];
    let index = dropdownValue - 1;

    array[index].style.display = 'block';
}

// Hide all of the forms when checking for the dropdown
function hideAllForms() {
    let miniDessertsForm = document.getElementById("miniDessertsForm");
    let dessertTrayForm = document.getElementById("dessertTrayForm");
    let pieAndCheesecakeForm = document.getElementById("pieAndCheesecakeForm");
    let cupcakeForm = document.getElementById("cupcakeForm");
    let dietaryForm = document.getElementById("dietaryForm");
    let signatureFlavorCakeForm = document.getElementById("signatureFlavorCakeForm");
    let cakeForm = document.getElementById("cakeForm");

    miniDessertsForm.style.display = 'none';
    dessertTrayForm.style.display = 'none';
    pieAndCheesecakeForm.style.display = 'none';
    cupcakeForm.style.display = 'none';
    dietaryForm.style.display = 'none';
    signatureFlavorCakeForm.style.display = 'none';
    cakeForm.style.display = 'none';
}

// Shows the default form (MiniDesserts)
function showDefaultForm() {
    let miniDessertsForm = document.getElementById("miniDessertsForm");
    miniDessertsForm.style.display = 'block';
}

// Functions ran on page load
hideAllForms();
getDropdown();
showDefaultForm();