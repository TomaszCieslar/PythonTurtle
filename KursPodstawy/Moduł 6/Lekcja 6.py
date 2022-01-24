import turtle
t = turtle.Turtle()

t.speed(1)
t.hideturtle()
t.pensize(5)
t.color('gold')

t.begin_fill()

for i in range(4):
    t.circle(50)
    t.left(90)

t.end_fill()

turtle.done()