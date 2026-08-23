const navigationContainer = document.querySelector("[data-navigation]");


if (navigationContainer) {

    fetch("../navigation.html")
        .then((response) => response.text())
        .then((navigation) => {

            navigationContainer.innerHTML = navigation;

            const currentPage =
                window.location.pathname.split("/").pop();

            navigationContainer
                .querySelectorAll(".sidebar-link")
                .forEach((link) => {

                    const linkPage =
                        link.getAttribute("href").split("/").pop();

                    link.classList.toggle(
                        "active",
                        linkPage === currentPage
                    );

                });

        });

}


const sidebar = document.getElementById("sidebar");
const menuButton = document.getElementById("menuButton");
const closeButton = document.getElementById("closeButton");
const overlay = document.getElementById("sidebarOverlay");


// Opens the sidebar
function openSidebar() {

    sidebar.classList.add("open");
    overlay.classList.add("open");

}


// Closes the sidebar
function closeSidebar() {

    sidebar.classList.remove("open");
    overlay.classList.remove("open");

}


// Open menu
menuButton?.addEventListener("click", openSidebar);


// Close menu
closeButton?.addEventListener("click", closeSidebar);


// Close by clicking outside
overlay?.addEventListener("click", closeSidebar);


// Close using Escape
document.addEventListener("keydown", (event) => {

    if (event.key === "Escape") {

        closeSidebar();

    }

});


// =========================================
// SUBJECT BUTTON CLICK ANIMATION
// =========================================

const subjectButtons =
    document.querySelectorAll(".subject-button");


subjectButtons.forEach((button) => {

    button.addEventListener("click", (event) => {

        // Stop the page from changing immediately
        event.preventDefault();


        const destination =
            button.getAttribute("href");


        // Start animation
        button.classList.add("pressed");


        // Wait for animation, then open page
        setTimeout(() => {

            window.location.href =
                destination;

        }, 180);

    });

});