import turtle
t = turtle.Turtle()
t.hideturtle()
t.color('blue')
t.fillcolor('red')
t.pensize(5)
t.left(15)

t.begin_fill()
for i in range(5):
    t.fd(100)
    t.right(360/5)
t.end_fill()

turtle.done()