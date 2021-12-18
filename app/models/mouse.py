from typing import Optional, Tuple
from dataclasses import dataclass


@dataclass
class Mouse:
    coordinates: Optional[Tuple]
