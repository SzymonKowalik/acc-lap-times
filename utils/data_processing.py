import json
import matplotlib.pyplot as plt
import os
from utils.classes import IndRaceResultRow, TrackLapTimes


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
