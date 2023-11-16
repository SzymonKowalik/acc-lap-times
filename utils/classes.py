import utils.time_processing as tp


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


class IndRaceResultRow:
    def __init__(self, place, car_number, first_name, last_name,
                 race_time, lap_count, winner_time, winner_lap_count):
        self.place = place
        self.car_number = car_number
        self.first_name = first_name
        self.last_name = last_name
        self.race_time_s = race_time / 1000
        self.race_time_txt = self.race_time_validation()
        self.lap_count = lap_count
        self.gap_to_winner_s = (race_time - winner_time) / 1000
        self.gap_to_winner_txt = self.gap_to_winner(winner_time, winner_lap_count)

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
