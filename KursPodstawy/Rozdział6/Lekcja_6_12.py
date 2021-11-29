import turtle
t= turtle.Turtle()
t.color('blue')
t.pensize(5)

for j in range (10):
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