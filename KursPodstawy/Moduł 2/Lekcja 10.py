import turtle
t = turtle.Turtle()

t.hideturtle()
t.left(90)
t.color('gold')
t.fillcolor('red')
t.pensize(10)

t.begin_fill()

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

t.end_fill()

turtle.done()