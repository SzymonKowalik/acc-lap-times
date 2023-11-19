from datetime import datetime as dt
import utils.time_processing as tp
import os


class Series:
    def __init__(self, name, description, race_time, quali_time, start_date, end_date):
        self.name = name
        self.description = description
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


class Week:
    def __init__(self, start_date, end_date, number, track):
        self.start_date = start_date
        self.end_date = end_date
        self.number = number
        self.track = track


def create_series(filepath):
    with open(filepath, 'r', encoding='UTF-8') as file:
        for i, values in enumerate(file):
            values = values.strip().split('\t')
            if i == 0:
                name, description, race_time, quali_time, start_date, end_date = values
                start_date = tp.to_date(start_date)
                end_date = tp.to_date(end_date)
                cur_series = Series(name, description, race_time, quali_time, start_date, end_date)
            else:
                start_date, end_date, track = values
                start_date = tp.to_date(start_date)
                end_date = tp.to_date(end_date)
                cur_week = Week(start_date, end_date, i, track)
                cur_series.add_week(cur_week)

    cur_series.is_active()
    cur_series.set_current_week()

    return cur_series


def get_all_series():
    series = []
    relative_path = 'data/series'
    for filename in os.listdir(relative_path):
        filepath = f"{relative_path}/{filename}"
        series.append(create_series(filepath))
    return series
