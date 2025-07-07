# import colorgram
from turtle import Turtle, Screen
import random

def draw_circle(space, circle_d):
    tim.begin_fill()
    tim.circle(circle_d)
    tim.end_fill()
    tim.penup()
    tim.forward(space + circle_d)
    tim.pendown()

def draw_row(horizontal, colors, space, circle_dmtr):
    for i in range(horizontal):
        tim.color(random.choice(colors))
        draw_circle(space, circle_dmtr)

def move_back(horizontal, space, circle_d):
    tim.penup()
    tim.left(90)
    tim.forward(space + circle_d)
    tim.left(90)
    tim.forward(horizontal*(space + circle_d))
    tim.left(180)
    tim.pendown()


# data preparations
color_list = [(46, 92, 144), (243, 250, 245), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88),
              (211, 162, 101), (37, 144, 46), (68, 34, 47), (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47),
              (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16), (18, 96, 49), (233, 237, 244),
              (211, 56, 76), (155, 23, 19), (187, 143, 156), (60, 167, 91), (46, 149, 196), (226, 177, 167),
              (163, 209, 182), (227, 171, 180), (17, 75, 108), (116, 123, 146), (184, 188, 208), (73, 79, 43),
              (162, 199, 214)]
# setup
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
screen = Screen()
screen.colormode(255)
screen.setup(width=960, height=900)


circle_diameter = 20
spacing = 50
rows = 10
columns = 10

# Grid size calculation
grid_width = columns * (spacing + circle_diameter) - spacing
grid_height = rows * (spacing + circle_diameter) - spacing

# Move turtle to top-left starting point (centered grid)
start_x = -grid_width / 2
start_y = -grid_height / 2

tim.penup()
tim.goto(start_x, start_y)
tim.pendown()

for _ in range(rows):
    draw_row(columns, color_list, spacing, circle_diameter)
    move_back(columns, spacing, circle_diameter)



screen.exitonclick()