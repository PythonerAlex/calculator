from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import math

expression = ''
equation = ''
sqrt_value = ''


window = tk.Tk()

window.title("Calculator (Super Early Beta Version 1.0)")

frame_buttons = Frame(master=window)
frame_result = Frame(master=window)


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ''
    equation.set('')


def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set(" Error ")
        expression = ''


def delete():
    pass


def sqrt(num):
    pass


equation = StringVar()
equation.set('')
answer = Label(window, textvariable=equation)
answer.grid(column=0, row=8)

seven = Button(window, text="7", command=lambda: press(7))
seven.grid(column=0, row=1)

eight = Button(window, text="8", command=lambda: press(8))
eight.grid(column=1, row=1)

nine = Button(window, text='9', command=lambda: press(9))
nine.grid(column=2, row=1)

four = Button(window, text="4", command=lambda: press(4))
four.grid(column=0, row=2)

five = Button(window, text='5', command=lambda: press(5))
five.grid(column=1, row=2)

six = Button(window, text='6', command=lambda: press(6))
six.grid(column=2, row=2)

one = Button(window, text='1', command=lambda: press(1))
one.grid(column=0, row=3)

two = Button(window, text='2', command=lambda: press(2))
two.grid(column=1, row=3)

three = Button(window, text='3', command=lambda: press(3))
three.grid(column=2, row=3)

C = Button(window, text='C', command=clear)
C.grid(column=0, row=4)

zero = Button(window, text='0', command=lambda: press(0))
zero.grid(column=1, row=4)

point = Button(window, text='.', command=lambda: press('.'))
point.grid(column=2, row=4)

equal = Button(window, text='=', command=equal)
equal.grid(column=3, row=4)

plus = Button(window, text="+", command=lambda: press('+'))
plus.grid(column=3, row=3)

minus = Button(window, text='-', command=lambda: press('-'))
minus.grid(column=3, row=2)

multiply = Button(window, text='x', command=lambda: press('*'))
multiply.grid(column=3, row=1)

delete = Button(window, text='⌫', command=delete)
delete.grid(column=3, row=0)

divide = Button(window, text='/', command=lambda: press('/'))
divide.grid(column=2, row=0)

squared = Button(window, text='^', command=lambda: press('**'))
squared.grid(column=1, row=0)

square_root = Button(window, text='√', command=sqrt(sqrt_value))
square_root.grid(column=0, row=0)

air1 = Label(window, text='')
air1.grid(column=0, row=5)

air2 = Label(window, text='')
air2.grid(column=0, row=6)

result_label = Label(window, text="RESULT", font=20)
result_label.grid(column=0, row=7)

window.mainloop()