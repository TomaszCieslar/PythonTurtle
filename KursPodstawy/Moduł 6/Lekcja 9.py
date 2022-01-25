import turtle
t = turtle.Turtle()

#ustawienia
t.hideturtle()
t.color('blue')
t.speed(10)

#glowny program
for i in range(100):
    t.fd(i)
    t.left(90)



turtle.done()