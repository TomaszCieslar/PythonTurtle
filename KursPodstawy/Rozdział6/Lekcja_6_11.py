import turtle
t = turtle.Turtle()
t.hideturtle()
t.color('lightgreen')
t.pensize(5)

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