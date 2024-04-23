"""Functions that implement sorting algorithms."""
import numpy as np
import timeit
import tracemalloc
import random

__author__ = "730404642"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    for i in range(1, len(x)):
        mover = x[i]
        index = i
        while index > 0 and mover < x[index - 1]:
            x[index] = x[index - 1]
            index -= 1
        x[index] = mover
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    for i in range(len(x) - 1):
        index_of_min = i
        for j in range(i + 1, len(x)):
            if x[j] < x[index_of_min]:
                index_of_min = j

        x[i], x[index_of_min] = x[index_of_min], x[i]
    return None