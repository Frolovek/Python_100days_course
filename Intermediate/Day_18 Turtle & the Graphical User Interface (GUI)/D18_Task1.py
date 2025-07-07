from turtle import Turtle, Screen
import random

def drawing_shape(angles):
    for _ in range(angles):
        tim.forward(100)
        tim.right(360 / angles)


tim = Turtle()
tim.shape("turtle")
tim.color("RoyalBlue")
screen = Screen()
screen.colormode(255)


for i in range(3,11):
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    tim.pencolor(r,g,b)
    drawing_shape(i)


screen.exitonclick()