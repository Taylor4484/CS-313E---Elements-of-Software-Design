# File: Assignment2b.py
#
# Description: Draws my personal logo my initals (TM) - You can see
# the logo here - www.taylormccaslin.com
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



    
#Draw House
ttl = Turtle()
ts = ttl.getscreen()
ts.bgcolor("#000000")
ttl.pencolor('#ffffff')
ttl.fillcolor('#ffffff')
ttl.up()
ttl.goto(0,0)


#start T
ttl.down()
ttl.begin_fill()
ttl.setheading(145)
ttl.forward(65)
ttl.setheading(90)
ttl.forward(40)
ttl.setheading(145)
ttl.forward(65)
ttl.setheading(270)
ttl.forward(50)
ttl.setheading(145)
ttl.forward(60)
ttl.setheading(270)
ttl.forward(50)
ttl.setheading(325)
ttl.forward(60)
ttl.setheading(270)
ttl.forward(100)
ttl.setheading(300)
ttl.forward(45)
ttl.setheading(325)
ttl.forward(95)
ttl.setheading(90)
ttl.position()
ttl.forward(50)
ttl.setheading(145)
ttl.forward(65)
ttl.setheading(90)
ttl.forward(90)
ttl.setheading(325)
ttl.forward(72)
#ttl.setheading(90)
#ttl.forward(45)
ttl.goto(0,0)
ttl.end_fill()
ttl.up()

#start M
ttl.pencolor('#999999')
ttl.fillcolor('#999999')
ttl.goto(6,-180)
ttl.down()
ttl.begin_fill()
ttl.setheading(90)
ttl.forward(210)
ttl.setheading(45)
ttl.forward(150)
ttl.setheading(342)
ttl.forward(40)
ttl.setheading(270)
ttl.forward(180)
ttl.setheading(225)
ttl.forward(40)
ttl.setheading(90)
ttl.forward(170)
ttl.setheading(225)
ttl.forward(40)
ttl.setheading(270)
ttl.forward(100)
ttl.setheading(225)
ttl.forward(40)
ttl.setheading(90)
ttl.forward(110)
ttl.setheading(225)
ttl.forward(40)
ttl.setheading(270)
ttl.forward(160)
ttl.goto(6,-180)
ttl.end_fill()
ttl.hideturtle()

time.sleep(20)


