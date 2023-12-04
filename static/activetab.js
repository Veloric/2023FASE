// For order, index, and contact
// Check if the location has a navbar item's name and if it does, set it as the active tab
(function setActiveTab() {
    let navbar = document.querySelector(".nav-bar");
    let tab = window.location.pathname;
    console.log(tab);
    console.log(typeof(tab));

    if (tab === "/order") {
        addActive(navbar, 0);
    } else if (tab === "/galleryphotos") {
        addActive(navbar, 2);
    } else if (tab === "/contact") {
        addActive(navbar, 3);
    } else if (tab === "/menu") {
        addActive(navbar, 4);
    } else if (tab === ("/adminPage")) {
        addActive(navbar, 5);
    } else if (tab === ("/login")) {
        addActive(navbar, 6);
    } else if (tab === ("/register")) {
        addActive(navbar, 7);
    } else if (tab === "/"){
        addActive(navbar, 1);
    }
})();

function addActive(navbar, i) {
    navbar.children[i].firstChild.classList.add("active");
}