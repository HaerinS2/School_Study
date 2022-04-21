import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(len):
    for i in range(4):
        t.forward(50)
        t.left(90)
def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color("#E6E6FA")
    square()
    t.turtle.end_fill()

s = turtle.turtle.Screen()
s.turtle.onscreenclick(drawit)

input("종료하려면 아무 키나 누르세요.")