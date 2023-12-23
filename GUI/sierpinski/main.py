from math import sqrt
from tkinter import Button, Canvas, Label, Frame, Tk, Scale


def midpoint(x, y):
    return ((x[0] + y[0])/2, (x[1] + y[1])/2)


def _helper(canvas, level, x, y, z):
    if level == 1:
        canvas.create_polygon(x, y, z)
    else:
        a = midpoint(x, y)
        b = midpoint(y, z)
        c = midpoint(x, z)
        _helper(canvas, level-1, x, a, c)
        _helper(canvas, level-1, a, y, b)
        _helper(canvas, level-1, c, b, z)


class App(Tk):

    def __init__(self, color, size):
        super().__init__()
        self.color = color
        self.size = size
        self.setup_ui()

    def setup_ui(self):
        self.frame = Frame(self)
        self.frame.pack()
        self.canvas = Canvas(
            self.frame, width=self.size, height=self.size, bg=self.color
        )
        self.canvas.pack(side="top")
        self.btn_draw = Button(self.frame, text="Draw", command=self._draw)
        self.btn_draw.pack(side="left", padx=5, pady=5)
        Label(self.frame, text="Level").pack(side="left", padx=5, pady=5)
        self.level = Scale(self.frame, from_=1, to=9, orient="horizontal")
        self.level.pack(side="left", padx=5, pady=5)

    def _draw(self):
        level = int(self.level.get())
        self.canvas.create_rectangle(
            0, 0, self.size + 5, self.size + 5, fill=self.color
        )
        h = int(round(self.size * sqrt(3.0)/2.0))
        x = (2, h + 3)
        y = (2 + self.size/2, 3)
        z = (2 + self.size, h + 3)
        _helper(self.canvas, level, x, y, z)


if __name__ == "__main__":
    app = App("peru", 512)
    app.mainloop()
