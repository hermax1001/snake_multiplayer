from typing import List, Optional, Set, Tuple

from loguru import logger

from app.const import Direction
from app.models.snake import Snake
from app.models.mouse import Mouse
from random import randrange

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
        if self.snakes:
            for snake in self.snakes:
                sign = DEAD_SNAKE if snake.is_dead else SNAKE
                for coordinate in snake.coordinates:
                    x, y = coordinate
                    field[y][x] = sign
        if self.mouse:
            x, y = self.mouse.coordinates
            field[y][x] = MOUSE
        return field

    def next_step(self):
        logger.debug(f'NEXT_STEP')

        for snake in self.snakes:
            x, y = snake.coordinates[-1]
            if self.mouse.coordinates == (x, y):
                self.mouse.coordinates = (randrange(0, self.width), randrange(0, self.height))
            else:
                snake.coordinates.popleft()

            if snake.direction is Direction.LEFT:
                snake.coordinates.append((x - 1, y))
            elif snake.direction is Direction.RIGHT:
                snake.coordinates.append((x + 1, y))
            elif snake.direction is Direction.UP:
                snake.coordinates.append((x, y - 1))
            else:
                snake.coordinates.append((x, y + 1))

            x, y = snake.coordinates[-1]
            if (x < 0 or x >= self.width) or (y < 0 or y >= self.height) or self.snakes.__contains__(snake.coordinates):
                snake.is_dead = True

        game_field.delete_dead_snakes()

    def delete_dead_snakes(self):
        self.snakes = [snake for snake in self.snakes if not snake.is_dead]

    def get_snake_by_sid(self, sid):
        return self.sid_snakes_map.get(sid)

    def add_snake(self, sid, snake: Snake):
        self.sid_snakes_map[sid] = snake
        self.snakes.append(snake)

    def add_mouse(self):
        mouse = Mouse(
            coordinates=(randrange(0, self.width), randrange(0, self.height))
        )
        self.mouse = mouse


game_field = Field(width=25, height=25)
