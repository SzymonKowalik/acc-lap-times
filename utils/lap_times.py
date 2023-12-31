import utils.time_processing as tp
import matplotlib.pyplot as plt
from utils.car_models import CAR_MODELS
import json


class TrackLapTimes:
    def __init__(self, track, car_id, ideal_time, my_time, fuel_usage, rating):
        self.track = track
        self.car = self.assign_car_model(car_id)
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

    @staticmethod
    def assign_car_model(car_id):
        try:
            return CAR_MODELS[int(car_id)]
        except ValueError:
            return ''


def generate_lap_time_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        lap_times = []

        for track_data in data['lapTimes']:
            track = track_data['track']
            ideal_time = track_data['idealTime']
            car_id = track_data['car']
            my_time = track_data['myTime']
            fuel_usage = track_data['fuelUsage']
            rating = track_data['rating']

            lap_time_row = TrackLapTimes(track, car_id, ideal_time, my_time, fuel_usage, rating)
            lap_times.append(lap_time_row)

        return lap_times


def best_tracks_graph(data):
    # Get track name and percentage of best for each track
    filtered_data = [[row.track, round(row.percentage - 100, 2)] for row in data if row.percentage != '-']
    # Sort lst by percentage ascending
    filtered_data.sort(key=lambda lst: lst[1])
    # Create lists for names, percentages and colors
    x, y, c = [], [], []
    color_cond = {1.5: "#F00", 2: "#F33", 2.5: "#F66", 3: "#FAA", 3.5: "#FCC", 4: "#FFF"}

    for pair in filtered_data:
        name, perc = pair
        x.append(name)
        y.append(perc)

        for k, v in color_cond.items():
            if perc < k:
                c.append(v)
                break
        else:
            c.append(color_cond[4])

    # Plot using bar plot and save
    plt.figure(figsize=(12, 7))
    plt.bar(x, y, color=c)

    plt.xticks(rotation=30)
    plt.subplots_adjust(bottom=0.15, top=1)

    plt.savefig('static/images/percentage.png', dpi=200)
    plt.clf()
