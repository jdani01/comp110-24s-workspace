"""Splitting a dictionary into two lists."""

__author__ = "730404642"


def get_keys(input: dict[str, int]) -> list[str]:
    """Gets the key."""
    return list(input.keys())


def get_values(input: dict[str, int]) -> list[int]:
    """Gets the value."""
    return list(input.values())