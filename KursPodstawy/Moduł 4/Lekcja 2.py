import turtle
t = turtle.Turtle('arrow')
t.shapesize(5)

t.color('black')
t.showturtle()
t.pensize(35)
t.setheading(90)

t.up()
t.goto(60,-40)
t.down()
t.fd(180)
t.left(90)
t.fd(150)
t.stamp()
t.up()


t.color('red')
t.goto(0,-120)
t.setheading(0)
t.pensize(50)
t.down()
t.circle(200)
t.circle(200,142)
t.left(90)
t.fd(400)
t.hideturtle()



turtle.done()