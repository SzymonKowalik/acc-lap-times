import json
import re
import matplotlib.pyplot as plt
import os


def generate_raw_data(file_path):
    with open(file_path, 'r') as file:
        data = []
        lines = file.readlines()
        # Format rest of the rows and count percentage
        for row in lines[1:]:
            track, ideal_time, car, my_time, fuel_usage, rating = row.strip().split('\t')
            # Calculate percentage
            if my_time != '-':
                percentage = round(txt_to_time(my_time) / txt_to_time(ideal_time) * 100, 2)
            else:
                percentage = '-'
            # Change fuel_usage to float
            if fuel_usage != '-':
                fuel_usage = round(float(fuel_usage), 1)
            data.append([track, txt_to_time(ideal_time), car, txt_to_time(my_time),
                         percentage, fuel_usage, rating])

        return data


def generate_printable_data(raw_data):
    # Set the title row
    data = [['Track', 'Ideal Time', 'Car', 'My Time', 'Percentage', 'Fuel Usage', 'Rating']]
    for row in raw_data:
        track, ideal_time, car, my_time, percentage, fuel_usage, rating = row
        # Format data
        ideal_time = time_to_txt(ideal_time)
        my_time = time_to_txt(my_time)
        fuel_usage = f"{fuel_usage}l" if fuel_usage != '-' else '-'
        percentage = f"{percentage}%" if percentage != '-' else '-'

        # Change rating to stars
        if rating != '-' and 0 <= int(rating) <= 5:
            stars = '★' * int(rating) + '☆' * (5 - int(rating))
        else:
            stars = '-'

        data.append([track, ideal_time, car, my_time, percentage, fuel_usage, stars])
    return data


def generate_all_data(file_path):
    raw_data = generate_raw_data(file_path)
    data = generate_printable_data(raw_data)
    return raw_data, data


def txt_to_time(text):
    if text == '-':
        return text
    if text.count(':') == 1:
        m, s = re.split(r':', text)
        time_in_s = (float(m) * 60) + float(s)
    else:
        h, m, s = re.split(r':', text)
        time_in_s = (float(h) * 3600) + (float(m) * 60) + float(s)
    return time_in_s


def time_to_txt(time):
    if time == '-':
        return time
    m, s = divmod(time, 60)
    if m < 60:
        return f"{int(m)}:{s:0>4.1f}"
    else:
        h, m = divmod(m, 60)
        return f"{int(h)}:{int(m):0>2}:{s:0>4.1f}"


def best_tracks_graph(data):
    # Data format: ['Track', 'Ideal Time', 'Car', 'My Time', 'Percentage', 'Fuel Usage', 'Rating']
    # Get track name and percentage of best for each track
    filtered_data = [[row[0], round(row[4] - 100, 2)] for row in data if row[4] != '-']
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

    race_results = [['Place', 'Car Number', 'First Name', 'Last Name', 'Time', 'Lap count']]
    for place, car in enumerate(leaderboard, start=1):
        # TODO Extract car model and put into leaderboard
        time = car['timing']['totalTime']
        race_time = time_to_txt(time / 1000) if time < 90000000 else 'DNF'
        car_results = [place, car['car']['raceNumber'], car['currentDriver']['firstName'],
                       car['currentDriver']['lastName'], race_time, car['timing']['lapCount']]

        race_results.append(car_results)

    return race_results
