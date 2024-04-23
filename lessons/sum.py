"""Summing the elements of a list using different loops."""

__author__ = "730404642"


def w_sum(vals: list[float]) -> float:
    """Sum using while."""
    sum = 0.0
    x = 0
    while x < len(vals):
        sum += vals[x]
        x += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sum using for/in."""
    sum = 0.0
    for x in vals:
        sum += x
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sum using for and range."""
    sum = 0.0
    for x in range(len(vals)):
        sum += vals[x]
    return sum