from turtle import Turtle, Screen
import random
line = Turtle()
line.shape("arrow")

clr = ["navy", "purple", "violet", "red", "green", "yellow", "blue", "black", "red", "green", "yellow",]


def dif_shape(side, clrname):
    line.color(clrname)
    for _ in range(side):
        line.forward(100)
        line.right(360 // side)


for sides in range(3, 11):
    line.color(random.choice(clr))
    dif_shape(sides, clr[sides])


screen = Screen()
screen.exitonclick()
