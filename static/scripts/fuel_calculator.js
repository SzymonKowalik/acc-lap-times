function fuelCalculator() {
    let race_h = parseFloat(document.getElementById('race_h').value);
    let race_min = parseFloat(document.getElementById('race_min').value);
    let lap_min = parseFloat(document.getElementById('lap_min').value);
    let lap_sec = parseFloat(document.getElementById('lap_sec').value);
    let fuel_per_lap = parseFloat(document.getElementById('fuel_per_lap').value);
    let fuel_capacity = parseFloat(document.getElementById('fuel_capacity').value);

    let race_time = (race_h * 3600) + (race_min * 60);
    let lap_time = (lap_min * 60) + lap_sec;

    let laps = Math.ceil(race_time / lap_time);
    let fuel_needed = laps * fuel_per_lap;
    let fuel_safe = fuel_needed * 1.1;

    if (isNaN(fuel_capacity) || fuel_capacity <= 0) {fuel_capacity = Infinity};

    let stints = Math.ceil(fuel_needed / fuel_capacity);
    console.log(fuel_capacity / fuel_needed, stints)
    let last_stint = fuel_needed % fuel_capacity;

    if (fuel_needed) {
        let total_laps_text = `Total laps: ${laps}.<br>`
        let fuel_needed_text = `Fuel needed: ${fuel_needed.toFixed(1)} liters.<br>`;
        let fuel_needed_safe_text = `Fuel needed (safe): ${fuel_safe.toFixed(1)} liters.<br>`;

        if (stints <= 1 || stints === Infinity) {
            document.getElementById("result").innerHTML = `${total_laps_text}${fuel_needed_text}${fuel_needed_safe_text}`;
        } else {
            let stints_text = `Total stints number: ${stints}.<br>`;
            let last_stint_text = `Last stint fuel: ${last_stint.toFixed(1)}.<br>`;

            document.getElementById("result").innerHTML = `${total_laps_text}${fuel_needed_text}
            ${fuel_needed_safe_text}<br>${stints_text}${last_stint_text}`;

        }

    } else {
        document.getElementById("result").innerHTML = `Enter correct data.`;
    }

}
