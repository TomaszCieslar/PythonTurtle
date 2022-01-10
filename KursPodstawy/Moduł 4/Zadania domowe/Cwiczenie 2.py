import turtle
t = turtle.Turtle('arrow')
t.shapesize(5)
t.speed('fastest')


t.hideturtle()
t.up()
t.color('red','blue')
t.goto(0,-100)
t.setheading(0)
t.pensize(50)
t.down()
t.begin_fill()
t.circle(200)
t.end_fill()

t.up()
t.goto(0,100)
t.setheading(45)
t.down()
t.fd(200)
t.fd(-400)

t.up()
t.goto(0,100)
t.setheading(135)
t.down()
t.fd(200)
t.fd(-400)





turtle.done()