from flask import Flask, render_template
from utils.data_processing import generate_all_data, best_tracks_graph, parse_race_results, time_to_txt
import matplotlib.pyplot as plt

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
    raw_data, data = generate_all_data(LAP_DATA_PATH)
    best_tracks_graph(raw_data)

    return render_template('lap_times.html', data=data)


@app.route('/race_results')
def race_results():
    race_result = parse_race_results()
    return render_template('race_results.html', data=race_result)


# Run the Flask app when the script is executed
if __name__ == '__main__':
    print(time_to_txt(3752.3))
    # Configure matplotlib
    matplotlib_settings()
    # Run the Flask app in debug mode
    app.run(debug=True)
