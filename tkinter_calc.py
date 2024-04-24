import tkinter as tk

def add1():
    a= int(e1.get())
    b = int(e2.get())
    c = a+b
    result = tk.Label(parent, text = c).place(x=30, y=120)
    
def sub1():
    a = int(e1.get())
    b = int(e2.get())
    c = a - b
    result = tk.Label(parent, text=c).place(x=30, y= 120)
parent = tk.Tk()

def mul1():
    a = int(e1.get())
    b = int(e2.get())
    c = a*b
    result = tk.Label(parent, text=c).place(x=30, y=120)
    
def div1():
    a = int(e1.get())
    b = int(e2.get())
    c = a/b
    result = tk.Label(parent, text = c).place(x=30, y=120)
parent.geometry("500x300")

A = tk.Label(parent, text = "A")
e1 = tk.Entry(parent)
A.place(x=30, y=30)
e1.place(x = 80, y =30)

B = tk.Label(parent, text = "B")
e2 = tk.Entry(parent)
B.place(x=30, y=60)
e2.place(x=80, y=60)

add = tk.Button(text = "Add", command = add1)
sub = tk.Button(text= "Subtract", command = sub1)
mul = tk.Button(text = "Multiply", command=mul1)
div = tk.Button(text = "Division", command=div1)
add.place(x=30, y=90)
sub.place(x=90, y=90)
mul.place(x=150, y=90)
div.place(x=210 , y=90)
parent.mainloop()