let checkbox = document.querySelector('#hide_empty');

checkbox.addEventListener('click', () => {
    let checkbox_state = checkbox.checked;
    let table_all = document.querySelector('#data_not_empty');
    let table_not_empty = document.querySelector('#data_empty');


    if (checkbox_state === true) {
        table_all.hidden = true;
        table_not_empty.hidden = false;
    } else {
        table_all.hidden = false;
        table_not_empty.hidden = true;
    }
})
