from __future__ import annotations
import random
import time
import sys
from enum import Enum
from dataclasses import dataclass
from typing import Tuple, List, Optional

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @classmethod
    def random(cls) -> Direction:
        return random.choice(list(Direction))

class Color(Enum):
    BLACK = 0
    WHITE = 1

@dataclass
class Cell:
    color: Color
    ants: List[LangtonAnt.Ant]

class LangtonAnt:
    def __init__(self, width: int, height: int, ants_count: int = 10):
        self.board = LangtonAnt.Board(width, height)
        self.ants = [self.Ant(self.board) for _ in range(ants_count)]
        self.display_chars = {Color.BLACK: ' ', Color.WHITE: '█', 'ant': '+'}

    class Board:
        def __init__(self, width: int, height: int):
            self.width = width
            self.height = height
            self.grid = [
                [Cell(Color.BLACK, []) for _ in range(width)]
                for _ in range(height)
            ]

        def get_cell(self, position: Tuple[int, int]) -> Optional[Cell]:
            x, y = position
            if 0 <= x < self.width and 0 <= y < self.height:
                return self.grid[y][x]
            return None

        def toggle_cell_color(self, position: Tuple[int, int]) -> None:
            if cell := self.get_cell(position):
                cell.color = Color.WHITE if cell.color == Color.BLACK else Color.BLACK

        def clear_ants(self) -> None:
            for row in self.grid:
                for cell in row:
                    cell.ants.clear()

        def add_ant(self, position: Tuple[int, int], ant: LangtonAnt.Ant) -> None:
            if cell := self.get_cell(position):
                cell.ants.append(ant)

    class Ant:
        DIRECTION_DELTAS = {
            Direction.NORTH: (0, -1),
            Direction.EAST: (1, 0),
            Direction.SOUTH: (0, 1),
            Direction.WEST: (-1, 0),
        }

        def __init__(self, board: LangtonAnt.Board):
            self.board = board
            self.position = (
                random.randint(0, board.width - 1),
                random.randint(0, board.height - 1)
            )
            self.direction = Direction.random()
            self.active = True

        def move(self) -> None:
            if not self.active:
                return

            self.board.toggle_cell_color(self.position)
            current_color = self.board.get_cell(self.position).color
            self.turn_right() if current_color == Color.WHITE else self.turn_left()

            dx, dy = self.DIRECTION_DELTAS[self.direction]
            self.position = (
                (self.position[0] + dx) % self.board.width,
                (self.position[1] + dy) % self.board.height
            )

        def turn(self, steps: int) -> None:
            if not self.active:
                return
            new_value = (self.direction.value + steps) % 4
            self.direction = Direction(new_value)

        def turn_left(self) -> None:
            self.turn(-1)

        def turn_right(self) -> None:
            self.turn(1)

        def turn_around(self) -> None:
            self.turn(2)

    def run(self) -> None:
        try:
            while True:
                self._update_display()
                self._simulate_step()
                time.sleep(0.01)
        except KeyboardInterrupt:
            sys.exit()

    def _simulate_step(self) -> None:
        self.board.clear_ants()
        for ant in self.ants:
            ant.move()
            self.board.add_ant(ant.position, ant)
        self._handle_ant_collisions()

    def _handle_ant_collisions(self) -> None:
        for y in range(self.board.height):
            for x in range(self.board.width):
                cell = self.board.grid[y][x]
                if len(cell.ants) > 1:
                    for ant in cell.ants:
                        ant.turn_around()

    def _update_display(self) -> None:
        print("\033[H\033[J", end="") # Cross-platform clear screen
        for row in self.board.grid:
            line = []
            for cell in row:
                if cell.ants:
                    char = self.display_chars['ant']
                else:
                    char = self.display_chars[cell.color]
                line.append(char)
            print("".join(line))

def get_terminal_size() -> Tuple[int, int]:
    try:
        from shutil import get_terminal_size
        return get_terminal_size(fallback=(80, 24))
    except ImportError:
        return 80, 24

if __name__ == '__main__':
    cols, rows = get_terminal_size()
    game = LangtonAnt(cols - 1, rows - 2, 10)
    game.run()