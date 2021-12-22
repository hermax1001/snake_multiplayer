from datetime import datetime
from typing import Optional, Tuple
from dataclasses import dataclass

from app.const import MouseType


@dataclass
class Mouse:
    coordinates: Optional[Tuple]
    type: MouseType
    death_time: datetime
    is_dead: bool = False


