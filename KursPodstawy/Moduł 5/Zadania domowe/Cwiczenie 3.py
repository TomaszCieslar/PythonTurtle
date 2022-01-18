import turtle
t = turtle.Turtle()
t.pensize(10)
t.penup()
t.goto(0,-100)
t.pendown()
t.color('blue','blue')
t.begin_fill()
t.circle(200,360,12)
t.end_fill()

t = turtle.Turtle('square')
t.penup()
t.goto(0,-10)
t.pendown()
t.color('white')
t.shapesize(20,1)
t.stamp()

t = turtle.Turtle('triangle')
t.penup()
t.left(90)
t.goto(0,180)
t.pendown()
t.color('white')
t.shapesize(5)
t.stamp()




turtle.done()
