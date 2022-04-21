import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(len):
    for i in range(4):
        t.forward(len)
        t.left(90)
square(50)