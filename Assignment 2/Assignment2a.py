# File: Assignment2a.py
#
# Description: Draws a house with one door, two windows and a
# chimney using Turtle Graphics.
#
# Student's Name: Micheal Taylor McCaslin
#
# Student's UT EID: MTM2275
#
# Course Name: CS 313E 
#
# Date Created: 9/22/12
#
# Date Last Modified: 9/24/12

from turtle import *
from math import *
import time

def drawSquare(turtle, width, height):
    """Draws a rectangle with the given turtle,
    with a defined width and height """
    
    turtle.down()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)


    
#Draw House
ttl = Turtle()
ttl.pencolor('black')
ttl.up()
ttl.goto(200,100)
ttl.setheading(270)
drawSquare(ttl, 400, 400)
ttl.up()
#draw door
ttl.goto(50,-100)
ttl.setheading(270)
drawSquare(ttl, 200, 100)
ttl.up()
#draw roof
ttl.goto(200,100)
ttl.setheading(135)
ttl.pendown()
ttl.forward(285)
ttl.left(90)
ttl.forward(285)
ttl.up()
#draw window1
ttl.goto(100,50)
ttl.setheading(0)
drawSquare(ttl, 75, 75)
ttl.up()
#draw window2
ttl.goto(-150,50)
ttl.setheading(0)
drawSquare(ttl, 75, 75)
ttl.up()
#draw chimney
ttl.left(90)
ttl.forward(105)
ttl.down()
ttl.forward(100)
ttl.right(90)
ttl.forward(25)
ttl.right(90)
ttl.forward(75)
ttl.hideturtle()

time.sleep(20)
