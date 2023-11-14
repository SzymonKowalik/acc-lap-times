from flask import Flask, render_template
from utils.data_processing import generate_data

app = Flask(__name__)
LAP_DATA_PATH = 'data/lap_data.txt'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fuel_calculator')
def fuel_calculator():
    return render_template('fuel_calculator.html')


@app.route('/lap_times')
def lap_times():
    data = generate_data(LAP_DATA_PATH)
    return render_template('lap_times.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
