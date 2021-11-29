import turtle
t= turtle.Turtle()

t.pensize(5)

t.color('blue')
for i in range(20):
    t.down()
    t.fd(10)
    t.up()
    t.fd(10)
    t.down()

t.up()
t.goto(0,-40)
t.down()

t.color('red')
for i in range(20):
    t.down()
    t.fd(10)
    t.up()
    t.fd(10)
    t.down()

turtle.done()