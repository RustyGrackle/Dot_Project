
#import colorgram
#rgb_colors = []
#
#colors = colorgram.extract('dot2.jpeg', 20)
#for color in colors:
#    r = color.rgb.r

#    g = color.rgb.g

#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)
color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]


import turtle
from turtle import Turtle, Screen
from random import random, choice
me = Turtle()
me.speed("fastest")
next = 0
turtle.colormode(255)

def change_row():
    global next
    me.penup()
    me.goto(-250, next - 250)
    me.pendown()
    next += 50


def create_row():

    me.color(choice(color_list))
    me.dot(20)
    me.penup()
    me.forward(50)
    me.pendown()


for i in range(10):
    change_row()
    for _ in range(10):
        create_row()

screen = Screen()
screen.exitonclick()
