import turtle
t = turtle.Turtle('circle')
t.color('yellow','yellow')

t.penup()
t.goto(0,0)
t.pendown()
t.shapesize(20)
t.stamp()

t.color('blue','blue')
t.penup()
t.goto(-60,50)
t.pendown()
t.shapesize(3)
t.stamp()

t.penup()
t.goto(60,50)
t.pendown()
t.shapesize(3)
t.stamp()

t.hideturtle()
t.penup()
t.goto(-120,-20)
t.pendown()
t.pensize(30)
t.pencolor('black')
t.setheading(-45)
t.fd(100)
t.left(45)
t.fd(100)
t.left(45)
t.fd(100)


turtle.done()

