import turtle
t = turtle.Turtle()
t.hideturtle()
t.color('blue')
t.pensize(5)


for i in range(5):
    t.fd(100)
    t.left(360/5)


turtle.done()