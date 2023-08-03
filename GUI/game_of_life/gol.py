from random import randint


class GameOfLife:

    def __init__(self, w, h):
        self.W = w
        self.H = h
        self.grid = [[0 for _ in range(w)] for _ in range(h)]

    def get_state(self, x, y):
        if 0 <= x < self.W and 0 <= y < self.H:
            return self.grid[y][x]
        return 0

    def set_state(self, x, y, state):
        if 0 <= x < self.W and 0 <= y < self.H:
            self.grid[y][x] = state

    def count_live_neighbors(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                count += self.get_state(x + dx, y + dy)
        return count

    def should_live(self, x, y):
        live_neighbors = self.count_live_neighbors(x, y)
        if self.get_state(x, y) == 1:
            return 2 <= live_neighbors <= 3
        return live_neighbors == 3

    def next_generation(self):
        new_grid = [[0 for _ in range(self.W)] for _ in range(self.H)]
        for y in range(self.H):
            for x in range(self.W):
                new_grid[y][x] = 1 if self.should_live(x, y) else 0
        self.grid = new_grid


def create_pattern(game_of_life, x, y, pattern):
    for dy in range(len(pattern)):
        for dx in range(len(pattern[dy])):
            game_of_life.set_state(x + dx, y + dy, pattern[dy][dx])


def create_random_cells(game_of_life, num_cells):
    for _ in range(num_cells):
        x = randint(0, game_of_life.W - 1)
        y = randint(0, game_of_life.H - 1)
        game_of_life.set_state(x, y, 1)