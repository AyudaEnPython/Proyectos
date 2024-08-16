"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from time import localtime, strftime
from tkinter import Label, Tk
# pip install prototools
from prototools import tw

BG, FG_OFF, FG_ON = tw.STONE_900, tw.STONE_800, tw.GREEN_400
FONT = "Helvetica 18"
THRESHOLD_PAST, THRESHOLD_TO = 3, 33
DISPLAY = (
    "ITRISUHALFTEN",
    "QUARTERTWENTY",
    "FIVEQMINUTEST",
    "PASTMTOSAMOPM",
    "ONENTWOZTHREE",
    "FOURFIVESEVEN",
    "SIXEIGHTYNINE",
    "TENELEVENPHIL",
    "TWELVELOCLOCK",
)
IT_IS = [(0, 0), (0, 1), (0, 3), (0, 4)]
AM, PM = ((3, 8), (3, 9)), ((3, 11), (3, 12))
PAST, TO = ((3, 0), (3, 1), (3, 2), (3, 3)), ((3, 5), (3, 6))
HALF = [(0, i) for i in range(6, 10)]
A_QUARTER = [(0, 7)] + [(1, i) for i in range(7)]
OCLOCK = [(8, i) for i in range(8, 13)]
MINUTES = [(2, i) for i in range(5, 12)]
FIVE = [(2, i) for i in range(0, 4)]
TEN = [(0, i) for i in range(10, 13)]
TWENTY = [(1, i) for i in range(7, 13)]
NS = (
    (4, range(3)), (4, range(4, 7)), (4, range(8, 13)),
    (5, range(4)), (5, range(4, 8)), (6, range(3)),
    (5, range(8, 13)), (6, range(3, 8)), (6, range(9, 13)),
    (7, range(3)), (7, range(3, 9)), (8, range(6)), (4, range(3))
)
MM = (
    FIVE + MINUTES, TEN + MINUTES, A_QUARTER,
    TWENTY + MINUTES, TWENTY + FIVE + MINUTES, HALF,
)


class App(Tk):

    def __init__(self):
        super().__init__() 
        self.title("AyudaEnPython")
        self.config(bg=BG)
        self.letters = {}
        self.setup_ui()
        self._update()

    def setup_ui(self):
        for i, row in enumerate(DISPLAY):
            for j, char in enumerate(row):
                label = Label(self, text=char, font=FONT, fg=FG_OFF, bg=BG)
                label.grid(row=i, column=j)
                self.letters[f"{i}{j}"] = label

    def _update(self):
        current = localtime()
        hh, mm = int(strftime("%I", current)), int(strftime("%M", current))
        am_or_pm = strftime("%p", current)
        self._reset_display()
        for (i, j) in self.translate(hh, mm, am_or_pm):
            self.letters[f"{i}{j}"].config(fg=FG_ON)
        self.after(1000, self._update)

    def _reset_display(self):
        for k in self.letters:
            self.letters[k].config(fg=FG_OFF)

    def _map(self, value, from_min, from_max, to_min, to_max, k=0.4):
        ratio = (value - from_min) / (from_max - from_min)
        return round(to_min + (ratio * (to_max - to_min)) - k)

    def to_past_or_to(self, mm):
        if THRESHOLD_PAST <= mm < THRESHOLD_TO:
            return PAST
        elif THRESHOLD_TO <= mm <= 57:
            return TO
        return []

    def to_mm(self, mm):
        if mm > 30:
            mm = 60 - mm
        return MM[self._map(mm, 3, 28, 0, 5)] if mm >= THRESHOLD_PAST else []

    def to_hh(self, hh, mm):
        start, range_ = NS[hh] if mm > THRESHOLD_TO else NS[hh - 1]
        return [(start, i) for i in range_]

    def translate(self, hh, mm, am_or_pm):
        letters = IT_IS
        letters += self.to_mm(mm)
        letters += self.to_past_or_to(mm)
        letters += self.to_hh(hh, mm)
        letters += AM if am_or_pm == "AM" else PM
        if 0 <= mm < THRESHOLD_PAST or 57 < mm <= 60:
            letters += OCLOCK
        return letters


if __name__ == "__main__":
    app = App()
    app.mainloop()
