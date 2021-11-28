import turtle
t = turtle.Turtle()
t.hideturtle()
t.color('blue')


for i in range(100):
    t.fd(i)
    t.left(90)


turtle.done()