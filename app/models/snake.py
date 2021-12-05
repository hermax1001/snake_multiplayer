from typing import Optional, Set, Tuple
from datetime import datetime
from dataclasses import dataclass
from app.const import Direction


@dataclass
class Snake:
    direction: Optional[Direction]
    birth_time: datetime
    length: int = 3
    coordinates = Optional[Set[Tuple]]
