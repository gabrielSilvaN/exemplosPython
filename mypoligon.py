import turtle
pol = turtle.Turtle()

def poligono(pol,n):
    for i in range(n):
        pol.fd(100)
        pol.lt(360/n)

    turtle.mainloop()

poligono(pol,80)
