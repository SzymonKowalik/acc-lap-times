from utils.gui_application import MainApp
from utils.data_processing import generate_data


def main():
    data = generate_data('data/lap_data.txt')
    app = MainApp(data)
    app.mainloop()


if __name__ == '__main__':
    main()
