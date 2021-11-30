import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.color('blue')


for i in range(4):
    t.circle(50)
    t.up()
    t.fd(70)
    t.down()


turtle.done()