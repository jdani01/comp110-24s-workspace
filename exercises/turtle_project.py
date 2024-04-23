"""Portrayal/Animation of the 2024 Eclipse. BEST VIEWED IN FULL SCREEN."""
 
__author__ = "730404642"
 
from turtle import Turtle, colormode, done 
import random
colormode(255)
 
 
def main() -> None:
    """The entrypoint of the scene."""
    ertle: Turtle = Turtle()
    ertle.speed(100)

    draw_background_blue(ertle, -1000, -500, 2000)
    draw_sun(ertle, -200, -200, 350)
    draw_moonphase1(ertle, -200, -200, 20)
    draw_background_black(ertle, -1000, -500, 2000)
    draw_stars(ertle, 30)
    draw_totality(ertle, -200, -200, 350)
    done()


def draw_stars(a_turtle: Turtle, stars: int) -> None:
    """Draws a changable amount of stars in the sky."""
    j: int = 0
    a_turtle.color(255, 255, 255)
    while j < stars:
        x = random.randint(-900, 900)
        y = random.randint(-450, 500)
        width = random.randint(5, 20)

        a_turtle.penup()
        a_turtle.goto(x, y) 
        a_turtle.setheading(0.0)
        a_turtle.pendown()
        a_turtle.fillcolor(255, 255, 255)
        a_turtle.begin_fill()
        i: int = 0

        while i < 4:
            a_turtle.forward(width)
            a_turtle.right(90)
            i = i + 1
        j = j + 1
        a_turtle.end_fill()


def draw_background_blue(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws the inital blue background."""
    a_turtle.color(0, 0, 0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.fillcolor(63, 40, 108)
    a_turtle.begin_fill()
    i: int = 0
    while (i < 4):
        a_turtle.forward(width)
        a_turtle.left(90)
        i = i + 1
    a_turtle.end_fill()


def draw_background_black(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws the background after the moon moves over the sun."""
    a_turtle.color(0, 0, 0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.fillcolor(0, 0, 0)
    a_turtle.begin_fill()
    i: int = 0
    while (i < 4):
        a_turtle.forward(width)
        a_turtle.left(90)
        i = i + 1
    a_turtle.end_fill()


def draw_sun(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws the inital sun shape."""
    a_turtle.color(255, 150, 0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.fillcolor(255, 213, 0)
    a_turtle.begin_fill()
    i: int = 0
    while (i < 4):
        a_turtle.forward(width)
        a_turtle.left(90)
        i = i + 1
    a_turtle.end_fill()


def draw_moonphase1(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Provides and animation of how the moon moved across the sun."""
    j: int = 0
    w = width
    while j < 34:
        a_turtle.color(0, 0, 0)
        a_turtle.penup()
        a_turtle.goto(x, y)
        a_turtle.pendown()

        a_turtle.fillcolor(37, 37, 37)
        a_turtle.begin_fill()
        i: int = 0
        while i < 4:
            a_turtle.forward(w)
            a_turtle.left(90)
            i = i + 1
        a_turtle.end_fill()
        w += 10
        j += 1


def draw_totality(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Shows the image of the moon fully over the sun."""
    j: int = 0
    white = 255
    w = width + 100
    while j < 3:
        a_turtle.color(white, white, white)
        a_turtle.penup()
        a_turtle.goto(x - 50, y - 50)
        a_turtle.pendown()

        a_turtle.fillcolor(white, white, white)
        a_turtle.begin_fill()
        i: int = 0
        while i < 4:
            a_turtle.forward(w)
            a_turtle.left(90)
            i = i + 1
        a_turtle.end_fill()
        w -= 30
        j += 1
        x += 15
        y += 15
        white -= 45

    x = -200
    y = -200
    a_turtle.color(0, 0, 0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.fillcolor(37, 37, 37)
    a_turtle.begin_fill()
    k: int = 0
    while (k < 4):
        a_turtle.forward(width)
        a_turtle.left(90)
        k = k + 1
    a_turtle.end_fill()

        
if __name__ == "__main__":
    main()