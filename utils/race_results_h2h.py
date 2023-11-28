import utils.time_processing as tp


def format_h2h_data(car1_number, car2_number, data):
    for row in data.result_rows:
        if row.car_number == car1_number:
            car1 = row
        if row.car_number == car2_number:
            car2 = row

    data = {
        'car1': {
            'driver': f"{car1.first_name} {car1.last_name}",
            'lap_times': [lap_data.lap_time_txt for lap_data in car1.laps_info],
            'laps': car1.lap_count
        },
        'car2': {
            'driver': f"{car2.first_name} {car2.last_name}",
            'lap_times': [lap_data.lap_time_txt for lap_data in car2.laps_info],
            'laps': car2.lap_count
        },
        'time_difference': [tp.time_to_txt(car2.lap_time_s - car1.lap_time_s, as_diff=True)
                            for car1, car2 in zip(car1.laps_info, car2.laps_info)],
        'faster_car': ['car1' if car1.lap_time_s < car2.lap_time_s else 'car2'
                       for car1, car2 in zip(car1.laps_info, car2.laps_info)],
        'lap_count': max(car1.lap_count, car2.lap_count)
    }

    return data
