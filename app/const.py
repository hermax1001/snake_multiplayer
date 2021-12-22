import random
from enum import Enum


class Direction(str, Enum):
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    UP = 'UP'
    DOWN = 'DOWN'


class MouseType(Enum):
    GREEN_MOUSE = 10
    RED_MOUSE = 11
    BlUE_MOUSE = 12
    YELLOW_MOUSE = 13
    BROWN_MOUSE = 14
    GREY_MOUSE = 15
