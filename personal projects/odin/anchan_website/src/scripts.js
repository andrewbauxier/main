// scripts.js

/**
 * Load the navigation HTML and insert it into the page.
 */
function loadNavigation() {
    fetch('nav.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('nav').innerHTML = data;
        })
        .catch(error => console.error('Error loading the navigation:', error));
}

// Call the function to load the navigation when the page loads
document.addEventListener('DOMContentLoaded', loadNavigation);