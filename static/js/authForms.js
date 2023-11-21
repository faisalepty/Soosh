const signupForm = document.querySelector('#signUpForm');
const loginForm = document.querySelector('#loginForm');
const signupButton = document.querySelector('#signupButton');
const loginButton = document.querySelector('#loginButton');
const signupHr = document.querySelector('#signupHr');
const loginHr = document.querySelector('#loginHr');
const password1 = document.querySelector('#id_password1');
const password2 = document.querySelector('#id_password2');

password1.attributes.placeholder = 'Password'
password2.attributes.placeholder = 'Confirm Password'

function loginSwap(){
    loginForm.className = 'd-block'
    signupForm.className = 'd-none'
    loginHr.style.color = 'black'
    signupHr.style.color = '#e5e9ed'

}
function signupSwap(){
    loginForm.className = 'd-none'
    signupForm.className = 'd-block'
    loginHr.style.color = '#e5e9ed'
    signupHr.style.color = 'black'

}
console.log(signupButton)

signupButton.addEventListener('click', signupSwap)
loginButton.addEventListener('click', loginSwap)