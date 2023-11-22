let raceTimes = document.querySelectorAll('.race_time');

function timeToSeconds(timeParts) {
    const raceTimeConversion = [3600, 60, 1];
    let timeSeconds = 0;
    for (let i=0; i<timeParts.length; i++) {
        timeSeconds += timeParts[i] * raceTimeConversion[i];
    }
    return timeSeconds
}

function format(time) {
    return ("0" + String(time)).slice(-2);
}

function secondsToTime(fromSeconds) {
    let hours = Math.floor((fromSeconds % (60 * 60 * 24)) / (60 * 60));
    let minutes = Math.floor((fromSeconds % (60 * 60)) / 60);
    let seconds = Math.floor(fromSeconds % 60);
    return `${format(hours)}:${format(minutes)}:${format(seconds)}`
}

function updateTime() {
    raceTimes.forEach(raceTime => {
        const raceTimeParts = raceTime.textContent.split(":");
        if (raceTimeParts.length != 1) {
            let raceTimeSeconds = timeToSeconds(raceTimeParts) - 1;
            raceTime.textContent = (raceTimeSeconds <= 0) ? 'Started' :  secondsToTime(raceTimeSeconds);
        }
    })
}

updateTime();
setInterval(updateTime, 1000);

