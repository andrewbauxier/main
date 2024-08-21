// project: aaDesign
// module: scripts.js
// author: andrew b. auxier

// Function to toggle between light and dark mode
function toggleMode() {
    try {
        // Debug log to check if the function is executing
        console.log('Mode toggled');
        
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
            if (!response.ok) throw new Error(`Failed to fetch translations: ${response.statusText}`);
            return response.json();
        })
        .then((translations) => {
            console.log('Loaded Translations:', translations);

            // Update navigation content
            try {
                document.getElementById('nav-about').textContent = translations.nav.about;
                document.getElementById('nav-services').textContent = translations.nav.services;
                document.getElementById('nav-legal').textContent = translations.nav.legal;
                document.getElementById('nav-menu').textContent = translations.nav.menu;
            } catch (error) {
                console.error('ERROR UPDATING NAVIGATION CONTENT:', error);
            }

            // Update footer content
            try {
                document.getElementById('footer').textContent = translations.footer.copyright;
            } catch (error) {
                console.error('ERROR UPDATING FOOTER CONTENT:', error);
            }

            // Update landing page content
            try {
                if (document.getElementById('landing-aboutUsTitle')) {
                    document.getElementById('landing-aboutUsTitle').textContent = translations.landing.aboutUsTitle;
                    document.getElementById('landing-aboutUsText').textContent = translations.landing.aboutUsText;

                    document.getElementById('landing-aboutUsSubheading1').textContent = translations.landing.aboutUsSubheading1;
                    document.getElementById('landing-aboutUsSubtext1').textContent = translations.landing.aboutUsSubtext1;
                    document.getElementById('landing-aboutUsSubheading2').textContent = translations.landing.aboutUsSubheading2;
                    document.getElementById('landing-aboutUsSubtext2').textContent = translations.landing.aboutUsSubtext2;

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
        const selectedLanguage = localStorage.getItem('language') || 'en';
        loadTranslations(selectedLanguage);

        languageSwitcher.value = selectedLanguage;
        languageSwitcher.addEventListener('change', (event) => {
            const selectedLanguage = event.target.value;
            loadTranslations(selectedLanguage);
            localStorage.setItem('language', selectedLanguage);
        });
    } catch (error) {
        console.error('ERROR HANDLING LANGUAGE SWITCH:', error);
    }
}

// Function to load the navigation bar content
function loadNav() {
    return fetch('nav.html')
        .then(response => {
            if (!response.ok) throw new Error(`FAILED TO LOAD nav.html: ${response.statusText}`);
            return response.text();
        })
        .then(data => {
            try {
                document.querySelector('nav').innerHTML = data;
                
                // Add event listener for the mode toggle checkbox
                const modeToggleCheckbox = document.getElementById('toggle-mode-checkbox');
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
            if (!response.ok) throw new Error(`FAILED TO LOAD footer.html: ${response.statusText}`);
            return response.text();
        })
        .then(data => {
            try {
                document.querySelector('footer').innerHTML = data;
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
            .then(handleLanguageSwitch)
            .catch((error) => {
                console.error('ERROR INITIALIZING PAGE PROMISE:', error);
            });
    } catch (error) {
        console.error('ERROR INITIALIZING PAGE:', error);
    }
}

// Initialize page after content is loaded
document.addEventListener('DOMContentLoaded', initializePage);
