import turtle
t = turtle.Turtle()

t.left(90)
t.color('gold')
t.pensize(10)

t.goto(-200,0)
t.forward(200)

t.color('blue')
t.left(90)
t.forward(200)

t.penup()
t.goto(200,0)
t.pendown()

t.color('violet')
t.left(90)
t.forward(200)
t.color('yellow')

t.left(90)
t.forward(200)

turtle.done()