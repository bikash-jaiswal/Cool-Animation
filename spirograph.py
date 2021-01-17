from turtle import Turtle, Screen
import random


def random_color():
    """Return the a tuple of (R, G, B) """
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    clr = (R, G, B)
    return clr


def draw_circle(line, angle=0):
    line.setheading(angle)
    line.pencolor(random_color())
    # line.pencolor("blue")
    line.circle(100, 360)


def spirograph():
    screen = Screen()
    screen.title("Lets Draw Spirograph!")
    screen.colormode(255)
    line = Turtle()
    line.speed(0)
    for angle in range(0, 360, 5):
        draw_circle(line, angle)
    screen.exitonclick()


if __name__ == '__main__':
    spirograph()
