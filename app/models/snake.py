from typing import Optional, Set, Tuple
from datetime import datetime
from dataclasses import dataclass
from app.const import Direction


@dataclass
class Snake:
    direction: Optional[Direction]
    birth_time: datetime
    coordinates: Optional[Set[Tuple]]
    length: int = 3

