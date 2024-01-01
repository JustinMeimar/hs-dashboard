const url = "http://127.0.0.1:3001/logs";
const itemsPerPage = 10;
let currentPage = 1;
let data = [];

async function fetchData(url) { 
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const fetchData = await response.json();
        data = fetchData;
    } catch (error) {
        console.error()
    }
}

function displayData(page) {
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const paginatedItems = data.slice(startIndex, endIndex);
    const container = document.getElementById('data-container'); // Correctly defining 'container'
    container.innerHTML = '';

    paginatedItems.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.className = 'data-item';
        itemElement.id = 'data-item-' + (startIndex + index); // Unique ID for each item

        Object.keys(item).forEach(key => {
            const subElement = document.createElement('div');
            subElement.className = 'item-field';
            subElement.innerHTML = `<strong>${key}:</strong> ${item[key]}`;
            itemElement.appendChild(subElement);
        });

        container.appendChild(itemElement);
    });
}

function setupPagination() {
    
    document.getElementById('next').addEventListener('click', () => {
        currentPage++;
        displayData(currentPage);
    });

    document.getElementById('prev').addEventListener('click', () => {
        currentPage = Math.max(1, currentPage - 1);
        displayData(currentPage);
    });
}

document.addEventListener('DOMContentLoaded', async function() {
    console.log('JavaScript loaded');

    await fetchData(url);
    displayData(currentPage);
    setupPagination();

});