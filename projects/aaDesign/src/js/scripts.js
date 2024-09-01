// project: aaDesign
// module: scripts.js
// author: andrew b. auxier

// The default locale of the website, which is JP (base text in html is Japanese)
const defaultLocale = 'jp';

// Variable to keep track of the current active locale
let locale;

// Empty object to hold the active locale's translations
let translations = {};

// Function to handle the light/dark mode toggle.
function handleModeSwitch() {
    // Get the mode switcher element (dropdown).
    const modeSwitcher = document.getElementById('mode-switcher');
    // Check if there's a saved mode in localStorage, default to 'light' if not.
    const selectedMode = localStorage.getItem('mode') || 'light';
    // Toggle the 'mode' class on the body to switch modes based on the selected mode.
    document.body.classList.toggle('mode', selectedMode === 'dark');
    // Set the mode switcher dropdown to reflect the current mode.
    modeSwitcher.value = selectedMode;

    // Add an event listener to handle changes when the user selects a different mode.
    modeSwitcher.addEventListener('change', (event) => {
        const selectedMode = event.target.value;
        // Toggle the mode class on the body based on the selected mode.
        document.body.classList.toggle('mode', selectedMode === 'dark');
        // Save the selected mode in localStorage.
        localStorage.setItem('mode', selectedMode);
    });
}

// Function to handle language switching
function handleLanguageSwitch() {
    // Get the language switcher element (dropdown)
    const languageSwitcher = document.getElementById('language-switcher');
    // Check if there's a saved language in localStorage, default to the base text (Japanese) if not
    const selectedLanguage = localStorage.getItem('language') || defaultLocale;

    // Set the language switcher dropdown to reflect the current language
    languageSwitcher.value = selectedLanguage;

    // Add an event listener to handle changes when the user selects a different language
    languageSwitcher.addEventListener('change', (event) => {
        const selectedLanguage = event.target.value;
        // If the selected language is 'en', load the English translations
        if (selectedLanguage === 'en') {
            setLocale('en');
        } else {
            // If the selected language is 'jp', revert to the base Japanese text
            setLocale('jp');
        }
        // Save the selected language in localStorage
        localStorage.setItem('language', selectedLanguage);
    });

    // Set the locale initially based on the selected language or default
    setLocale(selectedLanguage);
}

// Function to load translations for the given locale and translate the page
async function setLocale(newLocale) {
    // If the new locale is the same as the current locale, do nothing
    if (newLocale === locale) return;

    if (newLocale === 'jp') {
        // If the new locale is 'jp', reset the page to the base Japanese text
        locale = newLocale;
        resetToBaseText();
    } else {
        // If the new locale is 'en', load the English translations
        const newTranslations = await fetchTranslationsFor(newLocale);
        locale = newLocale;
        translations = newTranslations;
        // Translate the page content based on the loaded English translations
        translatePage();
    }
}

// Function to fetch the translations JSON object for the given locale over the network
async function fetchTranslationsFor(newLocale) {
    // Fetch the translation file for the selected locale
    const response = await fetch(`/translations/${newLocale}.json`);
    if (!response.ok) throw new Error(`Failed to fetch translations: ${response.statusText}`);
    return await response.json(); // Return the parsed JSON content
}

// Function to replace the inner text of each element that has a
// 'translate' class with the translation corresponding to its class-based key
function translatePage() {
    // Select all elements with the 'translate' class and pass them to the translateElement function
    document.querySelectorAll('.translate').forEach(translateElement);
}

// Function to replace the inner text of the given HTML element
// with the translation in the active locale
function translateElement(element) {
    // Store the original text in a custom attribute if not already stored
    if (!element.hasAttribute('data-original-text')) {
        element.setAttribute('data-original-text', element.innerText);
    }

    // Assume the translation key is the second class in the class list
    const key = Array.from(element.classList).find((cls) => cls !== 'translate');
    if (!key) {
        console.warn(`No translation key found in classes for element:`, element);
        return;
    }

    // Retrieve the translation from the loaded translations object using the key
    const translation = translations[key];
    if (translation) {
        element.innerText = translation; // Set the element's text to the translation
    } else {
        console.warn(`Translation for key "${key}" not found.`);
    }
}

// Function to reset the page content to the base Japanese text
function resetToBaseText() {
    document.querySelectorAll('.translate').forEach((element) => {
        // Restore the original content from the custom attribute
        const originalText = element.getAttribute('data-original-text');
        if (originalText) {
            element.innerText = originalText;
        }
    });
}

// Function to load the navigation bar content
function loadNav() {
    return fetch('nav.html')
        .then((response) => {
            if (!response.ok) throw new Error(`FAILED TO LOAD nav.html: ${response.statusText}`);
            return response.text();
        })
        .then((data) => {
            try {
                document.querySelector('nav').innerHTML = data; // Insert the fetched navigation content into the <nav> element
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
        .then((response) => {
            if (!response.ok) throw new Error(`FAILED TO LOAD footer.html: ${response.statusText}`);
            return response.text();
        })
        .then((data) => {
            try {
                document.querySelector('footer').innerHTML = data; // Insert the fetched footer content into the <footer> element.
            } catch (error) {
                console.error('ERROR INSERTING FOOTER CONTENT:', error);
            }
        })
        .catch((error) => {
            console.error('ERROR LOADING FOOTER:', error);
        });
}

// Function to generate breadcrumbs dynamically based on the URL path.
function generateBreadcrumb() {
    const breadcrumbContainer = document.querySelector('.breadcrumbs-container ol');
    if (!breadcrumbContainer) return; // Exit if the breadcrumb container doesn't exist

    // Get the current path and split it into parts, filtering out non-user-facing directories
    const pathArray = window.location.pathname
        .split('/')
        .filter((part) => part && !['js', 'img', 'fonts'].includes(part)); // Filter out irrelevant directories.

    // Clear existing breadcrumb content
    breadcrumbContainer.innerHTML = '';

    // Create and add the "Home" link
    const homeLink = document.createElement('li');
    homeLink.innerHTML = `<a href="/src/landing.html"></a>`;
    breadcrumbContainer.appendChild(homeLink);

    // Initialize the accumulated path, starting from "/src/"
    let accumulatedPath = '/src/';

    // Build the breadcrumb from the URL path.
    pathArray.forEach((segment, index) => {
        if (segment === 'src') return; // Skip adding "src" to avoid "src/src" duplication

        accumulatedPath += segment + '/';
        const isLast = index === pathArray.length - 1;

        const breadcrumbItem = document.createElement('li');
        if (isLast) {
            // For the last item, display it as plain text without ".html"
            breadcrumbItem.textContent = segment.replace('.html', '').replace(/-/g, ' ');
            breadcrumbItem.setAttribute('aria-current', 'page');
        } else {
            // For intermediate items, make them clickable links.
            breadcrumbItem.innerHTML = `<a href="${accumulatedPath}">${segment
                .replace('.html', '')
                .replace(/-/g, ' ')}</a>`;
        }
        breadcrumbContainer.appendChild(breadcrumbItem);
    });
}

// Function to ensure both the nav and footer are loaded before running translations
function initializePage() {
    try {
        // Load navigation and footer, then initialize other features
        Promise.all([loadNav(), loadFooter()])
            .then(() => {
                handleLanguageSwitch(); // Initialize language switcher and set the locale
                handleModeSwitch(); // Initialize mode switcher
                generateBreadcrumb(); // Generate breadcrumb after loading nav
            })
            .catch((error) => {
                console.error('ERROR INITIALIZING PAGE PROMISE:', error);
            });
    } catch (error) {
        console.error('ERROR INITIALIZING PAGE:', error);
    }
}

// Initialize page after content is loaded
document.addEventListener('DOMContentLoaded', initializePage);
