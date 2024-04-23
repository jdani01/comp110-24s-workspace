"""EX03 - Functional Battleship."""
import random

__author__ = "730404642"

blue: str = "\U0001F7E6"
red: str = "\U0001F7E5"
white: str = "\U00002B1C"


def input_guess(grid_size: int, type1: str) -> int:
    """Takes grid size and guess type."""
    assert type1 == "row" or type1 == "column"

    if type1 == "row":
        row_guess = int(input("Guess a row: "))
        while row_guess >= (grid_size + 1) or row_guess <= 0:
            row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

        return row_guess
    else:
        column_guess = int(input("Guess a column: "))
        while column_guess >= (grid_size + 1) or column_guess <= 0:
            column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        
        return column_guess
    

def print_grid(grid_size: int, row_guess: int, column_guess: int, if_hit: bool) -> None:
    """Prints grid."""
    blue_box_line = blue * grid_size

    if if_hit is True:
        row_count = row_guess
        while row_count > 1:
            print(blue_box_line)
            row_count -= 1
        
        print(blue * (column_guess - 1) + red + blue * (grid_size - column_guess))

        row_count2 = grid_size - row_guess
        while row_count2 >= 1:
            print(blue_box_line)
            row_count2 -= 1

    else:
        row_count = row_guess
        while row_count > 1:
            print(blue_box_line)
            row_count -= 1
        
        print(blue * (column_guess - 1) + white + blue * (grid_size - column_guess))

        row_count2 = grid_size - row_guess
        while row_count2 >= 1:
            print(blue_box_line)
            row_count2 -= 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Returns whether user made a hit or miss."""
    if secret_row == row_guess and secret_column == column_guess:
        print()
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Runs the main game."""
    has_win = False
    num_turn = 1

    while has_win is False and num_turn <= 5:
        print(f"=== Turn {num_turn}/5 ===")

        my_row_guess = input_guess(grid_size, "row")
        my_col_guess = input_guess(grid_size, "column")

        has_win = correct_guess(secret_row, secret_column, my_row_guess, my_col_guess)

        if has_win is True:
            print_grid(grid_size, my_row_guess, my_col_guess, True)
            print("Hit!")
            print(f"You won in {num_turn}/5 turns!")
        else:
            print_grid(grid_size, my_row_guess, my_col_guess, False)
            print("Miss!")
        
        num_turn += 1
    
    if has_win is False:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))