function fuelCalculator() {
    let race_h = parseFloat(document.getElementById('race_h').value);
    let race_min = parseFloat(document.getElementById('race_min').value);
    let lap_min = parseFloat(document.getElementById('lap_min').value);
    let lap_sec = parseFloat(document.getElementById('lap_sec').value);
    let fuel_per_lap = parseFloat(document.getElementById('fuel_per_lap').value);

    let race_time = (race_h * 3600) + (race_min * 60);
    let lap_time = (lap_min * 60) + lap_sec;

    let laps = Math.ceil(race_time / lap_time);
    let fuel_needed = laps * fuel_per_lap;
    let fuel_safe = fuel_needed * 1.1;

    if (fuel_needed) {
        document.getElementById("result").innerHTML = `Fuel needed: ${fuel_needed.toFixed(1)} liters.
            <br>Fuel needed (safe): ${fuel_safe.toFixed(1)} liters.<br>Total laps: ${laps}.`;
    } else {
        document.getElementById("result").innerHTML = `Enter correct data.`;
    }

}
