// project: aaDesign
// module: scripts.js
// author: andrew b. auxier

// Function to toggle between light and dark mode
function toggleMode() {
    // Toggle the 'mode' class on the body element
    document.body.classList.toggle('mode');
}

// Function to load translations based on the selected language
function loadTranslations(language) {
    // Fetch the JSON file containing translations for the selected language
    fetch(`/translations/${language}.json`)
        .then((response) => response.json()) // Convert the response to JSON
        .then((translations) => {
            // Log the loaded translations to verify they are correct
            console.log('Loaded Translations:', translations);

            // Update the navigation content with translations
            document.getElementById('nav-about').textContent = translations.nav.about;
            document.getElementById('nav-services').textContent = translations.nav.services;
            document.getElementById('nav-legal').textContent = translations.nav.legal;
            document.getElementById('nav-menu').textContent = translations.nav.menu;

            // Update the footer content with translations
            document.getElementById('footer-copyright').textContent = translations.footer.copyright;

            // Update the landing page content with translations
            if (document.getElementById('landing-welcome')) {
                document.getElementById('landing-welcome').textContent = translations.landing.welcome;
                document.getElementById('landing-aboutUsTitle').textContent = translations.landing.aboutUsTitle;
                document.getElementById('landing-aboutUsText').textContent = translations.landing.aboutUsText;
            }
        })
        .catch((error) => {
            console.error('Error loading translations:', error);
        });
}

// Function to handle language switching
function handleLanguageSwitch() {
    const languageSwitcher = document.getElementById('language-switcher');
    const selectedLanguage = localStorage.getItem('language') || 'en'; // Default to English
    loadTranslations(selectedLanguage); // Load the translations when the page loads

    // Set the value of the language switcher dropdown to the selected language
    languageSwitcher.value = selectedLanguage;
    languageSwitcher.addEventListener('change', (event) => {
        const selectedLanguage = event.target.value;
        loadTranslations(selectedLanguage); // Load translations based on user selection
        localStorage.setItem('language', selectedLanguage); // Save the selected language in localStorage
    });
}

// Function to load the navigation bar content
function loadNav() {
    // Fetch the content of nav.html
    return fetch('nav.html')
        .then(response => response.text()) // Convert the response to text
        .then(data => {
            const nav = document.querySelector('nav');
            // Insert the fetched HTML into the <nav> element
            nav.innerHTML = data;

            // Add event listener for the mode toggle checkbox
            const modeToggleCheckbox = document.querySelector('.nav-mode-toggle input[type="checkbox"]');
            if (modeToggleCheckbox) {
                // Add change event listener to toggle mode
                modeToggleCheckbox.addEventListener('change', toggleMode);
            }
        });
}

// Function to load the footer content
function loadFooter() {
    // Fetch the content of footer.html
    return fetch('footer.html')
        .then(response => response.text()) // Convert the response to text
        .then(data => {
            // Insert the fetched HTML into the <footer> element
            document.querySelector('footer').innerHTML = data;
        });
}

// Function to ensure both the nav and footer are loaded before running translations
function initializePage() {
    Promise.all([loadNav(), loadFooter()]).then(() => {
        // Re-run the translation logic after both nav and footer are fully loaded
        handleLanguageSwitch();
    });
}

// Call the function to load the navigation bar and footer when the page loads
document.addEventListener('DOMContentLoaded', () => {
    initializePage(); // Initialize the page after loading nav and footer
});
