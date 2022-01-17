import turtle
t = turtle.Turtle()

t.speed(10)
t.pensize(4)
t.color('oliveDrab', 'oliveDrab1')
t.setposition(-50,0)

t.begin_fill()
t.fd(175)
t.left(120)
t.fd(175)
t.left(120)
t.fd(175)
t.left(120)
t.end_fill()

t.fd(25)
t.right(90)
t.fillcolor('peachpuff')

t.begin_fill()
t.fd(125)
t.left(90)
t.fd(125)
t.left(90)
t.fd(125)
t.left(90)
t.fd(125)
t.left(90)
t.end_fill()

t.penup()
t.fd(62.5)
t.left(90)
t.fd(25)
t.right(90)
t.pendown()

t.color('black','black')
t.begin_fill()
t.circle(15)
t.end_fill()

t.hideturtle()

turtle.done()