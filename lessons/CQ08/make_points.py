"""Testing points.py."""

__author__ = "730404642"

from lessons.CQ08.point import Point


def check_points():
    """Checks points."""
    point_example = Point(3, 4)
    point_example.scale_by(2) 
    point_scaled = point_example.scale(2) 