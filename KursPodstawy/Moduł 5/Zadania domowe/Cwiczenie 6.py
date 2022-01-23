import turtle
t = turtle.Turtle('triangle')
t.color('black', 'green')
t.penup()
t.left(90)
t.goto(0,180)
t.pendown()
t.shapesize(5)
t.stamp()

t.penup()
t.goto(0,82)
t.pendown()
t.shapesize(6)
t.stamp()

t.penup()
t.goto(0,-35)
t.pendown()
t.shapesize(7)
t.stamp()

t = turtle.Turtle('square')
t.color('black', 'brown')

t.penup()
t.goto(0,-115)
t.pendown()
t.shapesize(4,2)
t.stamp()






turtle.done()
