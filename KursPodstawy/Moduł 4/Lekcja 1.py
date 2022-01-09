import turtle
t = turtle.Turtle('arrow')
t.shapesize(5)
t.speed('fastest')

t.up()
t.goto(-60,-40)
t.pensize(35)
t.down()
t.color('black')
t.setheading(90)
t.fd(180)
t.right(90)
t.fd(150)
t.showturtle()
t.stamp()
t.up()

t.hideturtle()
t.color('red')
t.goto(0,-120)
t.setheading(0)
t.pensize(50)
t.down()
t.circle(200)
t.circle(200,232)
t.left(90)
t.fd(400)

turtle.done()