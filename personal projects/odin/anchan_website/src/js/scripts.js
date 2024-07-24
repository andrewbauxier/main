// scripts.js

/**
 * Load the navigation HTML and insert it into the page.
 */
function loadNavigation() {
    fetch('nav.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('nav').innerHTML = data;
            setupHamburgerMenu();
        })
        .catch(error => console.error('Error loading the navigation:', error));
}

/**
 * Set up the hamburger menu toggle functionality.
 */
function setupHamburgerMenu() {
    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('nav');

    hamburger.addEventListener('click', () => {
        nav.classList.toggle('active');
    });
}

// Call the function to load the navigation when the page loads
document.addEventListener('DOMContentLoaded', loadNavigation);
