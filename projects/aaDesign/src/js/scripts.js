// Function to toggle between light and dark mode
function toggleMode() {
    // Toggle the 'mode' class on the body element
    document.body.classList.toggle('mode');
}

// Function to load the navigation bar content
function loadNav() {
    // Fetch the content of nav.html
    fetch('nav.html')
        .then(response => response.text()) // Convert the response to text
        .then(data => {
            const nav = document.querySelector('nav');
            // Insert the fetched HTML into the <nav> element
            nav.innerHTML = data;

            // Add event listener for the mode toggle button
            const modeToggle = document.getElementById('mode');
            if (modeToggle) {
                // Add click event listener to toggle mode
                modeToggle.addEventListener('click', toggleMode);
            }

            // Add event listener for the hamburger menu
            const hamburger = document.querySelector('.hamburger');
            if (hamburger) {
                // Add click event listener to toggle dropdown menu visibility
                hamburger.addEventListener('click', () => {
                    nav.classList.toggle('active');
                });
            }
        });
}

// Function to load the footer content
function loadFooter() {
    // Fetch the content of footer.html
    fetch('footer.html')
        .then(response => response.text()) // Convert the response to text
        .then(data => {
            // Insert the fetched HTML into the <footer> element
            document.querySelector('footer').innerHTML = data;
        });
}

// Call the functions to load the navigation bar and footer when the page loads
document.addEventListener('DOMContentLoaded', () => {
    loadNav(); // Load the navigation bar
    loadFooter(); // Load the footer
});
