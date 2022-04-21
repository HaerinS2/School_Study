import turtle
t=turtle.Turtle()
def maze(x, y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100, y+100)
        else:
            t.goto(x, y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

s = turtle.Screen()
t.shape("turtle")
t.speed(0)

maze (-300,200)

t.penup()
t.goto(-300, 250)
t.speed(1)
t.pendown()

s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")
s.listen()
s.mainloop()