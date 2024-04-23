from __future__ import annotations

"""Point Class CQ."""

__author__ = "730404642"


class Point:
    """Point class."""
    def __init__(p, x: float, y: float):
        """Initialzes point."""
        p.x = x
        p.y = y

    def scale_by(p, factor: int):
        """Mutiplies by factor."""
        p.x *= factor
        p.y *= factor
    
    def scale(p, factor: int) -> Point:
        """Creating a new point."""
        m = p.x * factor
        n = p.y * factor
        return Point(m, n)