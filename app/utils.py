from app.const import Direction


def is_opposite_direction(current: Direction, new: Direction) -> bool:
    """Return True if the direction is opposite"""
    return {current, new} in ({Direction.UP, Direction.DOWN}, {Direction.RIGHT, Direction.LEFT})
