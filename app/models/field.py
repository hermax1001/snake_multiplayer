from typing import List, Optional, Set, Tuple

from app.models.snake import Snake
from app.models.mouse import Mouse


class Field:
    width: int
    height: int
    snakes: Optional[List[Snake]]
    mouse: Optional[Mouse]
    coordinates = Set[Tuple]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coordinates = {(x, y) for y in range(height) for x in range(width)}

    def get_map(self):
        field = [[' '] * self.width] * self.height
        if self.snakes:
            for snake in self.snakes:
                x, y = snake.coordinates
                field[y][x] = '*'
        if self.mouse:
            x, y = self.mouse.coordinates
            field[y][x] = 'o'
        return field




