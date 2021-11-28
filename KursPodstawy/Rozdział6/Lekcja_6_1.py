import turtle
t = turtle.Turtle('square')
t.color('blue')
t.shapesize(6,1)

for i in range(3):
    t.stamp()
    t.right(45)


turtle.done()