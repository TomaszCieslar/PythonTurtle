import turtle
from random import randint
t = turtle.Turtle()

bok_trojkata = 50
liczba_trojkatow = 12
turtle.colormode(255)

def naszyjnik():
    t.pensize(3)
    for i in range(liczba_trojkatow):
        trojkat()
        t.fd(bok_trojkata)
        t.right(360/liczba_trojkatow)

def trojkat():
    t.down()
    for j in range(3):
        t.color(randint(0,255), randint(0,255), randint(0,255))
        t.fd(bok_trojkata)
        t.left(360/3)
    t.up()
t.goto(0,0)
naszyjnik()

turtle.done()