import turtle
t = turtle.Turtle()
t.color('gold')
t.hideturtle()
t.pensize(10)
t.setheading(45)

t.fillcolor('blue')

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

t.fillcolor('green')
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
turtle.done()