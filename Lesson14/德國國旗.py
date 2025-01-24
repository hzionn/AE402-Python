# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:24:36 2018

@author: Eric
"""

import turtle
tur = turtle.Turtle()

def rectangle():
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)

turtle.setup(850,850)

tur.penup()
tur.goto(-400,400)
tur.pendown()
#設定著色顏色
tur.fillcolor(0,0,0)
tur.begin_fill()
rectangle()
tur.end_fill()

tur.penup()
tur.goto(-400,200)
tur.pendown()
#設定著色顏色
tur.fillcolor(1,0,0)
tur.begin_fill()
rectangle()
tur.end_fill()

tur.penup()
tur.goto(-400,0)
tur.pendown()
#設定著色顏色
tur.fillcolor(1,1,0)
tur.begin_fill()
rectangle()
tur.end_fill()

turtle.done()
turtle.exitonclick()

