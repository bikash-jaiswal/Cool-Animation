import turtle as t
from turtle import Screen
import random

# clr = ["burlywood", "spring green", "medium violet red", "chartreuse", "dim gray", "gold"]
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    temp = (r, g, b)
    return temp

def walk():
    line = t.Turtle()
    t.colormode(255)

    line.pensize(10)
    line.speed(0)
    for _ in range(200):
        line.pendown()
        line.pencolor(random_color())
        line.forward(30)
        line.setheading(random.choice(direction))
        line.penup()


if __name__ == '__main__':

    screen = Screen()
    screen.title("Welcome to the Random walk!")
    walk()
    screen.exitonclick()
