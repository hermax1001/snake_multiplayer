from dataclasses import dataclass
from typing import List, Optional

from app.models.snake import Snake
from app.models.mouse import Mouse


@dataclass
class Field:
    width: int
    height: int
    new_snakes: Optional[List[Snake]]
    snakes: Optional[List[Snake]]
    mouse: Optional[Mouse]


@dataclass
class Point:
    X: int
    Y: int
