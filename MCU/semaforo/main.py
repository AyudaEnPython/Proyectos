"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import serial
from tkinter import Tk, Canvas

W = H = 60
SIZE = (5, 5, 55, 55)


class Light(Canvas):

    def __init__(self, master, color, command, mcu=None):
        super().__init__(master)
        self.config(bg="grey20", highlightthickness=0)
        self.config(width=W, height=H)
        self.create_oval(*SIZE, width=2, fill=color)
        self._command = command
        self.mcu = mcu
        self.bind("<ButtonPress-1>", self._press)

    def _press(self, _):
        if self.mcu is not None:
            self.mcu.write(bytes(str(self._command), "utf-8"))
        else:
            print(self._command)


class App(Tk):

    def __init__(self, mcu):
        super().__init__()
        self.mcu = mcu
        self.setup_ui()
        self.config(bg="grey20")

    def setup_ui(self):
        for color in  ("red", "yellow", "green"):
            Light(self, color, ord(color[0]), self.mcu).pack()


def main():
    try:
        arduino = serial.Serial(port="COM3", baudrate=9600)
    except Exception as e:
        arduino = None
    app = App(arduino)
    app.mainloop()


if __name__ == "__main__":
    main()
