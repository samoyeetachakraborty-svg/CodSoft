import tkinter as tk
import math

window = tk.Tk()
window.title("Basic calculator")
window.geometry("1000x800")

display = tk.Entry(window, width = 40, fg="white", bg="black", justify = "left", font = ("Arial", 24))
display.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

a = 0
operator = ""

def click(num):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(num))

def sc_clr():
    display.delete(0, tk.END)

def add():
    global a, operator
    a = int(display.get())
    operator = "+"
    display.delete(0, tk.END)

def subtract():
    global a, operator
    a = int(display.get())
    operator = "-"
    display.delete(0, tk.END)

def multiply():
    global a, operator
    a = int(display.get())
    operator = "*"
    display.delete(0, tk.END)

def sin():
    global a, operator
    a = int(display.get())
    operator = "sin"
    display.delete(0, tk.END)

def cos():
    global a, operator
    a = int(display.get())
    operator = "cos"
    display.delete(0, tk.END)

def tan():
    global a, operator
    a = int(display.get())
    operator = "tan"
    display.delete(0, tk.END)

def divide():
    global a, operator
    a = int(display.get())
    operator = "/"
    display.delete(0, tk.END)

def equal():
    if operator == "sin":
        r = math.sin(a)
    elif operator == "cos":
        r = math.cos(a)
    elif operator == "tan":
        r = math.tan(a)

    else:
        b = int(display.get())

        if operator == "+":
            r = a + b
        elif operator == "-":
            r = a - b
        elif operator == "*":
            r = a * b 
        elif operator == "/":
            r = a / b

    display.delete(0, tk.END)
    display.insert(0, str(r))



b1 = tk.Button(window, text="1", width = 10, height = 3, command=lambda: click(1))
b2 = tk.Button(window, text="2", width = 10, height = 3, command=lambda: click(2))
b3 = tk.Button(window, text="3", width = 10, height = 3, command=lambda: click(3))
b4 = tk.Button(window, text="4", width = 10, height = 3, command=lambda: click(4))
b5 = tk.Button(window, text="5", width = 10, height = 3, command=lambda: click(5))
b6 = tk.Button(window, text="6", width = 10, height = 3, command=lambda: click(6))
b7 = tk.Button(window, text="7", width = 10, height = 3, command=lambda: click(7))
b8 = tk.Button(window, text="8", width = 10, height = 3, command=lambda: click(8))
b9 = tk.Button(window, text="9", width = 10, height = 3, command=lambda: click(9))
b0 = tk.Button(window, text="0", width = 10, height = 3, command=lambda: click(0))

add_button = tk.Button(window, text="+", width = 10, height = 3, command=add, bg="yellow")
sub_button = tk.Button(window, text="-", width = 10, height = 3, command=subtract, bg="yellow")
mul_button = tk.Button(window, text="*", width = 10, height = 3, command=multiply, bg="yellow")
div_button = tk.Button(window, text="/", width = 10, height = 3, command=divide, bg="yellow")
sin_button = tk.Button(window, text = "sin", width = 10, height = 3, command=sin, bg="red", fg="white")
cos_button = tk.Button(window, text = "cos", width = 10, height = 3, command=cos, bg="red", fg="white")
tan_button = tk.Button(window, text = "tan", width = 10, height = 3, command=tan, bg="red", fg="white")

equal_button = tk.Button(window, text="=", width = 10, height = 3, command=equal, bg="green")
clear_button = tk.Button(window, text="C", width = 10, height = 3, command=sc_clr)


b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

b0.grid(row=4, column=1)

add_button.grid(row=1, column=3)
sub_button.grid(row=2, column=3)
mul_button.grid(row=3, column=3)
div_button.grid(row=4, column=3)
sin_button.grid(row=1, column=4)
cos_button.grid(row=2, column=4)
tan_button.grid(row=3, column=4)

equal_button.grid(row=4, column=2)
clear_button.grid(row=4, column=0)

window.mainloop()