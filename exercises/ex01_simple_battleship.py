"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730404642"

blue: str = "\U0001F7E6"
red: str = "\U0001F7E5"
white: str = "\U00002B1C"


secret = int(input("Pick a secret boat location between 1 and 4: "))

if secret < 1:
    print(f"Error! {secret} too low!")
    exit()
elif secret > 4:
    print(f"Error! {secret} too high!")
    exit()
else:
    guess = int(input("Guess a number between 1 and 4: "))

    if guess < 1:
        print(f"Error! {guess} too low!")
        exit()
    elif guess > 4:
        print(f"Error! {guess} too high!")
        exit()
    else:
        if guess == secret:
            if guess == 1:
                print(red + blue + blue + blue)
            elif guess == 2:
                print(blue + red + blue + blue) 
            elif guess == 3:
                print(blue + blue + red + blue) 
            else:
                print(blue + blue + blue + red)
            print("Correct! You hit the ship.")   
        else:
            if guess == 1:
                print(white + blue + blue + blue)
            elif guess == 2:
                print(blue + white + blue + blue)  
            elif guess == 3:
                print(blue + blue + white + blue)
            else:
                print(blue + blue + blue + white)
            print("Incorrect! You missed the ship.")