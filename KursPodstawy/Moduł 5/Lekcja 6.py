import turtle
t = turtle.Turtle('square')
t.up()
t.speed(1)

t.color('blue')
t.shapesize(4,0.5)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()

t.goto(100,50)
t.color('gold')
t.shapesize(4,0.5)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()

t.goto(-100,50)
t.color('lightblue')
t.shapesize(4,0.5)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()

t.goto(-100,-50)
t.color('violet')
t.shapesize(4,0.5)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()

t.goto(100,-50)
t.color('green')
t.shapesize(4,0.5)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()
t.right(45)
t.stamp()

turtle.done()