// OnCall Functions

// Section For User Options
const outerOption = document.querySelector('.outer-option'); 

// Using `.sidebar-option` class for buttons
const openDataButton = document.querySelector('.my-data');
const openHistoryButton = document.querySelector('.my-history');
const openBmiButton = document.querySelector('.my-bmi');

function openData() {
    // Prevent closing outer div when clicking inside window
    openDataButton.addEventListener('click', (event) => {
        event.stopPropagation(); 
    });
    outerOption.classList.add('show');
    openDataButton.classList.add('show');
    openHistoryButton.classList.remove('show');
    openBmiButton.classList.remove('show');
}

function openHistory() {
    // Prevent closing outer div when clicking inside window
    openHistoryButton.addEventListener('click', (event) => {
        event.stopPropagation(); 
    });
    outerOption.classList.add('show');
    openDataButton.classList.remove('show');
    openHistoryButton.classList.add('show');
    openBmiButton.classList.remove('show');
}

function openBmi() {
    // Prevent closing outer div when clicking inside window
    openBmiButton.addEventListener('click', (event) => {
        event.stopPropagation(); 
    });
    outerOption.classList.add('show');
    openDataButton.classList.remove('show');
    openHistoryButton.classList.remove('show');
    openBmiButton.classList.add('show');
}

function closeOuterOption() {

    // Click happened outside the outer div, proceed with closing
    openDataButton.classList.remove('show');
    openHistoryButton.classList.remove('show');
    openBmiButton.classList.remove('show');
  
    // Adding delay using setTimeout For Animation smoothness
    const delayPromise = new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 500); // 0.5 seconds delay , same as in css
    });
  
    // Waiting for the promise to resolve before removing the show class
    delayPromise.then(() => {
      outerOption.classList.remove('show');
    });
  }


// Search for consumables
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const resultsContainer = document.getElementById('resultsContainer');

    // In Case I Figure it out later on, For not just ignore

    // searchInput.addEventListener('input', function() {
    //     const searchQuery = searchInput.value.trim();

    //     // Make AJAX request to Django view
    //     fetch('/ajax/food-selection/', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/x-www-form-urlencoded',
    //             'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token
    //         },
    //         body: new URLSearchParams({ 'search_query': searchQuery }),
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         // Update resultsContainer with queried results and checkboxes
    //         resultsContainer.innerHTML = '';  // Clear previous results

    //         data.results.forEach(item => {
    //             const checkbox = document.createElement('input');
    //             checkbox.type = 'checkbox';
    //             checkbox.value = item.id;
                
    //             const label = document.createElement('label');
    //             label.appendChild(checkbox);
    //             label.appendChild(document.createTextNode(item.name));

    //             resultsContainer.appendChild(label);
    //         });
    //     })
    //     .catch(error => console.error('Error:', error));
    // });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }


    // Login
    const passwordInput = document.getElementById('pass');
    const revealPassword = document.getElementById('showPassword');

    revealPassword.addEventListener('change', function() {
        passwordInput.type = this.checked ? 'text' : 'password';
    })

    // Register
    const regPasswordInput = document.getElementById('password');
    const regRepeatPasswordInput = document.getElementById('repeatpassword');
    const regRevealPassword = document.getElementById('revealPassword');


    passwordInput.addEventListener('input', function () {
        // Check for password validation (at least 6 characters and contains at least 1 number)
        const password = passwordInput.value;

        // This part of the code does not work as intended

        // const lengthValid = password.length >= 6;
        // const containsNumber = /\d/.test(password);

        // if (!lengthValid || !containsNumber) {
        //     alert('Password must be at least 6 characters long and contain at least 1 number');
        // } else {}
    });

    regRevealPassword.addEventListener('change', function () {
        regPasswordInput.type = this.checked ? 'text' : 'password';
        regRepeatPasswordInput.type = this.checked ? 'text' : 'password';
    });




});


//Event Listener Section

// Login / Register transitions

function openSidebar() {
    document.getElementById("sidebar").style.right = "0";
}

function closeSidebar() {
    document.getElementById("sidebar").style.right = "-250px";
}

function performLogout() {
    window.location.href = logoutUrl;
}



//Hiding and Showing Login Window
const loginBtn = document.querySelector('.loginBtn')
const closeBtn = document.querySelector('.icon-close')
const authContainer = document.querySelector('.auth-container')

loginBtn.addEventListener('click', ()=> {
    wrapper.classList.add('active-login');
    authContainer.classList.add('active-login');
});

closeBtn.addEventListener('click', ()=> {
    wrapper.classList.remove('active-login');
    authContainer.classList.remove('active-login');
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





function  bmiCalculate(){
    const heightInput = document.getElementById('height');
    const heightUnit = document.getElementById('height-unit');
    const weightInput = document.getElementById('weight');
    const weightUnit = document.getElementById('weight-unit');
    const calculateButton = document.getElementById('calculate-bmi');
    // Get values and units
    const height = parseFloat(heightInput.value);
    const heightUnitValue = heightUnit.value;
    const weight = parseFloat(weightInput.value);
    const weightUnitValue = weightUnit.value;

    // Convert units if needed
    let convertedHeight, convertedWeight;
    if (heightUnitValue === 'cm') {
        convertedHeight = height / 100; // Convert cm to meters
    } else if (heightUnitValue === 'ft') {
        convertedHeight = height * 0.3048; // Convert ft to meters
    } else {
        convertedHeight = height; // Already in meters
    }
    
    if (weightUnitValue === 'lb') {
        convertedWeight = weight / 2.2046; // Convert lb to kg
    } else {
        convertedWeight = weight; // IF it is Already in kg
    }

    // Calculate BMI
    const bmi = convertedWeight / (convertedHeight * convertedHeight);

    // Display BMI result (you can replace this with other logic)
    alert(`Your BMI is: ${bmi.toFixed(2)}`);
};

