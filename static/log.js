document.addEventListener("DOMContentLoaded", function () {
    function openTab(evt, tabName) {
        let tabContent, tabLinks;

        tabContent = document.getElementsByClassName("tab-content");
        for (let i = 0; i < tabContent.length; i++) {
            tabContent[i].classList.remove("active");
        }

        tabLinks = document.getElementsByClassName("tab-link");
        for (let i = 0; i < tabLinks.length; i++) {
            tabLinks[i].className = tabLinks[i].className.replace(" active", "");
        }

        document.getElementById(tabName).classList.add("active");
        evt.currentTarget.className += " active";
    }

    document.querySelectorAll(".tab-link").forEach(tab => {
        tab.addEventListener("click", function(event) {
            openTab(event, tab.getAttribute("onclick").split("'")[1]);
        });
    });

    // Set default tab to login
    document.querySelector(".tab-link").click();
});
