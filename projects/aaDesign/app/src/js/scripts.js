// project: aaDesign
// module: scripts.js
// author: andrew b. auxier

// The default locale of the website, which is JP (base text in HTML is Japanese)
const defaultLocale = 'jp';
let locale;
let translations = {};

// Function to handle the light/dark mode toggle
function handleModeSwitch() {
    console.log("Initializing mode switcher...");
    const modeSwitcher = document.getElementById('mode-switcher');
    if (!modeSwitcher) {
        console.error("Mode switcher element not found!");
        return;
    }
    const selectedMode = localStorage.getItem('mode') || 'light';
    console.log("Selected mode from localStorage:", selectedMode);
    document.body.classList.toggle('mode', selectedMode === 'dark');
    modeSwitcher.value = selectedMode;

    modeSwitcher.addEventListener('change', (event) => {
        const selectedMode = event.target.value;
        console.log("Mode changed to:", selectedMode);
        document.body.classList.toggle('mode', selectedMode === 'dark');
        localStorage.setItem('mode', selectedMode);
    });
}

// Function to handle language switching
function handleLanguageSwitch() {
    console.log("Initializing language switcher...");
    const languageSwitcher = document.getElementById('language-switcher');
    if (!languageSwitcher) {
        console.error("Language switcher element not found!");
        return;
    }
    const selectedLanguage = localStorage.getItem('language') || defaultLocale;
    console.log("Selected language from localStorage:", selectedLanguage);
    languageSwitcher.value = selectedLanguage;

    languageSwitcher.addEventListener('change', (event) => {
        const selectedLanguage = event.target.value;
        console.log("Language changed to:", selectedLanguage);
        setLocale(selectedLanguage);
        localStorage.setItem('language', selectedLanguage);
    });

    setLocale(selectedLanguage);
}

// Function to load translations for the given locale and translate the page
async function setLocale(newLocale) {
    console.log("Setting locale to:", newLocale);
    if (newLocale === locale) {
        console.log("Locale is the same as the current locale. No change needed.");
        return;
    }

    if (newLocale === 'jp') {
        locale = newLocale;
        console.log("Resetting to base Japanese text.");
        resetToBaseText();
    } else {
        try {
            console.log("Fetching translations for locale:", newLocale);
            const newTranslations = await fetchTranslationsFor(newLocale);
            locale = newLocale;
            translations = newTranslations;
            console.log("Translations loaded:", translations);
            translatePage();
        } catch (error) {
            console.error("Error loading translations:", error);
        }
    }
}

// Function to fetch the translations JSON object for the given locale over the network
async function fetchTranslationsFor(newLocale) {
    console.log("Fetching translations from:", `/translations/${newLocale}.json`);
    const response = await fetch(`/translations/${newLocale}.json`);
    if (!response.ok) {
        throw new Error(`Failed to fetch translations: ${response.statusText}`);
    }
    return await response.json();
}

// Function to replace the inner text of each element with the translation corresponding to its class-based key
function translatePage() {
    console.log("Translating page content...");
    document.querySelectorAll('.translate').forEach(translateElement);
}

// Function to replace the inner text of the given HTML element with the translation in the active locale
function translateElement(element) {
    console.log("Translating element:", element);
    if (!element.hasAttribute('data-original-text')) {
        element.setAttribute('data-original-text', element.innerText);
    }
    const key = Array.from(element.classList).find((cls) => cls !== 'translate');
    if (!key) {
        console.warn("No translation key found in classes for element:", element);
        return;
    }
    const translation = translations[key];
    if (translation) {
        element.innerText = translation;
    } else {
        console.warn(`Translation for key "${key}" not found.`);
    }
}

// Function to reset the page content to the base Japanese text
function resetToBaseText() {
    console.log("Resetting page content to base Japanese text...");
    document.querySelectorAll('.translate').forEach((element) => {
        const originalText = element.getAttribute('data-original-text');
        if (originalText) {
            element.innerText = originalText;
        }
    });
}

// Function to load the navigation bar content
function loadNav() {
    console.log("Loading navigation...");
    return fetch('nav.html')
        .then((response) => {
            if (!response.ok) throw new Error(`FAILED TO LOAD nav.html: ${response.statusText}`);
            return response.text();
        })
        .then((data) => {
            try {
                console.log("Navigation content loaded. Inserting into DOM...");
                document.querySelector('nav').innerHTML = data;
            } catch (error) {
                console.error("ERROR INSERTING NAVIGATION CONTENT:", error);
            }
        })
        .catch((error) => {
            console.error("ERROR LOADING NAV:", error);
        });
}

// Function to load the footer content
function loadFooter() {
    console.log("Loading footer...");
    return fetch('footer.html')
        .then((response) => {
            if (!response.ok) throw new Error(`FAILED TO LOAD footer.html: ${response.statusText}`);
            return response.text();
        })
        .then((data) => {
            try {
                console.log("Footer content loaded. Inserting into DOM...");
                document.querySelector('footer').innerHTML = data;
            } catch (error) {
                console.error("ERROR INSERTING FOOTER CONTENT:", error);
            }
        })
        .catch((error) => {
            console.error("ERROR LOADING FOOTER:", error);
        });
}

// Function to generate breadcrumbs dynamically based on the URL path.
function generateBreadcrumb() {
    console.log("Generating breadcrumbs...");
    const breadcrumbContainer = document.querySelector('.breadcrumbs-container ol');
    if (!breadcrumbContainer) {
        console.warn("Breadcrumb container not found.");
        return;
    }

    const pathArray = window.location.pathname
        .split('/')
        .filter((part) => part && !['js', 'img', 'fonts'].includes(part));

    breadcrumbContainer.innerHTML = '';
    const homeLink = document.createElement('li');
    homeLink.innerHTML = `<a href="/src/landing.html"></a>`;
    breadcrumbContainer.appendChild(homeLink);

    let accumulatedPath = '/src/';
    pathArray.forEach((segment, index) => {
        if (segment === 'src') return;
        accumulatedPath += segment + '/';
        const isLast = index === pathArray.length - 1;
        const breadcrumbItem = document.createElement('li');
        if (isLast) {
            breadcrumbItem.textContent = segment.replace('.html', '').replace(/-/g, ' ');
            breadcrumbItem.setAttribute('aria-current', 'page');
        } else {
            breadcrumbItem.innerHTML = `<a href="${accumulatedPath}">${segment
                .replace('.html', '')
                .replace(/-/g, ' ')}</a>`;
        }
        breadcrumbContainer.appendChild(breadcrumbItem);
    });
}

// Function to ensure both the nav and footer are loaded before running translations
function initializePage() {
    console.log("Initializing page...");
    try {
        Promise.all([loadNav(), loadFooter()])
            .then(() => {
                console.log("Nav and footer loaded. Initializing other features...");
                // Add these later if we feel like it
                // handleLanguageSwitch();
                // handleModeSwitch();
                generateBreadcrumb();
            })
            .catch((error) => {
                console.error("ERROR INITIALIZING PAGE PROMISE:", error);
            });
    } catch (error) {
        console.error("ERROR INITIALIZING PAGE:", error);
    }
}

// Initialize page after content is loaded
document.addEventListener('DOMContentLoaded', initializePage);
