const header = document.querySelector("header");

window.addEventListener("scroll", function(){
    header.classList.toggle ("sticky", window.scrollY > 0)
});

let menu = document.querySelector('#menu-icon');
let list = document.querySelector('list');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    list.classList.toggle('active');
}