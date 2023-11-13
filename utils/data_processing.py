import re


def generate_data(file_path):
    with open(file_path, 'r') as file:
        data = []
        lines = file.readlines()
        # Set the title row
        data.append(['Track', 'Ideal Time', 'Car', 'My Time', 'Percentage', 'Rating'])
        # Format rest of the rows and count percentage
        for row in lines[1:]:
            track, ideal_time, car, my_time, rating = row.strip().split('\t')
            if my_time != '-':
                percentage = f"{txt_to_time(my_time) / txt_to_time(ideal_time) * 100:.2f}%"
            else:
                percentage = '-'
            # Change Rating to stars
            if rating != '-' and 0 <= int(rating) <= 5:
                stars = '★' * int(rating) + '☆' * (5 - int(rating))
            else:
                stars = '-'

            data.append([track, ideal_time, car, my_time, percentage, stars])

        return data


def txt_to_time(text):
    m, s = re.split(r':', text)
    time_in_s = (float(m) * 60) + float(s)
    return time_in_s
