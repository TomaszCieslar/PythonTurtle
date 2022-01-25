import turtle
t = turtle.Turtle()

#ustawienia
t.hideturtle()
t.speed(1)
t.pensize(5)
t.color('blue')

#czesc glowna programu

for i in range(1):
    t.circle(50)
    t.up()
    t.fd(200)
    t.down()
    t.circle(50)
    t.up()
    t.setheading(105)
    t.fd(200)
    t.down()
    t.circle(50)

turtle.done()