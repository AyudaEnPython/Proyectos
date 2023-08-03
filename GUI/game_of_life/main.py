from gol import GameOfLife, create_pattern, create_random_cells
from patterns import *
from tkinter import Tk, Canvas


class App(Tk):

    def __init__(self, gol, alive="black", dead="white", cell_size=10):
        super().__init__()
        self.title("Ayuda en Python - Game of Life")
        self.game_of_life = gol
        self.alive = alive
        self.dead = dead
        self.cell_size = cell_size
        self.canvas = Canvas(
            self,
            width=gol.W * cell_size,
            height=gol.H * cell_size,
            bg=dead,
        )
        self.canvas.pack()
        self.update()

    def draw_grid(self):
        self.canvas.delete('all')
        for y in range(self.game_of_life.H):
            for x in range(self.game_of_life.W):
                if self.game_of_life.get_state(x, y) == 1:
                    self.canvas.create_rectangle(
                        x * self.cell_size, y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill=self.alive,
                        outline=self.alive,
                    )

    def update(self):
        self.game_of_life.next_generation()
        self.draw_grid()
        self.after(100, self.update)


if __name__ == "__main__":
    W, H = 50, 30
    gol = GameOfLife(W, H)
    create_pattern(gol, 5, 5, GLIDER)
    create_pattern(gol, 20, 10, PULSAR)
    create_pattern(gol, 30, 20, BLINKER)
    create_pattern(gol, 10, 15, TOAD)
    create_pattern(gol, 40, 5, BEACON)
    create_pattern(gol, 2, 2, SPACESHIP)
    create_random_cells(gol, 300)
    app = App(gol, "green", "black")
    app.mainloop()
