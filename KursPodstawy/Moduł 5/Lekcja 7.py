import turtle
t = turtle.Turtle()
t.hideturtle()

t.goto(0,-100)
t.color('orange','orange')
t.begin_fill()
t.circle(200)
t.end_fill()

t=turtle.Turtle('triangle')
t.penup()
t.goto(-70,30)
t.right(90)
t.color('white')
t.shapesize(4)
t.stamp()

t.goto(-10,30)
t.stamp()
t.goto(50,30)
t.stamp()

t.goto(50,180)
t.left(180)
t.stamp()
t.goto(-50,180)
t.stamp()

t = turtle.Turtle('square')
t.color('black')
t.penup()
t.goto(0,300)
t.shapesize(3,12)


turtle.done()