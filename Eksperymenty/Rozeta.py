import turtle
t = turtle.Turtle()

t.penup()
t.goto(0,0)
t.setheading(90)
t.hideturtle()

t.speed(10)

for i in range(30):
    for j in range(2):
        t.color('purple')
        t.pendown()
        for w in range(6):
            t.forward(32)
            t.right(16)
        t.right(84)
    t.goto(0,0)
    t.right(15)



turtle.done()