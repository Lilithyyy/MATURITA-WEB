const navigationContainer = document.querySelector("[data-navigation]");


if (navigationContainer) {

    fetch("../navigation.html")
        .then((response) => {

            if (!response.ok) {
                throw new Error(`Navigation request failed: ${response.status}`);
            }

            return response.text();

        })
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

        })
        .catch(() => {

            navigationContainer.remove();

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


// =========================================
// TOPIC READING PROGRESS
// =========================================

if (document.body.classList.contains("topic-page")) {

    const progress = document.createElement("div");
    const progressFill = document.createElement("div");
    const progressLabel = document.createElement("span");

    progress.className = "reading-progress";
    progressFill.className = "reading-progress-fill";
    progressLabel.className = "reading-progress-label";

    progress.setAttribute("aria-label", "Postup čítania");
    progressLabel.setAttribute("aria-hidden", "true");
    progress.setAttribute("role", "progressbar");
    progress.setAttribute("aria-valuemin", "0");
    progress.setAttribute("aria-valuemax", "100");
    progress.append(progressFill);
    document.body.append(progress);
    document.body.append(progressLabel);

    const updateProgress = () => {

        const details =
            [...document.querySelectorAll(".topic-details")];

        const visitedDetails =
            details.filter((detail) => detail.dataset.visited === "true").length;

        const detailsProgress = details.length
            ? visitedDetails / details.length
            : 1;

        const scrollableHeight =
            document.documentElement.scrollHeight - window.innerHeight;

        const scrollProgress = scrollableHeight > 0
            ? window.scrollY / scrollableHeight
            : 1;

        const percentage =
            Math.round((detailsProgress * 0.7 + scrollProgress * 0.3) * 100);

        progressFill.style.height = `${percentage}%`;
        progressLabel.textContent = `${percentage}%`;
        progress.setAttribute("aria-valuenow", percentage);

    };


    const connectDetails = () => {

        document.querySelectorAll(".topic-details").forEach((detail) => {

            if (detail.dataset.progressBound) {
                return;
            }

            detail.dataset.progressBound = "true";

            detail.addEventListener("toggle", () => {

                if (detail.open) {
                    detail.dataset.visited = "true";
                }

                updateProgress();

            });

        });

        updateProgress();

    };


    window.addEventListener("scroll", updateProgress, { passive: true });
    window.addEventListener("resize", updateProgress);

    const topicContent = document.querySelector(".topic-content");

    new MutationObserver(connectDetails).observe(topicContent, {
        childList: true,
        subtree: true
    });

    connectDetails();

}