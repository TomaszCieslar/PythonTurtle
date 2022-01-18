import turtle
t = turtle.Turtle('square')
t.color('black','black')
t.goto(0,20)
t.shapesize(5,15)
t.stamp()

t = turtle.Turtle('circle')
t.color('black','black')

t.penup()
t.goto(-80,-60)
t.pendown()
t.shapesize(3)
t.stamp()

t.penup()
t.goto(80,-60)
t.pendown()
t.shapesize(3)
t.stamp()

turtle.done()

