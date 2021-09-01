from turtle import *
from random import random, choice

colors = ['red', 'green', 'brown', 'pink', 'purple']
# set up
my_turtle = Turtle()
my_win = my_turtle.getscreen()
my_turtle.color('pink')
my_turtle.left(90)
my_turtle.up()
my_turtle.backward(300)
my_turtle.down()


def tree(branch_length, turtle):
    if branch_length > 5:
        color = choice(colors)
        turtle.color(color)
        turtle.forward(branch_length)
        turtle.right(20)
        tree(branch_length - 15, turtle)
        color = choice(colors)
        turtle.color(color)
        turtle.left(40)
        tree(branch_length - 15, turtle)
        turtle.right(20)
        turtle.backward(branch_length)


tree(110, my_turtle)
my_win.exitonclick()
