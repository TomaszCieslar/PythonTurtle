import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.color('red')
t.speed(1)

t.begin_fill()

for i in range(5):
    t.forward(150)
    t.right(144)

t.end_fill()

turtle.done()