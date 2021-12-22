import random
from datetime import timedelta, datetime
from typing import List, Optional, Set, Tuple

from app.const import Direction, MouseType
from app.models.snake import Snake
from app.models.mouse import Mouse
from random import randrange, choice

SNAKE = 1
SNAKE_HEAD = -1
EMPTY = 0
GREEN_MOUSE = 10
RED_MOUSE = 11
BlUE_MOUSE = 12
YELLOW_MOUSE = 13
BROWN_MOUSE = 14
GREY_MOUSE = 15


class Game:
    width: int
    height: int
    snakes: Optional[List[Snake]] = []
    sid_snakes_map: dict = {}
    mice: Optional[List[Mouse]] = []
    coordinates = Set[Tuple]
    is_game_started = False

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coordinates = {(x, y) for y in range(height) for x in range(width)}

    def get_map(self):
        field = [[0] * self.width for _ in range(self.height)]
        for snake in self.snakes:
            for idx, coordinate in enumerate(snake.coordinates):
                x, y = coordinate
                field[y][x] = SNAKE if idx != len(snake.coordinates) - 1 else SNAKE_HEAD
        for mouse in self.mice:
            x, y = mouse.coordinates
            field[y][x] = mouse.type.value
        return field

    def next_step(self):
        if randrange(1, 11) == 1:
            self.add_mouse()

        mice_coordinates = {mouse.coordinates for mouse in self.mice}
        for snake in self.snakes:
            x, y = snake.coordinates[-1]
            if (x, y) not in mice_coordinates:
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
            if (x < 0 or x >= self.width) or (y < 0 or y >= self.height):
                snake.is_dead = True

        self.kill_mice()
        self.delete_dead_mice()
        self.delete_dead_snakes()

    def kill_mice(self):
        current_time = datetime.now()
        for mouse in self.mice:
            if current_time >= mouse.death_time:
                mouse.is_dead = True

    def delete_dead_snakes(self):
        self.snakes = [snake for snake in self.snakes if not snake.is_dead]

    def delete_dead_mice(self):
        self.mice = [mouse for mouse in self.mice if not mouse.is_dead]

    def get_snake_by_sid(self, sid):
        return self.sid_snakes_map.get(sid)

    def add_snake(self, sid, snake: Snake):
        self.sid_snakes_map[sid] = snake
        self.snakes.append(snake)

    def add_mouse(self):
        mouse = Mouse(
            coordinates=(randrange(0, self.width), randrange(0, self.height)),
            death_time=datetime.now() + timedelta(seconds=randrange(1, 11)),
            type=choice(list(MouseType))
        )
        self.mice.append(mouse)


game_field = Game(width=55, height=35)
