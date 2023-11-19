let checkbox = document.querySelector('#hide_empty');
const getParams = new URLSearchParams(window.location.search);

// Function to change the state of rows based on the checkbox state
function changeRowsHiddenState() {
    let checkboxState = checkbox.checked;
    let empty = document.querySelectorAll('.empty');

    if (checkboxState === true) {
        empty.forEach(row => {row.hidden = true;})
    } else {
        empty.forEach(row => {row.hidden = false;})
    }
}

// Check if 'hide_empty' parameter is present and has the value 'on' in the URL
if (getParams.has('hide_empty') && getParams.get('hide_empty') === 'on') {
    checkbox.checked = true;
    changeRowsHiddenState();
}

// Iterate through all query parameters and set the selected option in corresponding select elements
getParams.forEach((value, key) => {
    let options = document.querySelector(`#${key}`);
    for (let i=0; i<options.length; i++) {
        if (options[i].value === value) {
            options[i].selected = true;
        }
    }
})
