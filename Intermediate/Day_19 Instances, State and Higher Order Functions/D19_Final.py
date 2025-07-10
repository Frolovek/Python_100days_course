from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle is win the bet, enter the colour:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-240, y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print("You've lost!")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
















screen.exitonclick()


