import turtle
t = turtle.Turtle()

#ustawienia
t.color('blue')
t.pensize(5)
t.hideturtle()
t.speed(10)

#program glowny
for i in range(100):
    t.fd(i)
    t.right(45)



turtle.done()