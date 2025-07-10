from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.color("RoyalBlue")
screen = Screen()
screen.colormode(255)
tim.speed("fastest")

size_of_gap = int(input("Add size of gap:"))

for _ in range(360//size_of_gap):
    tim.circle(200)
    tim.setheading(tim.heading() + size_of_gap)
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    tim.pencolor(r,g,b)

screen.exitonclick()