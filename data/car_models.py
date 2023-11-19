class Car:
    def __init__(self, car_id, manufacturer, model, year, group):
        self.car_id = car_id
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.group = group


cars = [
    [12, 'Aston Martin', 'V12 Vantage GT3', '2013', 'GT3'],
    [20, 'Aston Martin', 'V8 Vantage GT3', '2019', 'GT3'],
    [3, 'Audi', 'R8 LMS', '2015', 'GT3'],
    [19, 'Audi', 'R8 LMS Evo', '2019', 'GT3'],
    [31, 'Audi', 'R8 LMS Evo II', '2022', 'GT3'],
    [11, 'Bentley', 'Continental GT3', '2015', 'GT3'],
    [8, 'Bentley', 'Continental GT3', '2018', 'GT3'],
    [30, 'BMW', 'M4 GT3', '2022', 'GT3'],
    [7, 'BMW', 'M6 GT3', '2017', 'GT3'],
    [14, 'Emil Frey Jaguar', 'G3', '2012', 'GT3'],
    [32, 'Ferrari', '296 GT3', '2023', 'GT3'],
    [2, 'Ferrari', '488 GT3', '2018', 'GT3'],
    [24, 'Ferrari', '488 GT3 Evo', '2020', 'GT3'],
    [17, 'Honda', 'NSX GT3', '2017', 'GT3'],
    [21, 'Honda', 'NSX GT3 Evo', '2019', 'GT3'],
    [4, 'Lamborghini', 'Huracan GT3', '2015', 'GT3'],
    [16, 'Lamborghini', 'Huracan GT3 Evo', '2019', 'GT3'],
    [33, 'Lamborghini', 'Huracan GT3 Evo2', '2023', 'GT3'],
    [15, 'Lexus', 'RC F GT3', '2016', 'GT3'],
    [5, 'McLaren', '650S GT3', '2015', 'GT3'],
    [22, 'McLaren', '720S GT3', '2019', 'GT3'],
    [35, 'McLaren', '720S GT3 Evo', '2023', 'GT3'],
    [1, 'Mercedes-AMG', 'GT3', '2015', 'GT3'],
    [25, 'Mercedes-AMG', 'GT3 2020', '2020', 'GT3'],
    [10, 'Nissan', 'GT-R Nismo GT3', '2015', 'GT3'],
    [6, 'Nissan', 'GT-R Nismo GT3', '2018', 'GT3'],
    [0, 'Porsche', '991 GT3 R', '2018', 'GT3'],
    [23, 'Porsche', '991 II GT3 R', '2019', 'GT3'],
    [34, 'Porsche', '992 GT3 R', '2023', 'GT3'],
    [13, 'Reiter Engineering', 'R-EX GT3', '2017', 'GT3'],
    [50, 'Alpine', 'A110 GT4', '2018', 'GT4'],
    [51, 'Aston Martin', 'Vantage GT4', '2018', 'GT4'],
    [52, 'Audi', 'R8 LMS GT4', '2018', 'GT4'],
    [53, 'BMW', 'M4 GT4', '2018', 'GT4'],
    [55, 'Chevrolet', 'Camaro GT4.R', '2017', 'GT4'],
    [56, 'Ginetta', 'G55 GT4', '2012', 'GT4'],
    [57, 'KTM', 'X-Bow GT4', '2016', 'GT4'],
    [58, 'Maserati', 'GranTurismo MC GT4', '2016', 'GT4'],
    [59, 'McLaren', '570S GT4', '2016', 'GT4'],
    [60, 'Mercedes-AMG', 'GT4', '2016', 'GT4'],
    [61, 'Porsche', '718 Cayman GT4 Clubsport', '2019', 'GT4'],
    [26, 'Ferrari', '488 Challenge Evo', '2020', 'GTC'],
    [18, 'Lamborghini', 'Huracan Super Trofeo', '2015', 'GTC'],
    [29, 'Lamborghini', 'Huracan Super Trofeo EVO2', '2021', 'GTC'],
    [9, 'Porsche', '991 II GT3 Cup', '2017', 'GTC'],
    [28, 'Porsche', '992 GT3 Cup', '2021', 'GTC'],
    [27, 'BMW', 'M2 CS Racing', '2020', 'TCX']
]

CAR_MODELS = {car_id: Car(car_id, manufacturer, model, year, group)
              for car_id, manufacturer, model, year, group in cars}
