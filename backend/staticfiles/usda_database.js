document.addEventListener('DOMContentLoaded', function () {
    const apiKey = 'YQVtAg0Pkdm4GI6fMg5EH8e5pXuh9ByzHsR8llw0'; // Replace with your USDA API key

    const searchInput = document.getElementById('searchInput');
    const resultsContainer = document.getElementById('resultsContainer');
    const bucket = document.getElementById('bucket');

    searchInput.addEventListener('input', debounce(search));

    function search() {
        const query = searchInput.value.trim();
        if (query.length === 0) {
            resultsContainer.innerHTML = '';
            return;
        }

        fetch(`https://api.nal.usda.gov/fdc/v1/foods/search?query=${query}&api_key=${apiKey}`)
            .then(response => response.json())
            .then(data => displayResults(data.foods))
            .catch(error => console.error('Error fetching data:', error));
    }

    function displayResults(foods) {
        resultsContainer.innerHTML = '';

        //Here I Can Add Additional Databases if Need be
        if (foods.length === 0) {
            resultsContainer.innerHTML = '<p>No results found.</p>';
            return;
        }

        const ul = document.createElement('ul');
        foods.forEach(food => {
            const li = document.createElement('li');
            li.textContent = food.description;
            li.classList.add('list-item');
            li.addEventListener('click', () => {
                selectItem(food);
                li.classList.add('selected-item');
            });
            ul.appendChild(li);
        });

        resultsContainer.appendChild(ul);
    }

    function selectItem(food) {
        // Extracting relevant information
        const { description, foodCategory, servingSize, servingSizeUnit, householdServingFullText, foodNutrients } = food;
    
        // Formatting food nutrients
        const nutrientsHTML = foodNutrients.map(nutrient => `<p class="bucket-item">${nutrient.nutrientName}: ${nutrient.value} ${nutrient.unitName}</p>`).join('');
    
        // Creating HTML for selected item
        const selectedItemHTML = `
        <li class="bucket-item"><strong>Description:</strong> ${description}</li>
        <li class="bucket-item"><strong>Category:</strong> ${foodCategory}</li>
        ${servingSize !== undefined ? `<li class="bucket-item"><strong>Serving Size:</strong> ${servingSize} ${servingSizeUnit}</li>` : `<li class="bucket-item"><strong>Quantity:</strong> 1</li>`}
        ${householdServingFullText !== undefined ? `<li class="bucket-item"><strong>Household Serving:</strong> ${householdServingFullText}</li>` : ''}
        <p style="text-align:center; color:white; font-size:24px;">Contents</p>
        ${nutrientsHTML}
    `;
    
        const addFood = document.getElementById('addFood')
        // Updating "bucket" div
        bucket.innerHTML = selectedItemHTML;
        addFood.style.display = 'block';
    }

    // Debounce function to delay API requests while typing
    function debounce(func, delay = 300) {
        let timeout;
        return function () {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                func.apply(this, arguments);
            }, delay);
        };
    }
});


// Scales Code

document.addEventListener('DOMContentLoaded', function () {

    const addFoodButton = document.getElementById('addFood');
    const scaleTable = document.createElement('table');
    scaleTable.id = 'scaleTable';


    // Create table headers
    scaleTable.innerHTML = `
        <tr>
            <th>Name/Description</th>
            <th>Quantity</th>
            <th>Energy</th>
        </tr>
    `;

    function extractFoodDetails(selectedFood) {
        // Extract relevant information from the selected food
        const parser = new DOMParser();
        const doc = parser.parseFromString(selectedFood, 'text/html');
        const description = doc.body.querySelector('.bucket-item:first-child').textContent.trim();
        const servingSize = getDescriptionValue(doc, 'Serving Size');
        const servingSizeUnit = getDescriptionUnit(doc, 'Serving Size');
        const householdServingFullText = getDescriptionValue(doc, 'Household Serving');
        const foodNutrients = Array.from(doc.body.querySelectorAll('.bucket-item')).map(item => {
            const parts = item.textContent.split(':');
            return { nutrientName: parts[0].trim(), value: parseFloat(parts[1]) };
        });
    
        return { description, servingSize, servingSizeUnit, householdServingFullText, foodNutrients };
    }
    
    function getDescriptionValue(doc, keyword) {
        const element = Array.from(doc.body.querySelectorAll('.bucket-item'))
            .find(item => item.textContent.includes(keyword));
    
        if (element) {
            return element.textContent.split(':')[1].trim();
        }
    
        return '';
    }
    
    function getDescriptionUnit(doc, keyword) {
        const element = Array.from(doc.body.querySelectorAll('.bucket-item'))
            .find(item => item.textContent.includes(keyword));
    
        if (element) {
            const match = element.textContent.match(/(\d+(\.\d+)?) (\w+)/);
            return match ? match[3] : '';
        }
    
        return '';
    }

    function getEnergyValue(foodNutrients) {
        const energyNutrient = foodNutrients.find(nutrient => nutrient.nutrientName.toLowerCase() === 'energy');
        return energyNutrient ? energyNutrient.value : 0;
    }

    let totalEnergy = 0;

    // Function to update the calorie counter
    function updateCalorieCounter() {
        const calorieCounter = document.getElementById('calorieCounter');
        calorieCounter.textContent = `Total Energy: ${totalEnergy} kcal`;
    }

    addFoodButton.addEventListener('click', function () {
        const selectedFood = document.getElementById('bucket').innerHTML;

        if (selectedFood.trim() !== '') {
            // Extract relevant information from the selected food
            const { description, servingSize, servingSizeUnit, foodNutrients } = extractFoodDetails(selectedFood);

            // Create a new table row for the scale
            const scaleTableRow = document.createElement('tr');
            scaleTableRow.innerHTML = `
            <td>${description}</td>
            ${servingSize !== '' ? `<td>${servingSize} ${servingSizeUnit}</td>` : `<td>1</td>`}
            <td>${getEnergyValue(foodNutrients)} kcal</td>
            `;
            scaleTable.appendChild(scaleTableRow);

            // Update the total energy
            totalEnergy += getEnergyValue(foodNutrients);

            // Update the calorie counter
            updateCalorieCounter();

            const showDetailed = document.getElementById('showDetailed');
            showDetailed.style.display = 'block';
            const showScale = document.getElementById('scaleTable');
            showScale.style.display = 'block';
            calorieCounter.style.display = 'block';
        }
    });

    // Append the table to the scale div
    document.querySelector('.scale').appendChild(scaleTable);

    updateCalorieCounter();
    
});
