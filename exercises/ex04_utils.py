"""EX04 - Utility Functions."""

__author__ = "730404642"


def all(list_ints: list[int], num1: int) -> bool:
    """Returns true/false if int matches every element in our list."""
    false_count = 0
    for n in list_ints:
        if num1 != n:
            false_count += 1
    
    if false_count != 0:
        return False
    elif len(list_ints) == 0:
        return False
    else:
        return True
    

def max(list_int: list[int]) -> int:
    """Returns the largest int in a list."""
    largest = list_int[0]
    for n in list_int:
        if n > largest:
            largest = n
    
    return largest


def is_equal(list_int1: list[int], list_int2: list[int]) -> bool:
    """Returns true/false if two lists are identical."""
    false_count = 0

    if len(list_int1) != len(list_int2):
        return False
    elif len(list_int1) == len(list_int2):
        for n in range(len(list_int1)):
            if list_int1[n] != list_int2[n]:
                false_count += 1
        if false_count != 0:
            return False
        else:
            return True
    

def extend(list_int1: list[int], list_int2: list[int]) -> None:
    """Combines two lists into the first list."""
    for n in range(len(list_int2)):
        list_int1.append(list_int2[n])