"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Canvas, Frame, Label, Scale, Tk, ttk

from algos import bubble_sort, insertion_sort
from utils import color, generate_data, normalize


T = {
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
}


class CustomCanvas(Canvas):

    def __init__(self, master):
        super().__init__(master)
        self["bg"] = "grey7"
        self.h = 250
        self.w = 600

    def show(self, data, colors):
        self.delete("all")
        width = self.w / (2*len(data) - 1)
        offset = 25
        spacing = 10
        for i, height in enumerate(normalize(data)):
            x0 = i*width + offset + spacing
            y0 = self.h - (height*220)
            x1 = ((i+1)*width) + offset
            y1 = self.h
            self.create_rectangle(x0, y0, x1, y1, fill=colors[i])
            self.create_text(
                x0+16, y0, anchor="se", text=str(data[i]), fill="white",
            )
        self.master.update_idletasks()


class Menu(Frame):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        Label(
            self, text="Sorting Algorithm",
        ).grid(row=0, column=0)
        self.algo = ttk.Combobox(self, values=["Bubble", "Insertion"])
        self.speed = Scale(
            self, from_=0.1, to=1.0, length=100, digits=2,
            resolution=0.1, orient="horizontal", label="Speed",
        )
        self.min_value = Scale(
            self, from_=1, to=20, orient="horizontal", label="Minimun Value",
            resolution=1,
        )
        self.max_value = Scale(
            self, from_=1, to=20, orient="horizontal", label="Maximun Value",
            resolution=1,
        )
        self.size = Scale(
            self, from_=8, to=20, resolution=1, orient="horizontal",
            label="Size",
        )
        self.max_value.set(20)
        self.size.set(12)
        self.algo.current(0)
        self.algo.grid(row=1, column=0)
        self.size.grid(row=0, column=2)
        self.min_value.grid(row=0, column=1)
        self.max_value.grid(row=1, column=1)
        self.speed.grid(row=1, column=2)
        self.btn_generate = Button(self, text="Generate")
        self.btn_start = Button(self, text="Start")
        self.btn_generate.grid(row=0, column=3, sticky="we")
        self.btn_start.grid(row=1, column=3, sticky="we")


class App(Tk):

    def __init__(self):
        super().__init__()
        self.menu = Menu()
        self.canvas = CustomCanvas(self)
        self.menu.pack()
        self.canvas.pack()
        self.menu.btn_generate["command"] = self.setup_data
        self.menu.btn_start["command"] = self.start_algo

    def setup_data(self):
        self.data = generate_data(
            min=self.menu.min_value.get(),
            max=self.menu.max_value.get(),
            size=self.menu.size.get(),
        )
        self.canvas.show(self.data, color(self.data, "red"))

    def start_algo(self):
        speed = self.menu.speed.get()
        T[self.menu.algo.get()](self.data, self.canvas.show, speed)


if __name__ == "__main__":
    app = App()
    app.mainloop()
