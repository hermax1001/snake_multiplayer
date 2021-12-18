from typing import Optional, Tuple, Deque
from datetime import datetime
from dataclasses import dataclass
from app.const import Direction


@dataclass
class Snake:
    direction: Optional[Direction]
    birth_time: datetime
    coordinates: Optional[Deque[Tuple]]
    length: int = 3

