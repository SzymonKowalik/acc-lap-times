let checkbox = document.querySelector('#hide_empty');

checkbox.addEventListener('click', () => {
    let checkbox_state = checkbox.checked;
    let empty = document.querySelectorAll('.empty');

    if (checkbox_state === true) {
        empty.forEach(row => {
        row.hidden = true;
        })
    } else {
        empty.forEach(row => {
        row.hidden = false;
        })
    }
})
