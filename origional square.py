import turtle
bob = turtle.Turtle()
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)

alice = turtle.Turtle()
square(alice)

def square(t, length):
    for i in range(4):
        t.fd(50)
        t.lt(90)

square(bob, 100)

tictac = turtle.Turtle()
square(tictac , alice)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 7, 70)



turtle.mainloop()
