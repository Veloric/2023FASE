// For order, index, and contact
// Check if the location has a navbar item's name and if it does, set it as the active tab
(function setActiveTab() {
    let navbar = document.querySelector(".nav-bar");
    let tab = window.location.pathname;

    if (tab === "/order") {
        addActive(navbar, 0);
    } else if (tab === "/galleryphotos") {
        addActive(navbar, 2);
    } else if (tab === "/contact") {
        addActive(navbar, 3);
    } else if (tab === "/menu") {
        addActive(navbar, 4);
    } else if (tab === ("/profile") || tab === ("/login")) {
        addActive(navbar, 5);
    } else if (tab === ("/logout") || tab === ("/register")) {
        addActive(navbar, 6);
    } else if (tab === ("/adminPage")) {
        addActive(navbar, 7);
    } else if (tab === "/"){
        addActive(navbar, 1);
    }
})();

function addActive(navbar, i) {
    navbar.children[i].firstChild.classList.add("active");
}

(function logOutCSS() {
    let logout = document.getElementById("nav-logout");
    if (logout != null) {
        logout.style.backgroundColor = "#f3c6e8";
        logout.style.padding = "0.5rem 1rem";
        logout.style.borderRadius = "0.375rem";

        logout.addEventListener("mouseover", function() {
            logout.style.backgroundColor = "#c887b1";
        })
        logout.addEventListener("mouseout", function() {
            logout.style.backgroundColor = "#f3c6e8";
        })
    }
})();