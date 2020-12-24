from tkinter import *
cal = Tk()
cal.title("General Calculator") 



e= Entry(cal, width=75, borderwidth=15, font=( 'ariel',11, 'bold'),bg="black", fg="white") 
e.grid(row=0, column=0, columnspan=11, padx=20, pady=20)

def nos_click(num):
    e.insert(END, num)


def nos_clear():
    e.delete(0, END)


def nos_add():
    fnum = e.get()
    global firstNumber 
    global math
    math = "add"
    firstNumber = int(fnum)
    e.delete(0, END)

def nos_subtract():
    fnum = e.get()
    global firstNumber
    global math
    math = "subtract"
    firstNumber = int(fnum)
    e.delete(0, END)

def nos_multiply():
    fnum = e.get()
    global firstNumber
    global math
    math = "multiply"
    firstNumber = int(fnum)
    e.delete(0, END)


def nos_divide():
    fnum = e.get()
    global firstNumber
    global math
    math = "divide"
    firstNumber = int(fnum)
    e.delete(0, END)


    

def nos_equals():
    second_num = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, int(second_num) + int(firstNumber))
    if math == "multiply":
        e.insert(0, int(second_num) * int(firstNumber))
    if math == "divide":
        if int(second_num)==0:
            e.insert(0, "ERROR!!"+" "+"DIVISION BY ZERO IS ILLEGAL")
        else:
            e.insert(0, int(firstNumber) / int(second_num))
    if math == "subtract":
        e.insert(0, int(firstNumber) - int(second_num))



number_0 = Button(cal, text="0", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(0))
number_1 = Button(cal, text="1", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(1))
number_2 = Button(cal, text="2", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(2))
number_3 = Button(cal, text="3", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(3))
number_4 = Button(cal, text="4", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(4))
number_5 = Button(cal, text="5", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(5))
number_6 = Button(cal, text="6", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(6))
number_7 = Button(cal, text="7", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(7))
number_8 = Button(cal, text="8", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="blanched almond", command= lambda: nos_click(8))
number_9 = Button(cal, text="9", padx=70, pady=35, font=( 'ariel',11, 'bold'),activebackground="blanched almond", command= lambda: nos_click(9))

number_1.grid(row=1, column=0)
number_2.grid(row=1, column=1)
number_3.grid(row=1, column=2)

number_4.grid(row=2, column=0)
number_5.grid(row=2, column=1)
number_6.grid(row=2, column=2)

number_7.grid(row=3, column=0)
number_8.grid(row=3, column=1)
number_9.grid(row=3, column=2)
number_0.grid(row=4, column=1)

add = Button(cal, text="+", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="misty rose",  command= lambda: nos_add())
subtract = Button(cal, text="-", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="misty rose",  command= lambda: nos_subtract())
multiply = Button(cal, text="*", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="misty rose",  command= lambda: nos_multiply())
divide = Button(cal, text="/", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="misty rose",  command= lambda: nos_divide())

    
add.grid(row=4, column=0)
subtract.grid(row=4, column=2)
multiply.grid(row=4, column=3)
divide.grid(row=3, column=3)

CE = Button(cal, text="CE", padx=70, pady=35, font=( 'ariel',13, 'bold'), activebackground="dark slate grey", command= lambda: nos_clear())
equals = Button(cal, text="=", padx=70, pady=35, font=( 'ariel',11, 'bold'), activebackground="misty rose", command= lambda: nos_equals())
CE.grid(row=1, column=3)
equals.grid(row=2, column=3)


cal.mainloop()
