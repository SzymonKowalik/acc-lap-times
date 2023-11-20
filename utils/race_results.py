from utils.car_models import CAR_MODELS
import utils.time_processing as tp
import matplotlib.pyplot as plt
import numpy as np
import json
import os


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


def parse_race_results():
    file_path = os.path.expanduser('~/Documents/Assetto Corsa Competizione/Results/race.json')
    with open(file_path, 'r', encoding='utf-16-le') as file:
        file_contents = json.load(file)

    leaderboard = file_contents['snapShot']['leaderBoardLines']
    all_lap_data = file_contents['laps']

    # winner data
    winner_time = leaderboard[0]['timing']['totalTime']
    winner_lap_count = leaderboard[0]['timing']['lapCount']

    race_results = []
    for place, row in enumerate(leaderboard, start=1):
        car_id = row['car']['carId']
        car_number = row['car']['raceNumber']
        team_name = row['car']['teamName']
        first_name = row['currentDriver']['firstName']
        last_name = row['currentDriver']['lastName']
        race_time = row['timing']['totalTime']
        lap_count = row['timing']['lapCount']
        car_model = row['car']['carModel']
        results_row = IndRaceResultRow(place, car_number, team_name, first_name, last_name,
                                       race_time, lap_count, winner_time, winner_lap_count, car_model)

        # Add lap times
        for lap_data in all_lap_data:
            lap_car_id = lap_data['carId']
            lap_time = lap_data['lapTime']

            if car_id == lap_car_id:
                results_row.add_lap_time(lap_time)

        results_row.convert_to_txt_times()
        results_row.generate_lap_times_graph()
        race_results.append(results_row)

    return race_results
