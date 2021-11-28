import turtle
t = turtle.Turtle('turtle')
t.color('blue')
t.pensize(5)


for i in range(100):
    t.fd(i)
    t.right(45)


turtle.done()