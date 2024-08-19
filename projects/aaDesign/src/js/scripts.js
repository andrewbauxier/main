// project: aaDesign
// module: scripts.js
// author: andrew b. auxier

// Function to toggle between light and dark mode
function toggleMode() {
    try {
        // Toggle the 'mode' class on the body element
        document.body.classList.toggle('mode');
    } catch (error) {
        console.error('ERROR TOGGLING MODE:', error);
    }
}

// Function to load translations based on the selected language
function loadTranslations(language) {
    fetch(`/translations/${language}.json`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Failed to fetch translations: ${response.statusText}`);
            }
            return response.json(); // Convert the response to JSON
        })
        .then((translations) => {
            console.log('Loaded Translations:', translations);

            // Update the navigation content with translations
            try {
                document.getElementById('nav-about').textContent = translations.nav.about;
                document.getElementById('nav-services').textContent = translations.nav.services;
                document.getElementById('nav-legal').textContent = translations.nav.legal;
                document.getElementById('nav-menu').textContent = translations.nav.menu;
            } catch (error) {
                console.error('ERROR UPDATING NAVIGATION CONTENT:', error);
            }

            // Update the footer content with translations
            try {
                document.getElementById('footer-copyright').textContent = translations.footer.copyright;
            } catch (error) {
                console.error('ERROR UPDATING FOOTER CONTENT:', error);
            }

            // Update the landing page content with translations
            try {
                if (document.getElementById('landing-welcome')) {
                    document.getElementById('landing-welcome').textContent = translations.landing.welcome;
                    document.getElementById('landing-aboutUsTitle').textContent = translations.landing.aboutUsTitle;
                    document.getElementById('landing-aboutUsText').textContent = translations.landing.aboutUsText;
                }
            } catch (error) {
                console.error('ERROR UPDATING LANDING PAGE CONTENT:', error);
            }
        })
        .catch((error) => {
            console.error('ERROR LOADING TRANSLATIONS:', error);
        });
}

// Function to handle language switching
function handleLanguageSwitch() {
    try {
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
    } catch (error) {
        console.error('ERROR HANDLING LANGUAGE SWITCH:', error);
    }
}

// Function to load the navigation bar content
function loadNav() {
    return fetch('nav.html')
        .then(response => {
            if (!response.ok) {
                throw new Error(`FAILED TO LOAD nav.html: ${response.statusText}`);
            }
            return response.text(); // Convert the response to text
        })
        .then(data => {
            try {
                const nav = document.querySelector('nav');
                nav.innerHTML = data; // Insert the fetched HTML into the <nav> element

                // Add event listener for the mode toggle checkbox
                const modeToggleCheckbox = document.querySelector('.nav-mode-toggle input[type="checkbox"]');
                if (modeToggleCheckbox) {
                    modeToggleCheckbox.addEventListener('change', toggleMode);
                }
            } catch (error) {
                console.error('ERROR INSERTING NAVIGATION CONTENT:', error);
            }
        })
        .catch((error) => {
            console.error('ERROR LOADING NAV:', error);
        });
}

// Function to load the footer content
function loadFooter() {
    return fetch('footer.html')
        .then(response => {
            if (!response.ok) {
                throw new Error(`FAILED TO LOAD footer.html: ${response.statusText}`);
            }
            return response.text(); // Convert the response to text
        })
        .then(data => {
            try {
                document.querySelector('footer').innerHTML = data; // Insert the fetched HTML into the <footer> element
            } catch (error) {
                console.error('ERROR INSERTING FOOTER CONTENT:', error);
            }
        })
        .catch((error) => {
            console.error('ERROR LOADING FOOTER:', error);
        });
}

// Function to ensure both the nav and footer are loaded before running translations
function initializePage() {
    try {
        Promise.all([loadNav(), loadFooter()])
            .then(() => {
                handleLanguageSwitch(); // Re-run the translation logic after both nav and footer are fully loaded
            })
            .catch((error) => {
                console.error('ERROR INITIALIZING PAGE PROMISE:', error);
            });
    } catch (error) {
        console.error('ERROR INITIALIZING PAGE:', error);
    }
}

// Call the function to load the navigation bar and footer when the page loads
document.addEventListener('DOMContentLoaded', () => {
    try {
        initializePage(); // Initialize the page after loading nav and footer
    } catch (error) {
        console.error('ERROR LOADING PAGE CONTENT:', error);
    }
});
