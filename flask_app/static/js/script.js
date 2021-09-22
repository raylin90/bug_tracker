let btn = document.querySelector("#btn");
let sideBar = document.querySelector(".sidebar");
let searchBtn = document.querySelector("#search-icon");

btn.onclick = function() {
    sideBar.classList.toggle("active");
}
searchBtn.onclick = function() {
    sideBar.classList.toggle("active");
}