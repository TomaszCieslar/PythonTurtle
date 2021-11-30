import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.color('blue')


for i in range(1):
    t.circle(50)
    t.up()
    t.fd(200)
    t.down()
    t.circle(50)
    t.up()
    t.setheading(105)
    t.fd(200)
    t.down()
    t.circle(50)


turtle.done()