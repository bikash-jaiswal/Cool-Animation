from turtle import Turtle, Screen

small_turtle = Turtle()

small_turtle.shape("arrow")
small_turtle.color("black")
x = 2
y = 3
for _ in range(10):

    small_turtle.forward(x)
    small_turtle.penup()
    small_turtle.forward(y)
    small_turtle.pendown()
    x = x+5


screen = Screen()
screen.exitonclick()
