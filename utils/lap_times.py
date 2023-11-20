import utils.time_processing as tp
import matplotlib.pyplot as plt


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


def generate_lap_time_data(file_path):
    with open(file_path, 'r') as file:
        data = []
        lines = file.readlines()
        # Format rest of the rows and count percentage
        for row in lines[1:]:
            track, ideal_time, car, my_time, fuel_usage, rating = row.strip().split('\t')

            lap_time_row = TrackLapTimes(track, car, ideal_time, my_time, fuel_usage, rating)
            data.append(lap_time_row)

        return data


def best_tracks_graph(data):
    # Get track name and percentage of best for each track
    filtered_data = [[row.track, round(row.percentage - 100, 2)] for row in data if row.percentage != '-']
    # Sort data by percentage ascending
    filtered_data.sort(key=lambda x: x[1])
    # Create lists for names, percentages and colors
    x, y, c = [], [], []
    color_cond = {2: "#0F3", 3: "#2E3", 4: "#FD3", 5: "#F93", 6: "#F03"}

    for pair in filtered_data:
        name, perc = pair
        x.append(name)
        y.append(perc)

        for k, v in color_cond.items():
            if perc < k:
                c.append(v)
                break
        else:
            c.append(color_cond[6])

    # Plot using bar plot and save
    plt.figure(figsize=(12, 7))
    plt.bar(x, y, color=c)

    plt.savefig('static/images/percentage.png', dpi=200)
    plt.clf()
