"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, Toplevel
from functools import partial

from utils import calculate, VARIANTS


class TopWindow(Toplevel):

    def __init__(self, master, variant):
        super().__init__(master=master)
        self.title(f"{variant}")
        self.geometry("180x160")
        self.setup_ui(variant)

    def setup_ui(self, v):
        a, op, b = VARIANTS[v]
        x, y, r = Entry(self), Entry(self), Label(self)
        btn = Button(self, text=f"{v[0]} = {a[0]} {op} {b[0]}", width=10)
        btn["command"] = lambda: calculate(x, op, y, r)
        Label(self, text=a).pack()
        x.pack(pady=5)
        Label(self, text=b).pack()
        y.pack(pady=5)
        btn.pack(pady=5)
        r.pack(pady=5)


class Menu(Toplevel):

    def __init__(self, master, title):
        super().__init__(master=master)
        self.title(title)
        self.geometry("140x140")
        self.setup_ui()

    def setup_ui(self):
        Label(self, text="Ley de Ohm").pack()
        for variant in VARIANTS.keys():
            btn = Button(
                self, width=16, text=f"{variant}",
                command=partial(TopWindow, self, variant),
            )
            btn.pack(pady=5)
