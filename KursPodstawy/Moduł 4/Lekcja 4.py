import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(10)

#pien
t.color('brown','brown')
t.setheading(0)
t.up()
t.goto(100,-200)
t.down()
t.begin_fill()
t.fd(50)
t.left(90)
t.fd(100)
t.left(90)
t.fd(50)
t.left(90)
t.fd(100)
t.left(90)
t.end_fill()


t.color('green','green')
t.setheading(0)


#korona1
t.up()
t.goto(50,-100)
t.setheading(0)
t.down()
t.begin_fill()
t.fd(150)
t.left(120)
t.fd(150)
t.left(120)
t.fd(150)


#korona2
t.up()
t.goto(50,-50)
t.setheading(0)
t.down()
t.begin_fill()
t.fd(150)
t.left(120)
t.fd(150)
t.left(120)
t.fd(150)

#korona3
t.up()
t.goto(50,0)
t.setheading(0)
t.down()
t.begin_fill()
t.fd(150)
t.left(120)
t.fd(150)
t.left(120)
t.fd(150)




t.end_fill()

turtle.done()