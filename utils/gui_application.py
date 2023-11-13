import customtkinter as ctk


class MainApp(ctk.CTk):
    def __init__(self, data):
        super().__init__()
        self.title = "ACC Best Lap Times"
        self.geometry("700x500")
        self.central_frame = CentralFrame(self, data)
        self.central_frame.place(x=0, y=0)


class CentralFrame(ctk.CTkScrollableFrame):
    def __init__(self, root, data):
        super().__init__(master=root, width=700, height=500)
        self.first_row = True
        self.generate_panels(data)

    def generate_panels(self, data):
        for index, values in enumerate(data):
            track, ideal_time, car, my_time, percentage, rating = values
            if self.first_row:
                box = Box(self, track, ideal_time, car, my_time, percentage, rating, ctk.CTkFont("Arial", 13, weight="bold"))
            else:
                box = Box(self, track, ideal_time, car, my_time, percentage, rating)
            box.grid(row=index, column=0)
            # After setting bold on first row, changes to normal
            self.first_row = False


class Box(ctk.CTkFrame):
    def __init__(self, root, track, ideal_time, car, my_time, percentage, rating, font=("Arial", 13)):
        super().__init__(master=root, width=100, height=20)
        self.track = ctk.CTkLabel(self, text=track, width=180, font=font)
        self.ideal_time = ctk.CTkLabel(self, text=ideal_time, width=70, font=font)
        self.car = ctk.CTkLabel(self, text=car, width=80, font=font)
        self.my_time = ctk.CTkLabel(self, text=my_time, width=70, font=font)
        self.percentage = ctk.CTkLabel(self, text=percentage, width=70, font=font)
        self.rating = ctk.CTkLabel(self, text=rating, width=70, font=font)

        self.track.grid(row=0, column=0, padx=10)
        self.ideal_time.grid(row=0, column=1, padx=10)
        self.car.grid(row=0, column=2, padx=10)
        self.my_time.grid(row=0, column=3, padx=10)
        self.percentage.grid(row=0, column=4, padx=10)
        self.rating.grid(row=0, column=5, padx=10)
