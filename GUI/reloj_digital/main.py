"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from time import strftime
from tkinter import Tk, ttk


class DigitalClock(Tk):

    def __init__(self) -> None:
        super().__init__()
        self._config()
        self.setup_ui()
        self._update()

    def setup_ui(self) -> None:
        self.display = ttk.Label(
            self,
            font=("Arial", 40),
            background="black",
            foreground="green",
        )
        self.display.pack(expand=True)

    def _update(self) -> None:
        self.display.configure(text=strftime("%H:%M:%S"))
        self.after(1000, self._update)

    def _config(self) -> None:
        self.title("Ayuda en Python")
        self.geometry("250x80")
        self.resizable(0, 0)
        self["bg"] = "black"


if __name__ == "__main__":
    reloj = DigitalClock()
    reloj.mainloop()
