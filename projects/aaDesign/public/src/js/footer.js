// project: aaDesign
// module: footer.js
// author: andrew b. auxier

// Function to load the footer content
function loadFooter() {
    console.log('Loading footer...');
    return fetch('footer.html')
        .then((response) => {
            if (!response.ok) throw new Error(`FAILED TO LOAD footer.html: ${response.statusText}`);
            return response.text();
        })
        .then((data) => {
            try {
                console.log('Footer content loaded. Inserting into DOM...');
                document.querySelector('footer').innerHTML = data;
            } catch (error) {
                console.error('ERROR INSERTING FOOTER CONTENT:', error);
            }
        })
        .catch((error) => {
            console.error('ERROR LOADING FOOTER:', error);
        });
}
