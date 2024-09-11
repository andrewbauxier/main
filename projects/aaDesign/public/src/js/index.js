// project: aaDesign
// module: index.js
// author: andrew b. auxier

// Function to initialize the page
function initializePage() {
    console.log('Initializing page...');
    try {
        Promise.all([loadNav(), loadFooter()])
            .then(() => {
                console.log('Nav and footer loaded. Initializing other features...');
                generateBreadcrumb();
            })
            .catch((error) => {
                console.error('ERROR INITIALIZING PAGE PROMISE:', error);
            });
    } catch (error) {
        console.error('ERROR INITIALIZING PAGE:', error);
    }
}

// Event listener for DOMContentLoaded
document.addEventListener('DOMContentLoaded', initializePage);
