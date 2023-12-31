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


// Search for consumables
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const resultsContainer = document.getElementById('resultsContainer');

    searchInput.addEventListener('input', function() {
        const searchQuery = searchInput.value.trim();

        // Make AJAX request to Django view
        fetch('/ajax/food-selection/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token
            },
            body: new URLSearchParams({ 'search_query': searchQuery }),
        })
        .then(response => response.json())
        .then(data => {
            // Update resultsContainer with queried results and checkboxes
            resultsContainer.innerHTML = '';  // Clear previous results

            data.results.forEach(item => {
                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.value = item.id;
                
                const label = document.createElement('label');
                label.appendChild(checkbox);
                label.appendChild(document.createTextNode(item.name));

                resultsContainer.appendChild(label);
            });
        })
        .catch(error => console.error('Error:', error));
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});