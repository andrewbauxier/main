// project: aaDesign
// module: nav.js
// author: andrew b. auxier

// Function to load the navigation bar content
function loadNav() {
    console.log('Loading navigation...');
    return fetch('nav.html')
        .then((response) => {
            if (!response.ok) throw new Error(`FAILED TO LOAD nav.html: ${response.statusText}`);
            return response.text();
        })
        .then((data) => {
            try {
                console.log('Navigation content loaded. Inserting into DOM...');
                document.querySelector('nav').innerHTML = data;
            } catch (error) {
                console.error('ERROR INSERTING NAVIGATION CONTENT:', error);
            }
        })
        .catch((error) => {
            console.error('ERROR LOADING NAV:', error);
        });
}

// Function to generate breadcrumbs dynamically based on the URL path.
function generateBreadcrumb() {
    console.log('Generating breadcrumbs...');
    const breadcrumbContainer = document.querySelector('.breadcrumbs-container ol');
    if (!breadcrumbContainer) {
        console.warn('Breadcrumb container not found.');
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
