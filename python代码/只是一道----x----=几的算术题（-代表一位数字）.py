import turtle
import random
import time
t=turtle.Turtle()
def pX():
    t.goto(0,0)
    t.pendown()
    t.color('red')
    t.left(45)
    t.forward(150)
    t.backward(300)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.backward(300)
    t.forward(150)
a=random.randint(1,9999)
b=random.randint(1,9999)
c=a*b
t.penup()
t.backward(165)
t.write(f"{a}×{b}=?", font=("宋体",
                            30, "normal"))
t.width(10)
time.sleep(0.5)
d=input('')
if d is None:
	d=''
good=False
t.goto(-165,-60)
t.write(f"?={d}", font=("宋体",30, "normal"))
if len(d)!=0:
    if str(c)==d:
        good=True
        t.goto(-150,0)
        t.pendown()
        t.color('lime')
        t.goto(-50,-155.6)
        t.goto(150,150)
    else:
        pX()
else:
    t.color('#FFF143')
    t.goto(-150.618,-170)
    t.write('?',font=("Arial",360,"normal"))
if not good:
    t.color('black')
    t.setheading(0)
    t.penup()
    t.goto(-165,-160)
    t.write(f"正确答案={c}", font=("宋体",
                                    30, "normal"))
t.hideturtle()
turtle.done()