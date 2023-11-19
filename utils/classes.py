import utils.time_processing as tp
from utils.car_models import CAR_MODELS
import matplotlib.pyplot as plt
import numpy as np


class TrackLapTimes:
    def __init__(self, track, car, ideal_time, my_time, fuel_usage, rating):
        self.track = track
        self.car = car
        self.ideal_time_s = tp.txt_to_time(ideal_time)
        self.ideal_time_txt = ideal_time
        self.my_time_s = tp.txt_to_time(my_time)
        self.my_time_txt = my_time
        self.percentage = self.calculate_percentage()
        self.fuel_usage = fuel_usage
        self.rating = rating
        self.stars = self.calculate_stars()
        self.is_set = self.is_set()

    def calculate_percentage(self):
        if self.my_time_s != '-':
            return round(self.my_time_s / self.ideal_time_s * 100, 2)
        else:
            return '-'

    def calculate_stars(self):
        if self.rating != '-' and 0 <= int(self.rating) <= 5:
            return '★' * int(self.rating) + '☆' * (5 - int(self.rating))
        else:
            return '-'

    def is_set(self):
        return self.my_time_s != '-'


class IndRaceResultRow:
    def __init__(self, place, car_number, team_name, first_name, last_name,
                 race_time, lap_count, winner_time, winner_lap_count, car_model):
        self.place = place
        self.car_number = car_number
        self.team_name = team_name
        self.first_name = first_name
        self.last_name = last_name
        self.race_time_s = race_time / 1000
        self.race_time_txt = self.race_time_validation()
        self.lap_count = lap_count
        self.gap_to_winner_s = (race_time - winner_time) / 1000
        self.gap_to_winner_txt = self.gap_to_winner(winner_time, winner_lap_count)
        self.car = CAR_MODELS[car_model]
        self.lap_times_s = []
        self.lap_times_txt = []

    def race_time_validation(self):
        if self.race_time_s > (25 * 60 * 60):
            return 'DNF'
        else:
            return tp.time_to_txt(self.race_time_s)

    def gap_to_winner(self, winner_time, winner_lap_count):
        if self.lap_count < winner_lap_count:
            return f"+{winner_lap_count - self.lap_count} lap(s)"
        else:
            if self.race_time_s == (winner_time / 1000):
                return '-'
            else:
                gap = tp.time_to_txt(self.race_time_s - (winner_time / 1000))
                return f"+{gap}"

    def add_lap_time(self, time):
        self.lap_times_s.append(time / 1000)

    def convert_to_txt_times(self):
        self.lap_times_txt = [tp.time_to_txt(time) for time in self.lap_times_s]

    def show_lap_times_txt(self):
        text = "Lap times\n"
        for lap, time in enumerate(self.lap_times_txt, start=1):
            text += f"{lap}: {time}\n"
        return text

    # TODO Optimization
    def generate_lap_times_graph(self):
        x, y = [], []
        for lap, time in enumerate(self.lap_times_s, start=1):
            x.append(lap)
            y.append(time)

        # Set up y label
        y_bottom = round(np.min(y), 1)
        y_top = round(np.percentile(y, 90), 1)
        plt.ylim(y_bottom - 0.5, y_top)
        try:
            step = (y_top - y_bottom) / 5
            if step <= 0:
                raise ValueError
        except ValueError:
            step = 0.5
        y_range_s = np.arange(y_bottom, y_top, step=step)
        y_range_txt = [tp.time_to_txt(time) for time in y_range_s]
        plt.yticks(y_range_s, labels=y_range_txt)
        # Set up x label
        plt.xticks(np.arange(1, len(self.lap_times_s)+1, 1))
        # Set titles
        plt.xlabel("Lap Number")
        plt.ylabel("Lap Time")
        # Plot and save
        plt.grid(color='#444')
        plt.plot(x, y, c='orange')
        plt.savefig(f"static/images/race_lap_times/{self.car_number}.png", dpi=100)
        plt.clf()
        plt.close()
