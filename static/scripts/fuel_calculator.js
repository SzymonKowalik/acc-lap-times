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

    if (isNaN(fuelCapacity) || fuelCapacity <= 0) {fuelCapacity = Infinity};

    let stints = Math.ceil(fuelNeeded / fuelCapacity);
    console.log(fuelCapacity / fuelNeeded, stints)
    let lastStint = fuelNeeded % fuelCapacity;

    if (fuelNeeded) {
        let totalLapsText = `Total laps: ${laps}.<br>`
        let fuelNeededText = `Fuel needed: ${fuelNeeded.toFixed(1)} liters.<br>`;
        let fuelNeededSafeText = `Fuel needed (safe): ${fuelSafe.toFixed(1)} liters.<br>`;

        if (stints <= 1 || stints === Infinity) {
            document.getElementById("result").innerHTML = `${totalLapsText}${fuelNeededText}${fuelNeededSafeText}`;
        } else {
            let stintsText = `Total stints number: ${stints}.<br>`;
            let lastStintText = `Last stint fuel: ${lastStint.toFixed(1)}.<br>`;

            document.getElementById("result").innerHTML = `${totalLapsText}${fuelNeededText}
            ${fuelNeededSafeText}<br>${stintsText}${lastStintText}`;
        }
    } else {
        document.getElementById("result").innerHTML = `Enter correct data.`;
    }

}
