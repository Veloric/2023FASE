// For order, index, and contact
// Check if the location has a navbar item's name and if it does, set it as the active tab
(function setActiveTab() {
    let navbar = document.querySelector(".nav-bar");
    let tab = window.location.href;

    if (tab.includes("order")) {
        addActive(navbar, 0);
    } else if (tab.includes("galleryphotos")) {
        addActive(navbar, 2);
    } else if (tab.includes("contact")) {
        addActive(navbar, 3);
    } else if (tab.includes("menu")) {
        addActive(navbar, 4);
    } else if (tab.includes("addMenu")) {
        addActive(navbar, 5);
    } else {
        addActive(navbar, 1);
    }
})();

function addActive(navbar, i) {
    navbar.children[i].firstChild.classList.add("active");
}