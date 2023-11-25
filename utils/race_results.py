from utils.car_models import CAR_MODELS
import utils.time_processing as tp
import matplotlib.pyplot as plt
import numpy as np
import json
import os


class RaceInfo:
    def __init__(self, fastest_lap, winner_time, winner_laps):
        self.fastest_lap = fastest_lap
        self.winner_time = winner_time
        self.winner_laps = winner_laps
        self.result_rows = []

    def add_result(self, row):
        self.result_rows.append(row)


class IndRaceResultRow:
    def __init__(self, race_info, place, car_number, team_name, first_name, last_name,
                 race_time, lap_count, personal_fastest, car_model):
        self.race_info = race_info

        self.place = place
        self.car_number = car_number
        self.team_name = team_name
        self.first_name = first_name
        self.last_name = last_name

        self.race_time_s = race_time
        self.race_time_txt = self.race_time_validation()
        self.lap_count = lap_count
        self.personal_fastest = personal_fastest

        self.gap_to_winner_s = race_time - self.race_info.winner_time
        self.gap_to_winner_txt = self.gap_to_winner()

        self.car = CAR_MODELS[car_model]
        self.laps_info = []

    def race_time_validation(self):
        if self.race_time_s > (25 * 60 * 60):
            return 'DNF'
        else:
            return tp.time_to_txt(self.race_time_s)

    def gap_to_winner(self):
        winner_laps = self.race_info.winner_laps
        winner_time = self.race_info.winner_time

        if self.lap_count < self.race_info.winner_laps:
            return f"+{winner_laps - self.lap_count} lap(s)"
        else:
            if self.race_time_s == winner_time:
                return '-'
            else:
                gap = tp.time_to_txt(self.race_time_s - winner_time)
                return f"+{gap}"

    def add_lap_time(self, lap_info):
        self.laps_info.append(lap_info)

    def generate_lap_times_graph(self):
        x, y = [], []
        for lap, lap_info in enumerate(self.laps_info, start=1):
            x.append(lap)
            y.append(lap_info.lap_time_s)

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
        plt.xticks(np.arange(1, len(self.laps_info)+1, 1))
        # Set titles
        plt.xlabel("Lap Number")
        plt.ylabel("Lap Time")
        # Plot and save
        plt.grid(color='#444')
        plt.plot(x, y, c='orange')
        plt.savefig(f"static/images/race_lap_times/{self.car_number}.png", dpi=100)
        plt.clf()
        plt.close()


class LapInfo:
    def __init__(self, lap_time, is_race_fastest, is_personal_best, is_invalidated):
        self.lap_time_txt = tp.time_to_txt(lap_time)
        self.lap_time_s = lap_time
        self.is_race_fastest = is_race_fastest
        self.is_personal_best = is_personal_best
        self.is_invalidated = is_invalidated


def parse_race_results():
    file_path = os.path.expanduser('~/Documents/Assetto Corsa Competizione/Results/race.json')
    with open(file_path, 'r', encoding='utf-16-le') as file:
        file_contents = json.load(file)

    leaderboard = file_contents['snapShot']['leaderBoardLines']
    all_lap_data = file_contents['laps']

    # race_data
    fastest_lap = file_contents['snapShot']['bestlap'] / 1000
    winner_time = leaderboard[0]['timing']['totalTime'] / 1000
    winner_lap_count = leaderboard[0]['timing']['lapCount']

    race_results = RaceInfo(fastest_lap, winner_time, winner_lap_count)

    for place, row in enumerate(leaderboard, start=1):
        car_id = row['car']['carId']
        car_number = row['car']['raceNumber']
        team_name = row['car']['teamName']
        first_name = row['currentDriver']['firstName']
        last_name = row['currentDriver']['lastName']
        race_time = row['timing']['totalTime'] / 1000
        lap_count = row['timing']['lapCount']
        personal_fastest = row['timing']['bestLap'] / 1000
        car_model = row['car']['carModel']

        results_row = IndRaceResultRow(race_results, place, car_number, team_name, first_name,
                                       last_name, race_time, lap_count, personal_fastest, car_model)

        # Add lap times
        for lap_data in all_lap_data:
            # Get lap time
            lap_time = lap_data['lapTime']
            lap_time_s = lap_time / 1000

            # Do not add if DNF during the lap
            if lap_time_s > (60 * 60):
                continue

            # Get additional data
            flags = lap_data['flags']
            lap_car_id = lap_data['carId']

            if car_id == lap_car_id:
                is_race_fastest = 1 if fastest_lap == lap_time_s else 0
                is_personal_best = 1 if personal_fastest == lap_time_s else 0
                is_invalidated = 1 if flags in [1, 1025] else 0

                lap_info = LapInfo(lap_time_s, is_race_fastest, is_personal_best, is_invalidated)
                results_row.add_lap_time(lap_info)

        # Currently not used in new results design
        # results_row.generate_lap_times_graph()
        race_results.add_result(results_row)

    return race_results
