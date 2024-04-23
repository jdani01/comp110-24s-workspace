"""Mutating functions."""

__author__ = "730404642"


def manual_append(word: list[int], num: int) -> None:
    """Appends an int to a list int."""
    word = word.append(num)


def double(word: list[int]) -> None:
    """Doubles the int value for every element in a list."""
    word_len = len(word)
    while word_len >= 1:
        word[word_len - 1] = word[word_len - 1] * 2
        word_len -= 1

