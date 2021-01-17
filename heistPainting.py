import io
from extractcolor import get_rgb_color
import turtle as t
import random
from turtle import Screen
from PIL import Image

colors = get_rgb_color('spot.jpg', 30)
store_img = []


def generate_gif():
    """
    Very useful method to generate ps file to GIF
    uses PIL to generate the gif
    """
    print(f"Generating the GIF file")
    store_img[0].save("heist-dot.gif", save_all=True, append_images=store_img, duration=100, loop=0)
    print("Completed")


def draw_spot(tt):
    """
    A helper method to draw random colored dots with diameter 20
    """
    tt.dot(20, random.choice(colors))


def row(spot):
    """
    Uses draw_spot method to generate 10 dots in a row.
    And save the convert the canvas of PS format to img
    and stores to a list which later used in generating gif
    """
    ts = t.getcanvas()
    for _ in range(10):
        draw_spot(spot)
        spot.penup()
        spot.forward(50)
        spot.pendown()
        ps = ts.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        store_img.append(img)


def run_painting():
    """
    Main method where turtle plays role
    """
    spot = t.Turtle()
    spot.penup()
    spot.setposition(-200, -200)
    spot.pendown()
    spot.hideturtle()
    for x in range(10):
        row(spot)
        spot.penup()
        spot.goto(-200+x, spot.ycor()+50)
        spot.pendown()


if __name__ == '__main__':
    screen = Screen()
    screen.colormode(255)
    run_painting()
    generate_gif()
    screen.exitonclick()
