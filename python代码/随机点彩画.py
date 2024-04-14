import turtle
import random
import time
color=''
width=x=y=0
t=turtle.Turtle()
#不重要的东西（适配）
t.penup()
t.forward(102.5)
t.pendown()
t.left(90)
t.forward(102.5)
for i in range(3):
    t.left(90)
    t.forward(205)
t.left(90)
t.forward(102.5)
#-----------------
t.penup
for i in range(random.randint(100,1000)):
    t.penup()
    width=random.randint(1,100)
    x=random.uniform(-102.50,102.50)
    y=random.uniform(-102.50,102.50)
    color='#'+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])+random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
    t.pensize(width)
    t.color(color)
    t.goto(x,y)
    t.pendown()
    t.goto(x-0.01,y)
turtle.done()