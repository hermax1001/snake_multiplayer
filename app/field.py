from datetime import datetime
from typing import List, Optional, Set, Tuple
from collections import deque

from app.const import Direction
from app.models.snake import Snake
from app.models.mouse import Mouse

SNAKE = 1
DEAD_SNAKE = -1
MOUSE = 2
EMPTY = 0


class Field:
    width: int
    height: int
    snakes: Optional[List[Snake]] = []
    sid_snakes_map: dict = {}
    mouse: Optional[Mouse] = None
    coordinates = Set[Tuple]
    is_game_started = False

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coordinates = {(x, y) for y in range(height) for x in range(width)}

    def get_map(self):
        field = [[0] * self.width for _ in range(self.height)]
        # for i in range(15):
        #     field[randrange(0, self.width)][randrange(0, self.height)] = '*'
        # field[randrange(0, self.width)][randrange(0, self.height)] = 'o'
        if self.snakes:
            for snake in self.snakes:
                for coordinate in snake.coordinates:
                    x, y = coordinate
                    field[y][x] = SNAKE
        if self.mouse:
            x, y = self.mouse.coordinates
            field[y][x] = MOUSE
        return field

    def next_step(self):
        pass

    def get_snake_by_sid(self, sid):
        return self.sid_snakes_map[sid]

    def add_snake(self, sid):
        snake = Snake(
            direction=Direction.UP,
            birth_time=datetime.now(),
            coordinates=deque([(0, self.height - 1), (0, self.height - 2), (0, self.height - 3)])
        )
        self.sid_snakes_map[sid] = snake
        self.snakes.append(snake)


game_field = Field(width=20, height=20)
