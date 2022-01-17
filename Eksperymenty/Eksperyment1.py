import turtle
gravity = -0.005 #pixels / (time of iteration) ^ 2
x_velocity = 1 #pixels / (time of iteration)
y_velocity = 0.25 #pixels / (time of iteration)
energy_loss = 0.95

width = 600
height = 800

ball = turtle.Turtle()


window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

ball.penup()
ball.color('green')
ball.shape('circle')

while True:  
    ball.sety(ball.ycor() + y_velocity)
    ball.setx(ball.xcor() + x_velocity)
    y_velocity += gravity
    if ball.ycor() < -height / 2:
        y_velocity = -y_velocity * energy_loss
        ball.sety(-height / 2)
        
    if ball.xcor() > width / 2 or ball.xcor() < -width / 2:
        x_velocity = -x_velocity

    window.update()

window.mainloop()

    

#turtle.done()