import turtle
t = turtle.Turtle()

#parametry programu
t.hideturtle()
t.pensize(5)
t.color('blue')
t.speed(1)


#glowna petla
for i in range(4):
    t.circle(50)
    t.up()
    t.fd(70)
    t.down()


turtle.done()