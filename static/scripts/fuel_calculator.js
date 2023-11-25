document.querySelector(".calc-submit").addEventListener('click', fuelCalculator);

function fuelCalculator() {
    let raceH = parseFloat(document.getElementById('race_h').value);
    let raceMin = parseFloat(document.getElementById('race_min').value);
    let lapMin = parseFloat(document.getElementById('lap_min').value);
    let lapSec = parseFloat(document.getElementById('lap_sec').value);
    let fuelPerLap = parseFloat(document.getElementById('fuel_per_lap').value);
    let fuelCapacity = parseFloat(document.getElementById('fuel_capacity').value);

    let raceTime = (raceH * 3600) + (raceMin * 60);
    let lapTime = (lapMin * 60) + lapSec;

    let laps = Math.ceil(raceTime / lapTime);
    let fuelNeeded = laps * fuelPerLap;
    let fuelSafe = fuelNeeded * 1.15;

    if (isNaN(fuelCapacity) || fuelCapacity <= 0) {
        fuelCapacity = Infinity
    }

    let stints = Math.ceil(fuelNeeded / fuelCapacity);
    let lastStint = fuelNeeded % fuelCapacity;
    let container = document.getElementById("result-container");
    container.innerHTML = ''; // clear past results

    if (fuelNeeded) {
        generateResultBox(container, 'Total Laps', laps);
        generateResultBox(container, 'Fuel Needed', fuelNeeded.toFixed(1));
        generateResultBox(container, 'Fuel Needed (safe)', fuelSafe.toFixed(1));

        if (stints > 1 && stints !== Infinity) {
            generateResultBox(container, 'Total stints', stints);
            generateResultBox(container, 'Last Stint Fuel', lastStint.toFixed(1));
        }
    } else {
        generateResultBox(container, 'Fill missing inputs', '');
    }
}


function generateResultBox(container, title, info) {
        let boxDiv = document.createElement("div");
        boxDiv.classList.add("calc-result-box");

        let titleDiv = document.createElement("div");
        titleDiv.classList.add("calc-result-title");
        titleDiv.textContent = title;

        let infoDiv = document.createElement("div");
        infoDiv.classList.add("calc-result-info");
        infoDiv.textContent = info;

        boxDiv.appendChild(titleDiv);
        boxDiv.appendChild(infoDiv);

        container.appendChild(boxDiv)
}

