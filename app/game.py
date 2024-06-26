from collections import defaultdict
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
                field[y][x] = SNAKE
            # head_coordinates
            x, y = snake.coordinates[-1]
            field[y][x] = SNAKE_HEAD

        for mouse in self.mice:
            x, y = mouse.coordinates
            field[y][x] = mouse.type.value
        return field

    def next_step(self):
        if randrange(1, 11) == 1:
            self.add_mouse()

        mice_coordinates_map = defaultdict(list)
        for mouse in self.mice:
            mice_coordinates_map[mouse.coordinates].append(mouse)
        for snake in self.snakes:
            x, y = snake.coordinates[-1]
            if (x, y) in mice_coordinates_map:
                for mouse in mice_coordinates_map[(x, y)]:
                    mouse.is_dead = True
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

        self.kill_snakes()
        self.kill_mice()
        self.delete_dead_mice()
        self.delete_dead_snakes()

    def kill_mice(self):
        current_time = datetime.now()
        for mouse in self.mice:
            if current_time >= mouse.death_time:
                mouse.is_dead = True

    def kill_snakes(self):
        # head coordinates
        coord_snake_map = defaultdict(list)
        for snake in self.snakes:
            for coord in snake.coordinates:
                coord_snake_map[coord].append(snake)

        for snake in self.snakes:
            x, y = snake.coordinates[-1]
            if (
                (x < 0 or x >= self.width)
                or (y < 0 or y >= self.height)
            ):
                self.kill_snake(snake)
            snakes_in_head = coord_snake_map[(x, y)]
            if len(snakes_in_head) > 1:
                for s in snakes_in_head:
                    if s is not snake:
                        self.kill_snake(snake, s)

    def kill_snake(self, victim: Snake, killer: Optional[Snake] = None):
        victim.is_dead = True
        for i in range(len(victim.coordinates) - 2):
            self.add_mouse(victim.coordinates[i])
        if killer:
            killer.kills += 1

    def delete_dead_snakes(self):
        self.snakes = [snake for snake in self.snakes if not snake.is_dead]

    def delete_dead_mice(self):
        self.mice = [mouse for mouse in self.mice if not mouse.is_dead]

    def get_snake_by_sid(self, sid):
        return self.sid_snakes_map.get(sid)

    def add_snake(self, sid, snake: Snake):
        self.sid_snakes_map[sid] = snake
        self.snakes.append(snake)

    def add_mouse(self, coordinates=None):
        mouse = Mouse(
            coordinates=coordinates or (randrange(0, self.width), randrange(0, self.height)),
            death_time=datetime.now() + timedelta(seconds=randrange(1, 11)),
            type=choice(list(MouseType))
        )
        self.mice.append(mouse)


game_field = Game(width=55, height=35)
