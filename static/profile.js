document.addEventListener("DOMContentLoaded", function () {
    //Event listener for the "Save changes" button
    document.getElementById("saveChangesBtn").addEventListener("click", function () {
        if (validateForm()) {
            alert("Form is valid!");
            //Implement save logic here
        }
    });

    function validateForm() {
        document.getElementById("errorMessages").innerHTML = "";

        //Check if the first name is not empty
        var firstName = document.getElementById("inputFirstName").value.trim();
        if (firstName === "") {
            document.getElementById("errorMessages").innerHTML = "<p class='text-danger'>Please enter your first name.</p>";
            return false; //Form is not valid
        }

        //Add MORE validation logic for other inputs...
        return true; //Form is valid
    }
});
