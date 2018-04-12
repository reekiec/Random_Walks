import turtle as t
import random

last = 5
r = 5

def choice(num):
    if num == 1:
        t.forward(10)
    elif num == 2:
        t.backward(10)
    elif num == 3:
        t.left(90)
        t.forward(10)
    else:
        t.right(90)
        t.forward(10)

t.screensize(1000,1000)
turtle = t.Turtle()
t.hideturtle()

for i in range(1000):
    r = random.randint(1,4)
    choice(r)
    #print(i)

