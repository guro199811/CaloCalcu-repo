//Hiding and Showing Login Window
const loginBtn = document.querySelector('.loginBtn')
const closeBtn = document.querySelector('.icon-close')

loginBtn.addEventListener('click', ()=> {
    wrapper.classList.add('active-login');
});

closeBtn.addEventListener('click', ()=> {
    wrapper.classList.remove('active-login');
})



//Transition Between Login and Register
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link')
const registerLink = document.querySelector('.register-link')



registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

