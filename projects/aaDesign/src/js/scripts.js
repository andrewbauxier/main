// project: aaDesign
// module: scripts.js
// author: andrew b. auxier

// The default locale our app first shows
const defaultLocale = "en";

// The active locale
let locale;

// Gets filled with active locale translations
let translations = {};

// Function to toggle between light and dark mode
function handleModeSwitch() {
    const modeSwitcher = document.getElementById('mode-switcher');
    const selectedMode = localStorage.getItem('mode') || 'light';
    document.body.classList.toggle('mode', selectedMode === 'dark');
    modeSwitcher.value = selectedMode;

    modeSwitcher.addEventListener('change', (event) => {
        const selectedMode = event.target.value;
        document.body.classList.toggle('mode', selectedMode === 'dark');
        localStorage.setItem('mode', selectedMode);
    });
}

// Function to handle language switching
function handleLanguageSwitch() {
    const languageSwitcher = document.getElementById('language-switcher');
    const selectedLanguage = localStorage.getItem('language') || defaultLocale;

    languageSwitcher.value = selectedLanguage;
    languageSwitcher.addEventListener('change', (event) => {
        const selectedLanguage = event.target.value;
        setLocale(selectedLanguage);
        localStorage.setItem('language', selectedLanguage);
    });

    setLocale(selectedLanguage); // Initialize locale on page load
}

// Load translations for the given locale and translate the page
async function setLocale(newLocale) {
    if (newLocale === locale) return;
    const newTranslations = await fetchTranslationsFor(newLocale);
    locale = newLocale;
    translations = newTranslations;
    translatePage();
}

// Fetch translations JSON object for the given locale over the network
async function fetchTranslationsFor(newLocale) {
    const response = await fetch(`/translations/${newLocale}.json`);
    if (!response.ok) throw new Error(`Failed to fetch translations: ${response.statusText}`);
    return await response.json();
}

// Function to access nested properties safely
function getNestedTranslation(obj, key) {
    return key.split('.').reduce((o, k) => {
        if (o === undefined || o === null) {
            throw new Error(`Path "${key}" is invalid. "${k}" is not found in the object.`);
        }
        return o[k];
    }, obj);
}

// Replace the inner text of each element that has a
// data-i18n-key attribute with the translation corresponding
// to its data-i18n-key or id
function translatePage() {
    document.querySelectorAll("[data-i18n-key], [id]").forEach(translateElement);
}

// Replace the inner text of the given HTML element
// with the translation in the active locale
function translateElement(element) {
    // Use data-i18n-key if present, fall back to id if not
    const key = element.getAttribute("data-i18n-key") || element.id;
    if (!key) {
        console.warn(`No data-i18n-key or id found for element:`, element);
        return;
    }
    
    // Retrieve the translation using the nested key approach
    const translation = getNestedTranslation(translations, key);
    if (translation) {
        element.innerText = translation;
    } else {
        console.warn(`Translation for key "${key}" not found.`);
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

// Function to generate breadcrumb dynamically based on the URL path
function generateBreadcrumb() {
    const breadcrumbContainer = document.querySelector(".breadcrumbs-container ol");
    if (!breadcrumbContainer) return; // Exit if the breadcrumb container doesn't exist

    // Get the current path and split it into parts, filtering out non-user-facing directories
    const pathArray = window.location.pathname
        .split("/")
        .filter(part => part && !["js", "img", "fonts"].includes(part)); // Filter out irrelevant directories

    // Clear existing breadcrumb content
    breadcrumbContainer.innerHTML = "";

    // Create and add the "Home" link
    const homeLink = document.createElement("li");
    homeLink.innerHTML = `<a href="/src/landing.html"></a>`;
    breadcrumbContainer.appendChild(homeLink);

    // Initialize the accumulated path, starting from "/src/"
    let accumulatedPath = "/src/";

    // Build the breadcrumb from the URL path
    pathArray.forEach((segment, index) => {
        // Skip adding "src" to avoid "src/src" duplication
        if (segment === "src") return;

        accumulatedPath += segment + "/";
        const isLast = index === pathArray.length - 1;

        // Create the breadcrumb item
        const breadcrumbItem = document.createElement("li");
        if (isLast) {
            // For the last item, display it as plain text without ".html"
            breadcrumbItem.textContent = segment.replace(".html", "").replace(/-/g, " ");
            breadcrumbItem.setAttribute("aria-current", "page");
        } else {
            // For intermediate items, make them clickable links
            breadcrumbItem.innerHTML = `<a href="${accumulatedPath}">${segment.replace(".html", "").replace(/-/g, " ")}</a>`;
        }
        breadcrumbContainer.appendChild(breadcrumbItem);
    });
}

// Function to ensure both the nav and footer are loaded before running translations
function initializePage() {
    try {
        Promise.all([loadNav(), loadFooter()])
            .then(() => {
                handleLanguageSwitch();  // Load and set the locale
                handleModeSwitch();       // Initialize mode switcher
                generateBreadcrumb();     // Generate breadcrumb after loading nav
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
