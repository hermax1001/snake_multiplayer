from typing import List, Optional, Set, Tuple

from app.models.snake import Snake
from app.models.mouse import Mouse
from random import randrange

class Field:
    width: int
    height: int
    snakes: Optional[List[Snake]] = set()
    mouse: Optional[Mouse] = None
    coordinates = Set[Tuple]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coordinates = {(x, y) for y in range(height) for x in range(width)}

    def get_map(self):
        field = [[' '] * self.width for i in range(self.height)]
        for i in range(15):
            field[randrange(0, self.width)][randrange(0, self.height)] = '*'
        field[randrange(0, self.width)][randrange(0, self.height)] = 'o'
        if self.snakes:
            for snake in self.snakes:
                x, y = snake.coordinates
                field[y][x] = '*'
        if self.mouse:
            x, y = self.mouse.coordinates
            field[y][x] = 'o'
        return field


game_field = Field(width=20, height=20)
