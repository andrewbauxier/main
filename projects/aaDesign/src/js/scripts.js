// project: aaDesign
// module: scripts.js
// author: andrew b. auxier

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
                document.getElementById('nav-services').textContent = translations.nav.services;
                document.getElementById('nav-portfolio').textContent = translations.nav.portfolio;
                document.getElementById('nav-legal').textContent = translations.nav.legal;
                
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
                    document.getElementById('landing-serviceFeesTitle').textContent = translations.landing.serviceFeesTitle;
                    document.getElementById('landing-translationServiceButton').textContent = translations.landing.translationServiceButton;
                    document.getElementById('landing-designServiceButton').textContent = translations.landing.designServiceButton;
                }
                // Update Services page content
                if (document.getElementById('services-title')) {
                    document.getElementById('services-center1').textContent = translations.services.center1;
                    document.getElementById('services-center2Bold').textContent = translations.services.center2Bold;
                    document.getElementById('services-center2').textContent = translations.services.center2;
                    document.getElementById('services-center3').textContent = translations.services.center3;

                }
            } catch (error) {
                console.error('ERROR UPDATING LANDING PAGE CONTENT:', error);
            }
        })
        .catch((error) => {
            console.error('ERROR LOADING TRANSLATIONS:', error);
        });
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
                handleLanguageSwitch();
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
