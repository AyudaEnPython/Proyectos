"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, Toplevel
from functools import partial

from utils import calculate, VARIANTS


def top_window(master, v):
    top = Toplevel(master)
    top.title(f"{v}")
    top.geometry("180x160")
    a, op, b = VARIANTS[v]
    x, y, r = Entry(top), Entry(top), Label(top)
    btn = Button(top, text=f"{v[0]} = {a[0]} {op} {b[0]}", width=10)
    btn["command"] = lambda: calculate(x, op, y, r)
    Label(top, text=a).pack()
    x.pack(pady=5)
    Label(top, text=b).pack()
    y.pack(pady=5)
    btn.pack(pady=5)
    r.pack(pady=5)


def menu(master):
    this = Toplevel(master)
    this.title("Electricidad")
    this.geometry("140x140")
    Label(this, text="Ley de Ohm").pack()
    for variant in VARIANTS.keys():
        btn = Button(
            this, width=10, text=f"{variant}",
            command=partial(top_window, this, variant),
        )
        btn.pack(pady=5)
