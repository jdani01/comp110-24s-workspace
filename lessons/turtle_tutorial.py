from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

leo.penup()
leo.goto(-100, -100)
leo.pendown()

leo.color(99, 204, 250)

leo.fillcolor(32, 67, 93)
leo.begin_fill()
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1
leo.end_fill()

done()

