function login() {
    const enteredUsername = document.getElementById('username').value;
    const enteredPassword = document.getElementById('password').value;

    if (enteredUsername === 'user' && enteredPassword === 'pass') {
        window.location.href = 'HtmlPage2.html';
    } else {
        alert('Invalid username or password. Please try again.');
    }
}



function signup() {
    const enteredUsername = document.getElementById('newUsername').value;
    const enteredPassword = document.getElementById('newPassword').value;
    alert(enteredUsername); //until we have secure DB
    alert(enteredPassword); //until we have secure DB
}

function recoverPassword() { //need to find free API and learn it 
    alert("Under Construction");
}

function showSignupForm() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('signupForm').style.display = 'block';
    document.getElementById('forgotPasswordForm').style.display = 'none';
}

function showForgotPasswordForm() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('signupForm').style.display = 'none';
    document.getElementById('forgotPasswordForm').style.display = 'block';
}

function showLoginForm() {
    document.getElementById('loginForm').style.display = 'block';
    document.getElementById('signupForm').style.display = 'none';
    document.getElementById('forgotPasswordForm').style.display = 'none';
}
