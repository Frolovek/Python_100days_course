from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.color("RoyalBlue")
tim.width(15)
screen = Screen()
screen.colormode(255)
directions = [0, 90, 180, 360]


for _ in range (100):
    tim.setheading(random.choice(directions))
    tim.forward(100)
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    tim.pencolor(r,g,b)



screen.exitonclick()