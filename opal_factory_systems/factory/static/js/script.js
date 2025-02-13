// Hide preloader when page fully loads
window.addEventListener("load", function () {
    document.getElementById("preloader").style.opacity = "0";
    setTimeout(() => document.getElementById("preloader").style.display = "none", 500);
});



// Dark Mode Toggle
document.getElementById("dark-mode-toggle").addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
});

// Load User Preference
if (localStorage.getItem("darkMode") === "true") {
    document.body.classList.add("dark-mode");
}




