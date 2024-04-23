"""EX02 - One Shot Battleship."""
 
__author__ = "730404642"

blue: str = "\U0001F7E6"
red: str = "\U0001F7E5"
white: str = "\U00002B1C"

grid_size = 4
secret_row = 3
secret_column = 2

row_guess = int(input("Guess a row: "))
while row_guess >= (grid_size + 1) or row_guess <= 0:
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess = int(input("Guess a column: "))
while column_guess >= (grid_size + 1) or column_guess <= 0:
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

blue_box_line = blue * grid_size

if secret_row == row_guess and secret_column == column_guess:
    row_count = secret_row
    while row_count > 1:
        print(blue_box_line)
        row_count -= 1
    
    print(blue * (secret_column - 1) + red + blue * (grid_size - secret_column))

    row_count2 = grid_size - secret_row
    while row_count2 >= 1:
        print(blue_box_line)
        row_count2 -= 1

    print("Hit!")


if secret_row != row_guess or secret_column != column_guess:
    row_count = row_guess
    while row_count > 1:
        print(blue_box_line)
        row_count -= 1
    
    print(blue * (column_guess - 1) + white + blue * (grid_size - column_guess))

    row_count2 = grid_size - row_guess
    while row_count2 >= 1:
        print(blue_box_line)
        row_count2 -= 1

    if secret_row == row_guess and secret_column != column_guess:
        print("Close! Correct row, wrong column.")
    elif secret_row != row_guess and secret_column == column_guess:
        print("Close! Correct column, wrong row.")
    else:
        print("Miss!")