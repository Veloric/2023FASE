// JavaScript to add items and order forms, and other functions.
const orderForms = document.getElementById("orderForms");

function createOrderForm() {
    const orderForm = document.createElement("div");
    orderForm.className = "order-form-container";

    orderForm.innerHTML = `
            orderForm.innerHTML = `
                <span class="delete-button" onclick="deleteOrderForm(this)">X</span>
                <form>
                    <select class="item-type-dropdown" id="item" name="item" onchange="updateOptions(this)">
                        <option value="Cupcake">Cupcake</option>
                        <option value="Cake">Cake</option>
                        <option value="Brownie">Brownie</option>
                        <option value="Dessert Tray">Dessert Tray</option>
                        <option value="Pie">Pie</option>
                        <option value="Cheesecake">Cheesecake</option>
                        <option value="Dietary Specialties">Dietary Specialties</option>    
                        <option value="Mini Tarts">Mini Tarts</option>
                        <option value="Mini Pastries">Mini Pastries</option>
                        <option value="Mini Cheesecake Cups">Mini Cheesecake Cups</option>
                        <option value="Mini Mousse Cups">Mini Mousse Cups</option>
                        <option value="Assorted Mini Desserts">Others</option>
                    </select>

                    <label for="flavor">Flavor:</label>
                    <select id="flavor" name="flavor">
                        <option value="Vanilla Birthday">Vanilla B-day</option>
                        <option value="Chocolate Birthday">Chocolate B-day</option>
                        <option value="Salted Caramel">Salted Caramel</option>
                        <option value="Rockin' Red Velvet">Red Velvet</option>
                        <option value="24 Carrot">Carrot</option>
                        <option value="Peanut Butter Cup">Peanut Butter Cup</option>
                        <option value="Fudge Brownie Explosion">Fudge Brownie</option>
                        <option value="Death By Chocolate">Death By Chocolate</option>
                        <option value="Flower">Flower (Vanilla)</option>
                        <option value="Cannoli">Cannoli</option>
                        <option value="GF Vanilla with Vanilla Buttercream">GF Vanilla</option>
                        <option value="GF Chocolate with Fudge Icing">GF Chocolate</option>
                        <option value="GF Lemon with Vanilla Buttercream">GF Lemon</option> 
                    </select>

                    <label for="size">Size:</label>
                    <select id="size" name="size">
                        <option value="Mini">Mini</option>
                        <option value="Birthday">Birthday (Medium)</option>
                        <option value="Gourmet">Gourmet (Large)</option>
                    </select>

                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" name="quantity" min="1" value="1" onchange="updateItemTotal()">

                    <label for="decorRequests">Decor Requests:</label>
                    <textarea id="decorRequests" name="decorRequests"></textarea>

                    <label for="unitPrice">Unit Price:</label>
                    <input type="text" id="unitPrice" name="unitPrice" readonly>

                    <label for="ItemTotal">Item Total:</label>
                    <input type="text" id="ItemTotal" name="ItemTotal" readonly>
                
                </form>
            `;

            orderForms.appendChild(orderForm);

            // Reset the form
            orderForm.querySelector("form").reset();
        }

        function deleteOrderForm(button) {
            const orderForm = button.parentElement;
            orderForms.removeChild(orderForm);
        }

        function updateOptions(select) {
            const flavorSelect = select.parentElement.querySelector("#flavor");
            const sizeSelect = select.parentElement.querySelector("#size");

            switch (select.value) {
                case "Cake":
                    flavorSelect.innerHTML = `
                        <option value="Andes Mint">Andes Mint</option>
                        <option value="Cookies N' Cream">Cookies N' Cream</option>
                        <option value="Mocha/Macchiato Cake">Mocha/Macchiato Cake</option>
                        <option value="Chocolate Chip Cake">Red Velvet</option>
                        <option value="Fudge Cake">Fudge</option>
                        <option value="Funfetti Fudge">Funfetti Fudge</option>
                        <option value="Chocolate Peanut Butter">Peanut Butter Chocolate</option>
                        <option value="Cherry Cheesecake">Cherry Cheesecake</option>
                        <option value="Red Velvet">Red Velvet</option>
                        <option value="Carrot Cake">Carrot</option>
                        <option value="Black Forest">Black Forest</option>
                        <option value="Chocolate Mousse Cake">Chocolate Mousse</option>
                        <option value="Cannoli Cake">Cannoli</option>
                        <option value="Raspberry Dream">Raspberry Dream</option>
                        <option value="Traditional Strawberry Shotcake">Trad. Strawberry Shortcake</option>
                        <option value="Tiramisu">Tiramisu</option>
                        <option value="Chocolate Decadence">Chocolate Decadence</option>
                        <option value="Nutella">Nutella</option>
                        <option value="Italian Rum">Italian Rum</option>
                        <option value="Signature Strawberry Shortcake">Signature Strawberry Shortcake (with Chocolate)</option>
                    `;
                    sizeSelect.innerHTML = `
                        <option value="6">6"</option>
                        <option value="8">8"</option>
                        <option value="10">10"</option>
                        <option value="12">12"</option>
                        <option value="1/4 Sheet">1/4 Sheet"</option>
                        <option value="1/2 Sheet">1/2 Sheet"</option>
                        <option value="Full Sheet">Full Sheet"</option>
                    `;
                    break;

                case "Brownie":
                    flavorSelect.innerHTML = `
                        <option value="Birthday">Birthday</option>
                        <option value="Oreo">Oreo</option>
                        <option value="Salted Caramel">Salted Caramel</option>
                        <option value="Peanut Butter">Peanut Butter</option>
                    `;
                    sizeSelect.innerHTML = `
                        <option value="Brownie Bites">Brownie Bites</option>
                        <option value="Regular">Regular</option>
                    `;
                    break;

                //Realized that you might be able to do this by parsing through data in SQL. Let me know if you need me to keep doing this
                //If not, feel free to adjust as needed and delete this - Laiba 
                /*
                case "Dessert Tray":
                    flavorSelect.innerHTML = `
                        
                    `;
                    sizeSelect.innerHTML = `
                        
                    `;

                case "Pie":
                    flavorSelect.innerHTML = `
                        

                    `;
                    sizeSelect.innerHTML = `
                        

                    `;
                case "Cheesecake":
                    flavorSelect.innerHTML = `
                        

                    `;
                    sizeSelect.innerHTML = `
                        

                    `;
                
                case "Dietary ":
                    flavorSelect.innerHTML = `

                    `;
                    sizeSelect.innerHTML = `
                        
                    `;
                */
            }
        }

        function updateItemTotal() {
            const unitPrice = parseFloat(document.getElementById("unitPrice").value);
            const quantity = parseFloat(document.getElementById("quantity").value);
            const ItemTotal = unitPrice * quantity;
            document.getElementById("ItemTotal").value = isNaN(ItemTotal) ? '' : ItemTotal.toFixed(2);
        }
    
    /* Dont know if this is needed, but here it is */
        const dateInput = document.getElementById("day");
        const timeInput = document.getElementById("pickup");

        // Calculate the minimum and maximum date values
        const now = new Date();
        const minDate = new Date(now.getTime() + 72 * 60 * 60 * 1000); // 72 hours from now
        minDate.setMinutes(0, 0, 0); // Clear minutes, seconds, and milliseconds

        // Set the minimum and maximum date values
        dateInput.setAttribute("min", minDate.toISOString().slice(0, 10)); // Format as yyyy-mm-dd
        dateInput.setAttribute("max", "2030-12-31"); // A far-future date for maximum

        // Set the step for the time input to allow selection in 15-minute intervals
        timeInput.setAttribute("step", "900"); // 15 minutes in seconds

        // Set the minimum and maximum time values (in HH:MM format)
        timeInput.setAttribute("min", "11:00");
        timeInput.setAttribute("max", "18:00");
    }
}
