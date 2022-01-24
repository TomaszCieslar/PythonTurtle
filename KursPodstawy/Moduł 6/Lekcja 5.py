import turtle
t = turtle.Turtle()

t.speed(1)
t.hideturtle()
t.pensize(5)
t.color('red')

for i in range(10):
    t.circle(50)
    t.left(36)

turtle.done()