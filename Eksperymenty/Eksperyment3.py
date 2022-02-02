import turtle

t = turtle.Turtle()
step = 20

def colorGreen():
    t.color('green')

def colorBlack():
    t.color('black')

def up():
    t.setheading(90)
    t.forward(step)

def down():
    t.setheading(270)
    t.forward(step)

def right():
    t.setheading(0)
    t.forward(step)

def left():
    t.setheading(180)
    t.forward(step)

turtle.listen()

turtle.onkey(colorGreen, "g")
turtle.onkey(colorBlack, "b")

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")

turtle.mainloop()