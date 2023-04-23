console.log('Script connected.');

// get dom elements
const form = document.getElementById('url-form');
const urlInput = document.getElementById('txt-input');
const submitBtn = document.getElementById('submit');
const displayArea = document.getElementById('display-area');

const formSubmit = async e => {
    e.preventDefault();

    const urlToShorten = urlInput.value;
    if (!urlToShorten) return;

    const res = await fetch('/api/url', {
        method: 'POST',
        body: JSON.stringify({
            url: urlToShorten
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const response = await res.json();

    if (!res.ok) {
        // TODO: append error message
        console.log(response);
        return;
    };

    console.log(response);

    displayArea.innerText = window.location.href.slice(0, window.location.href.length-1) + response.id;
};

form.addEventListener('submit', formSubmit);