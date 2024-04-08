"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Tk

from widgets import menu


def setup_ui(master):
    btn = Button(master, text="Electricidad")
    btn["command"] = lambda: menu(master)
    btn.pack(pady=5)


if __name__ == "__main__":
    root = Tk()
    root.title("Calculadora")
    root.geometry("140x140")
    setup_ui(root)
    root.mainloop()
