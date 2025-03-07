import random, time, typing
import sys, os, platform

class GameOfLife:
    def __init__(self, width, height, rate):
        self.WIDTH = width
        self.HEIGHT = height
        self.ALIVE_CH = '█'
        self.DEAD_CH = ' '
        self.cells = [[random.random() < rate for _ in range(self.WIDTH)]
                      for _ in range(self.HEIGHT)]

    def run(self):
        while True:
            self._print()
            self._update_grid()
            try:
                time.sleep(0.5)
            except KeyboardInterrupt:
                sys.exit()

    def _print(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        for y in range(self.HEIGHT):
            row = "".join(
                self.ALIVE_CH if self.cells[y][x] else self.DEAD_CH
                for x in range(self.WIDTH)
            )
            print(row)

    def _update_grid(self):
        next_cell = [[False for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                next_cell[y][x] = self._get_next_cell_state(x, y)
        self.cells = next_cell

    def _get_next_cell_state(self, x: int, y: int) -> bool:
        num_neighbors = self._count_live_neighbors(x, y)
        is_alive = self.cells[y][x]
        if is_alive:
            return num_neighbors in (2, 3)
        else:
            return num_neighbors == 3

    def _count_live_neighbors(self, x: int, y: int) -> int:
        num_neighbors = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor_x = (x + dx) % self.WIDTH
                neighbor_y = (y + dy) % self.HEIGHT
                if self.cells[neighbor_y][neighbor_x]:
                    num_neighbors += 1
        return num_neighbors

if __name__ == '__main__':
    game = GameOfLife(79, 20, 0.1)
    game.run()