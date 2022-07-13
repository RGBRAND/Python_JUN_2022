from turtle import *

t = Turtle()
t.speed('fast')
bgcolor('black')
t.color('yellow')
pensize(2)
for i in range(1,500,3):
    t.fd(i)
    t.lt(60)
    mainloop()