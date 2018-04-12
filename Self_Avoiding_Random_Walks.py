import turtle as t
import random

last = 5
r = 5
cds = {}
x = 0
y = 0

def choice(num,x,y):
    if num == 1:
        t.forward(10)
        y += 10
    elif num == 2:
        t.backward(10)
        y -= 10
    elif num == 3:
        t.left(90)
        t.forward(10)
        t.right(90)
        x -= 10
    elif num == 4:
        t.right(90)
        t.forward(10)
        t.left(90)
        x += 10
    else:
        pass
    return(x,y)

t.screensize(1000,1000)
turtle = t.Turtle()
t.hideturtle()
t.mode("logo")

for i in range(1000):
    xt = x
    yt = y
    r = random.randint(1,4)
    if r == 1 or r == 2:
        if x not in cds.keys():       
            temp = choice(r,x,y)
            print(x, "not in cds keys")
        elif r == 1:
            if y + 10 not in cds[x]:
                temp = choice(r,x,y)
            else:
                pass
        elif r == 2:
            if y - 10 not in cds[x]:
                temp = choice(r,x,y)
            else:
                pass
    elif r == 3:
        if x - 10 not in cds.keys():
            temp = choice(r,x,y)
        elif y not in cds[x-10]:
            temp = choice(r,x,y)
    else:
        if x + 10 not in cds.keys():
            temp = choice(r,x,y)
        elif y not in cds[x+10]:
            temp = choice(r,x,y)
    x = temp[0]
    y = temp[1]
    if x not in cds.keys():
        cds[xt] = [yt]
    else:
        cds[xt].append(yt)
    #print(x,y)
print(cds)

