from typing import Optional, Tuple, Deque, Any
from datetime import datetime
from dataclasses import dataclass
from app.const import Direction


@dataclass
class Snake:
    direction: Optional[Direction]
    birth_time: datetime
    coordinates: Optional[Deque[Tuple]]
    sid: Any
    is_dead: bool = False

