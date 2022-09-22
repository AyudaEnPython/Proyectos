"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Canvas, Frame


class CustomCanvas(Canvas):

    def __init__(self):
        super().__init__()
    
    def draw_data(self):
        pass


class Menu(Frame):

    def __init__(self):
        super().__init__()


class App(Tk):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = App()
    app.mainloop()
