import turtle
bob = turtle.Turtle()


def quadrado(bob,length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
    
    #turtle.mainloop()

def quadrado2(bob,length):
    for i in range(4):
        bob.lt(90)
        bob.fd(length)
        


quadrado(bob, 100)
quadrado(bob, -200)
quadrado(bob, 200)
quadrado(bob, -100)

quadrado2(bob, 100)
quadrado2(bob, -200)
quadrado2(bob,200)
quadrado2(bob,-100)

bob.fd(300)
bob.lt(90)
bob.fd(300)
bob.lt(90)
bob.fd(600)
bob.lt(90)
bob.fd(600)
bob.lt(90)
bob.fd(600)
bob.lt(90)
bob.fd(300)

