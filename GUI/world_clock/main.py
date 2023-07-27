"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from time import strftime
from datetime import datetime, timedelta
from tkinter import Tk, Label

clocks = []
TIMEZONES = (
    ("Peru", -5),
    ("Italy", 2),
    ("Japan", 9),
)


def get_time(diff):
    current_time = datetime.utcnow() + timedelta(hours=diff)
    return current_time.strftime("%H:%M:%S")


def update_times():
    for i, (_, diff) in enumerate(TIMEZONES):
        clocks[i].config(text=get_time(diff))
    root.after(1000, update_times)


def setup_gui(master):
    master.title("World Clock")
    master["bg"] = "black"
    Label(master, text=strftime("%A %d %B %Y"), bg="black", fg="yellow",
        font=("Courier", 24)).grid(row=0, columnspan=2, padx=5)
    for i, (country, _) in enumerate(TIMEZONES, 1):
        Label(master, text=country, bg="black", fg="white",
            font=("Courier", 18)).grid(row=i, column=0)
        clock = Label(
            master, text="", bg="black", fg="cyan", font=("Courier", 18))
        clock.grid(row=i, column=1)
        clocks.append(clock)


root = Tk()
setup_gui(root)
update_times()
root.mainloop()
