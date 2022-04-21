from tkinter import *
window = Tk()

def process1():
    C = float(e2.get())
    F = (9/5)*C + 32
    e1.insert(0,str(F))

def process2():
    F = float(e1.get())
    C = (F-32)*5/9

l1 = Label(window, text = "화씨")
l2 = Label(window, text = "섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text = "화씨에서 섭씨로", command=process1)
b2 = Button(window, text = "섭씨에서 화씨로", command=process2)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()