import turtle
t = turtle.Turtle()
t.hideturtle()

#pierwszy
t.left(120)
t.color('violet')
t.fillcolor('orange')
t.pensize(10)
t.begin_fill()
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.end_fill()

#drugi
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

#trzeci
t.setheading(0)
t.goto(200,0)
t.color('red')
t.fillcolor('blue')
t.pensize(10)
t.begin_fill()
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.end_fill()




turtle.done()