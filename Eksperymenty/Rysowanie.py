import turtle
t = turtle.Turtle('circle')

t.color('orange')

def rysuj(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(rysuj)

def main():
    turtle.listen()
    t.ondrag(rysuj)
    turtle.mainloop()

main()