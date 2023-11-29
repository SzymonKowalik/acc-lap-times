from datetime import datetime as dt
import utils.time_processing as tp
from datetime import timedelta, date
import json


class Series:
    def __init__(self, name, description, website, race_time, quali_time, start_date, end_date):
        self.name = name
        self.description = description
        self.website = website
        self.race_time = race_time
        self.quali_time = quali_time
        self.start_date = start_date
        self.end_date = end_date
        self.weeks = []
        self.active = None
        self.current_week = None

    def add_week(self, week):
        self.weeks.append(week)

    def is_active(self):
        current_date = dt.now().date()
        self.active = self.start_date <= current_date <= self.end_date

    def set_current_week(self):
        if not self.active:
            return None

        current_date = dt.now().date()
        for week in self.weeks:
            if week.start_date <= current_date <= week.end_date:
                self.current_week = week

    def mid_season_brake_remaining(self):
        for week in self.weeks:
            if week.start_date > dt.now().date():
                remaining = week.end_date - week.start_date
                # return remaining.strftime("%d")
                return f"{remaining.days} Days Left"


class Week:
    def __init__(self, start_date, end_date, number, track):
        self.start_date = start_date
        self.end_date = end_date
        self.number = number
        self.track = track

        self.start_times = []
        self.upcoming_race = None
        self.upcoming_race_in = None

    def generate_daily_start_times(self, first_race, interval, repeats):
        self.start_times = []
        race_time = dt.strptime(first_race, '%H:%M')
        index = 1
        while (index <= repeats or repeats == -1) and race_time < dt.strptime('23:59', '%H:%M'):
            self.start_times.append(race_time.time())
            race_time += timedelta(hours=interval)
            index += 1

        if self.start_times:
            self.set_upcoming_race()

    def set_upcoming_race(self):
        current_datetime = dt.now()
        if self.start_date <= current_datetime.date() <= self.end_date:
            if len(self.start_times) == 1:
                self.upcoming_race = self.start_times[0]
            else:
                for race_time in self.start_times:
                    if current_datetime.time() < race_time:
                        self.upcoming_race = race_time
                        break
                else:
                    self.upcoming_race = self.start_times[0]
            self.set_countdown_start(current_datetime)

    def set_countdown_start(self, current_datetime):
        tomorrow_date = current_datetime.date() + timedelta(days=1)
        current_time = current_datetime.time()
        is_next_day = False

        time_diff = dt.combine(date.min, self.upcoming_race) - dt.combine(date.min, current_time)
        # Check if next race is tomorrow, then add 1 day
        if time_diff <= timedelta(0):
            is_next_day = True
            next_day = dt(1, 1, 2, 0, 0, 0, 0)
            time_diff = dt.combine(next_day, self.upcoming_race) - dt.combine(date.min, current_time)

        if is_next_day and tomorrow_date > self.end_date:
            self.upcoming_race_in = 'Next week'
        else:
            self.upcoming_race_in = str(time_diff).split('.', maxsplit=1)[0]


def create_series(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)

    all_series = []

    for series in data['series']:
        name = series['name']
        description = series['description']
        website = series['website']
        race_length = series['raceLength']
        quali_length = series['qualiLength']
        start_date = tp.to_date(series['startDate'])
        end_date = tp.to_date(series['endDate'])
        cur_series = Series(name, description, website, race_length, quali_length, start_date, end_date)

        for week in series['weeks']:
            start_date = tp.to_date(week['startDate'])
            end_date = tp.to_date(week['endDate'])
            number = week['weekNumber']
            track = week['track']
            cur_week = Week(start_date, end_date, number, track)
            cur_week.generate_daily_start_times(week['firstRace'], week['raceInterval'], week['raceCount'])
            cur_series.add_week(cur_week)

        cur_series.is_active()
        cur_series.set_current_week()
        all_series.append(cur_series)

    return all_series
