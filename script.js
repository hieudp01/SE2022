let loginForm = document.querySelector('.login-form');

document.querySelector('#login-btn').onclick = () =>{
    loginForm.classList.toggle('active');
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    loginForm.classList.remove('active');
}

window.onscroll = () =>{
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

/*
document.getElementById("switchToRegister").addEventListener("click", function(e) {
    e.preventDefault();
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("registerForm").style.display = "block";
});

document.getElementById("switchToLogin").addEventListener("click", function(e) {
    e.preventDefault();
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("registerForm").style.display = "none";
});*/