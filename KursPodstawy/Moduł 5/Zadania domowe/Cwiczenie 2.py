import turtle
t = turtle.Turtle('square')
t.color('red','red')
t.goto(0,20)
t.shapesize(3,10)
t.stamp()

t.penup()
t.goto(0,-40)
t.pendown()
t.shapesize(3,15)
t.stamp()


t = turtle.Turtle('circle')
t.color('black','black')

t.penup()
t.goto(-120,-100)
t.pendown()
t.shapesize(3)
t.stamp()

t.penup()
t.goto(120,-100)
t.pendown()
t.shapesize(3)
t.stamp()

turtle.done()

