from typing import Optional
from dataclasses import dataclass
from app.models.field import Point


@dataclass
class Mouse:
    coordinates = Optional[Point]
