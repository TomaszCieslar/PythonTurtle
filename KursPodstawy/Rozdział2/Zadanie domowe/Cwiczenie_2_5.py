import turtle
t = turtle.Turtle()

# t.hideturtle()
t.pensize(0)
t.setheading(45)

t.color('red')
t.fillcolor('red')

t.begin_fill()
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.forward(-100)
t.end_fill()

t.color('yellow')
t.fillcolor('yellow')
t.begin_fill()
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.setheading(315)

t.color('green')
t.fillcolor('green')

t.begin_fill()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()
turtle.done()