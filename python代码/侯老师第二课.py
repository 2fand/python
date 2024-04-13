import turtle
import random
colors=['red','orange','yellow','lime','cyan','blue','#cc33ff']
t=turtle.Turtle()
t.speed(0)
t.width(3)
t.shape('turtle')
t.shapesize(3)
t.color('orange')
for i in range(60):
    t.color(colors[random.randint(0,6)])
    t.circle(100)
    t.right(6)
turtle.done()