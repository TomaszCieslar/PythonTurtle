import turtle
t = turtle.Turtle()

#ustawienia
t.hideturtle()
t.pensize(5)
t.color('lightgreen')
t.speed(1)

#program glowny

t.begin_fill()
for i in range(3):
    t.fd(150)
    t.left(120)
t.end_fill()

t.up()
t.goto(0,70)
t.down()

t.begin_fill()
for i in range(3):
    t.fd(150)
    t.left(120)
t.end_fill()

t.up()
t.goto(0,140)
t.down()

t.begin_fill()
for i in range(3):
    t.fd(150)
    t.left(120)
t.end_fill()


turtle.done()