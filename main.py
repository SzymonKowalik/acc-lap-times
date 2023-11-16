from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from utils.data_processing import best_tracks_graph, parse_race_results, generate_lap_time_data

app = Flask(__name__)
LAP_DATA_PATH = 'data/lap_data.txt'


def matplotlib_settings():
    # Set compatibility with Flask
    plt.switch_backend('agg')
    # plt.style.use('dark_background')
    plt.rcParams['axes.facecolor'] = '#222'
    plt.rcParams['figure.facecolor'] = '#222'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    plt.rcParams['axes.edgecolor'] = 'white'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fuel_calculator')
def fuel_calculator():
    return render_template('fuel_calculator.html')


@app.route('/lap_times', methods=["GET"])
def lap_times():
    # TODO Save state of Hide empty
    data = generate_lap_time_data(LAP_DATA_PATH)
    best_tracks_graph(data)

    sort_by = request.args.get('sort_by', default='track')
    sort_direction = int(request.args.get('sort_direction', default=0))

    valid_rows = []
    remaining_rows = []

    for row in data:
        if getattr(row, sort_by) != '-':
            valid_rows.append(row)
        else:
            remaining_rows.append(row)

    valid_rows.sort(key=lambda x: getattr(x, sort_by), reverse=sort_direction)
    valid_rows.extend(remaining_rows)

    data = valid_rows

    return render_template('lap_times.html', data=data)


@app.route('/race_results')
def race_results():
    race_result = parse_race_results()
    return render_template('race_results.html', data=race_result)


# Run the Flask app when the script is executed
if __name__ == '__main__':
    # Configure matplotlib
    matplotlib_settings()
    # Run the Flask app in debug mode
    app.run(debug=True)
