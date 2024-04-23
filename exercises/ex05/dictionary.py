"""EX05 - Dictionary."""
 
__author__ = "730404642"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    inverse: dict[str, str] = {}
    for key in d:
        y = d[key]
        inverse[y] = key
    return inverse


def favorite_color(d: dict[str, str]) -> str:
    """Returns the highest color count."""
    color_count: dict[str, int] = {}

    for color in d.values():
        if color not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1

    max_count = max(color_count.values())
    most_popular_colors = []

    for color, count in color_count.items():
        if count == max_count:
            most_popular_colors.append(color)
    
    for color in d.values():
        if color in most_popular_colors:
            return color
        

def count(list_1: list[str]) -> dict[str, int]:
    """Counts the amount of times an element shows up in a list."""
    result: dict[str, int] = {}
    for elem in list_1:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    """Groups elements in a list based off its first letter."""
    letter: dict[str, list[str]] = {}
    
    for elem in list_1:
        first = elem.lower()[0]
        
        if first not in letter:
            letter[first] = [elem]
        else:
            letter[first].append(elem)
    return letter


def update_attendance(d: dict[str, list[str]], day: str, student: str) -> None:
    """Adds students to an attendance sheet."""
    if day in d:
        if student not in d[day]:
            d[day].append(student)
    else:
        d[day] = [student]
    return None