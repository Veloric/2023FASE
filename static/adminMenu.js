function getDropdown() {
    let dropdown = document.getElementById("menuSelection");
    let dropdownValue;

    dropdown.addEventListener('focusout', function() {
        dropdownValue = dropdown.value;
    })
}




getDropdown();