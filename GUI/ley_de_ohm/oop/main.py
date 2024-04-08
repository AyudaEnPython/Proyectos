"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Tk
from widgets import Menu


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("140x140")
        self.setup_ui()

    def setup_ui(self):
        btn = Button(self, text="Electricidad")
        btn["command"] = lambda: Menu(self, "Electricidad")
        btn.pack(pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
