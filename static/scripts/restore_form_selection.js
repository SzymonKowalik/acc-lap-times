const getParams = new URLSearchParams(window.location.search);

// Iterate through all query parameters and set the selected option in corresponding select elements
getParams.forEach((value, key) => {
    let options = document.querySelector(`#${key}`);
    for (let i=0; i<options.length; i++) {
        if (options[i].value === value) {
            options[i].selected = true;
        }
    }
})
