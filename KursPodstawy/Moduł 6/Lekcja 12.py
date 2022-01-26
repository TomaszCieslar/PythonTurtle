from os import rename
import turtle
t = turtle.Turtle()

#ustawienia
t.hideturtle()
t.speed(10)
t.color('blue')
t.pensize(5)

#program glowny
t.up()
t.goto(-100,0)
t.down()

for j in range(10):
    for i in range(20):
        t.down()
        t.fd(10)
        t.up()
        t.fd(10)
        t.down()
    t.up()
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(400)
    t.left(180)
    




turtle.done()