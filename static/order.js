// JavaScript to add items and order forms
const orderForms = document.getElementById("orderForms");

function createOrderForm() {
    const orderForm = document.createElement("div");
    orderForm.className = "order-form-container";

    orderForm.innerHTML = `
        <span class="delete-button" onclick="deleteOrderForm(this)">X</span>
        <form>
            <select class="item-type-dropdown" id="item" name="item" onchange="updateOptions(this)">
                <option value="Cupcake">Cupcake</option>
                <option value="Cake">Cake</option>
                <option value="Brownie">Brownie</option>
            </select>

            <label for="flavor">Flavor:</label>
            <select id="flavor" name="flavor">
                <option value="Chocolate">Chocolate</option>
                <option value="Vanilla">Vanilla</option>
                <option value="Strawberry">Strawberry</option>
            </select>

            <label for="size">Size:</label>
            <select id="size" name="size">
                <option value="Small">Small</option>
                <option value="Medium">Medium</option>
                <option value="Large">Large</option>
            </select>

            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity" min="1" value="1">

            <label for="unitPrice">Unit Price:</label>
            <input type="text" id="unitPrice" name="unitPrice" readonly>

            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity" min="1" value="1" onchange="updateTotalPrice()">

            <label for="totalPrice">Total Price:</label>
            <input type="text" id="totalPrice" name="totalPrice" readonly>
        
            <label for="decorRequests">Decor Requests:</label>
            <textarea id="decorRequests" name="decorRequests"></textarea>
        
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
        case "Cupcake":
            flavorSelect.innerHTML = `
                <option value="Chocolate">Chocolate</option>
                <option value="Vanilla">Vanilla</option>
                <option value="Strawberry">Strawberry</option>
            `;
            sizeSelect.innerHTML = `
                <option value="Small">Small</option>
                <option value="Medium">Medium</option>
            `;
    }
}
