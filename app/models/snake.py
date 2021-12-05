from typing import Optional, Set
from datetime import datetime
from dataclasses import dataclass
from app.const import Direction
from app.models.field import Point


@dataclass
class Snake:
    direction: Optional[Direction]
    birth_time: datetime
    length: int = 3
    coordinates = Optional[Set[Point]]
