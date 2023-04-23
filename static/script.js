console.log('Script connected.');

// get dom elements
const card = document.querySelector('.card');
const form = document.getElementById('url-form');
const urlInput = document.getElementById('txt-input');
const submitBtn = document.getElementById('submit');
const displayArea = document.getElementById('display-area');

const displayErrorMessage = message => {
    // check if message already on page
    const existing = document.querySelectorAll('.error');

    if (existing.length > 0) {
        return existing[0].innerText = message;
    };

    const errorNode = document.createElement('p');
    errorNode.className = 'error';
    errorNode.innerText = message;

    card.append(errorNode);
};

const removeErrorMessage = () => {
    // get existing message if exists
    const existing = document.querySelectorAll('.error');

    for (let i = 0; i < existing.length; i++) {
        existing[i].remove();
    };
};

const formSubmit = async e => {
    e.preventDefault();

    removeErrorMessage();

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
        return displayErrorMessage('Error making request. Please check that you have entered a valid URL.');
    };

    console.log(response);

    displayArea.innerText = window.location.href.slice(0, window.location.href.length-1) + response.id;
};

form.addEventListener('submit', formSubmit);