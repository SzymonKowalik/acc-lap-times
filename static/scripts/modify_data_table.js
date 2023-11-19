let checkbox = document.querySelector('#hide_empty');
const get_params = new URLSearchParams(window.location.search);

// Function to change the state of rows based on the checkbox state
function change_rows_hidden_state() {
    let checkbox_state = checkbox.checked;
    let empty = document.querySelectorAll('.empty');

    if (checkbox_state === true) {
        empty.forEach(row => {row.hidden = true;})
    } else {
        empty.forEach(row => {row.hidden = false;})
    }
}

// Check if 'hide_empty' parameter is present and has the value 'on' in the URL
if (get_params.has('hide_empty') && get_params.get('hide_empty') === 'on') {
    checkbox.checked = true;
    change_rows_hidden_state();
}

// Iterate through all query parameters and set the selected option in corresponding select elements
get_params.forEach((value, key) => {
    let options = document.querySelector(`#${key}`);
    for (let i=0; i<options.length; i++) {
        if (options[i].value === value) {
            options[i].selected = true;
        }
    }
})
