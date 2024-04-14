import turtle
t=turtle.Turtle()
color=''
t.penup()
t.goto(-1000,0)
t.pendown()
for i in range(100):
    if i%2==0:
        color='red'
    else:
        color='blue'
    t.color(color)
    t.width(i+1)
    t.forward(20)
t.penup()
t.goto(0,-50)
t.pendown()
t.width(10)
t.color('lime')
t.circle(100)
turtle.done()

