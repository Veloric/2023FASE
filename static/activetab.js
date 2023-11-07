// For order, index, and contact
// Check if the location has a navbar item's name and if it does, set it as the active tab
(function setActiveTab() {
    let navbar = document.querySelector(".nav-bar");
    let tab = window.location.href;

    if (tab.includes("order")) {
        navbar.children[0].firstChild.classList.add("active");
    } else if (tab.includes("contact")) {
        navbar.children[2].firstChild.classList.add("active");
    } else if (tab.includes("menu")) {
        navbar.children[3].firstChild.classList.add("active");
    } else if (tab.includes("adminMenu")) {
        navbar.children[4].firstChild.classList.add("active");
    } else {
        navbar.children[1].firstChild.classList.add("active");
    }
})();