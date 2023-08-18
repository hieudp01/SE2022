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

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var role = document.getElementById("role").value;

    // Perform authentication logic here

    // Assuming you've verified the credentials and role
    if (role === "parent") {
        // Redirect to parent.html
        window.location.href = "index/parent.html";
    } else if (role === "teacher") {
        // Redirect to teacher.html
        window.location.href = "teacher/teacher.html";
    } else if (role === "admin") {
        // Redirect to admin.html
        window.location.href = "admin/admin.html";
    }
    else if (role === "guest"){
        window.location.href = "index.html";
      
    } else {
        alert("Invalid credentials. Please try again.");
    }
});
