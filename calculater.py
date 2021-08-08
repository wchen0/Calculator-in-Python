from calculation import calculation
from tkinter import *


root = Tk()

root.title("Simple Calculater")


e = Entry(root, width=37, borderwidth=7)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 


def button_click(X):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(X))


def button_clear():
	e.delete(0, END)


def result():
	current = e.get()
	e.delete(0, END)
	if calculation(current) == None:
		e.insert(0, str(current) + ' Invalid Input!')
	else:
		e.insert(0, str(current) + '=' + str(calculation(current)))
	



button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))

button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text='+', padx=39, pady=20, command=lambda: button_click('+'))
button_subtract = Button(root, text='-', padx=40, pady=20, command=lambda: button_click('-'))
button_multiply = Button(root, text='*', padx=40, pady=20, command=lambda: button_click('*'))
button_divide = Button(root, text='/', padx=40, pady=20, command=lambda: button_click('/'))

button_equal = Button(root, text=' = ', padx=34, pady=20, command=result)
button_clear = Button(root, text='Clear', padx=28, pady=20, command=button_clear)
button_left_bracket = Button(root, text='(', padx=40, pady=20, command=lambda: button_click('('))
button_right_bracket = Button(root, text=')', padx=40, pady=20, command=lambda: button_click(')'))



# Put the buttons on screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_add.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2)

button_left_bracket.grid(row=6, column=0)
button_right_bracket.grid(row=6, column=1)
button_clear.grid(row=6, column=2)


root.mainloop()

