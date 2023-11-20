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
    raceTimesSaved.forEach(raceObject => {

        const raceTimeParts = raceObject.timeText.split(":");
        let now = new Date();
        const currentTimeParts = [now.getHours(), now.getMinutes(), now.getSeconds()];
        let raceTimeSeconds = timeToSeconds(raceTimeParts);

        let currentTimeSeconds = timeToSeconds(currentTimeParts);
        let timeDiff = raceTimeSeconds - currentTimeSeconds;
        let timeText = secondsToTime(timeDiff);
        raceObject.divObject.textContent = `Upcoming race in ${timeText}`;
    })
}

let raceTimesSaved = [];
raceTimes.forEach(raceTime => {
    let raceObject = {};
    raceObject.divObject = raceTime;
    raceObject.timeText = raceTime.textContent;
    raceTimesSaved.push(raceObject);
});

updateTime();
setInterval(updateTime, 1000);
