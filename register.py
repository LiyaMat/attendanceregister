from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import *
import datetime
import time

root = Tk()
root.title("ATTENDANCE REGISTER")
root.geometry('1350x700+0+0')
root.configure(background='Black')
# frame setup
LeftMayFrame = Frame(root, width=1000, height=650, bd=8, relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(root, width=350, height=650, bd=8, relief="raise")
RightMayFrame.pack(side=LEFT)

LeftMayFrame1 = Frame(LeftMayFrame, width=1000, height=350, bd=8, relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=600, bd=8, relief="raise")
LeftMayFrame2.pack(side=TOP)

RightMayFrame1 = Frame(RightMayFrame, width=350, height=215, bd=8, relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2 = Frame(RightMayFrame, width=350, height=415, bd=8, relief="raise")
RightMayFrame2.pack(side=TOP)

# variableinitialization
dateoforder = StringVar()
value0, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

# components
dateoforder.set(time.strftime("%d/%m/%Y"))
#mark
def markregister():
    if value0.get()=="/":
        value0.set("/")
        value2.set("/")
        value1.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        value10.set("/")
        value11.set("/")
        value12.set("/")
    elif value0.get()=="0":
        value0.set("0")
        value1.set("0")
        value2.set("0")
        value3.set("0")
        value4.set("0")
        value5.set("0")
        value6.set("0")
        value7.set("0")
        value8.set("0")
        value9.set("0")
        value10.set("0")
        value11.set("0")
        value12.set("0")
    elif value0.get()=="S":
        value0.set("S")
        value1.set("S")
        value3.set("S")
        value2.set("S")
        value4.set("S")
        value5.set("S")
        value6.set("S")
        value7.set("S")
        value8.set("S")
        value9.set("S")
        value10.set("S")
        value11.set("S")
        value12.set("S")
    elif value0.get()=="A":
        value0.set("A")
        value1.set("A")
        value3.set("A")
        value4.set("A")
        value2.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        value8.set("A")
        value9.set("A")
        value10.set("A")
        value11.set("A")
        value12.set("A")
    elif value0.get()=="L":
        value0.set("L")
        value1.set("L")
        value2.set("L")
        value3.set("L")
        value4.set("L")
        value5.set("L")
        value6.set("L")
        value7.set("L")
        value8.set("L")
        value9.set("L")
        value10.set("L")
        value11.set("L")
        value12.set("L")
    elif value0.get()==" ":
        value0.set("")
        value1.set("")
        value2.set("")
        value3.set("")
        value4.set("")
        value5.set("")
        value6.set("")
        value7.set("")
        value8.set("")
        value9.set("")
        value10.set("")
        value11.set("")
        value12.set("")


#exitfunction
def qexit():
    qexit=messagebox.askyesno("Exit System","Do you want to leave?")
    if qexit>0:
        root.destroy()
        return
#reset
def reset():
    value0.set("")
    value1.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")

# Leftmayframe1
slno = Label(LeftMayFrame1, font=('arial', '10', "bold"), text="Sl no", bd=16)
slno.grid(row=0, column=0, sticky=W)
Student_no = Label(LeftMayFrame1, font=('arial', '10', "bold"), text="Student No", bd=16)
Student_no.grid(row=0, column=1, sticky=W)
Student_name = Label(LeftMayFrame1, font=('arial', '10', "bold"), text="Student Name", bd=16)
Student_name.grid(row=0, column=2, sticky=W)
course_code = Label(LeftMayFrame1, font=('arial', '10', "bold"), text="Course Code", bd=16)
course_code.grid(row=0, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame1, textvariable=value0, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=0, column=4)

btnArrow = Button(LeftMayFrame1, text="Fill", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1,command=markregister).grid(row=0, column=5)
btnReset = Button(LeftMayFrame1, text="Reset", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1,command=reset).grid(row=0, column=6)
btnExit = Button(LeftMayFrame1, text="Exit", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                 height=1,command=qexit).grid(row=0, column=7)
lbldateoforder = Label(LeftMayFrame1, font=('arial', 10, 'bold'), textvariable=dateoforder, padx=2, pady=2, bd=2,
                       fg='black', bg='white', relief='sunken').grid(row=0, column=8, sticky=W)

# lefmayframe2
slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="1", bd=16)
slno.grid(row=0, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="1234", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=0, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Ann Maria", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=0, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="1005", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=0, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value1, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=0, column=4)


btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=0, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=0, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=0, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=0, column=8)


slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="2", bd=16)
slno.grid(row=1, column=0, sticky=W)
Student_no = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="1297", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no.grid(row=1, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Shana Mary", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=1, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="C345", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=1, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value2, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=1, column=4)


btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=1, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=1, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=1, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=1, column=8)


slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="3", bd=16)
slno.grid(row=2, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="1298", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=2, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Steffy Eliza", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=2, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="m9090", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=2, column=3, sticky=W)


box = ttk.Combobox(LeftMayFrame2, textvariable=value3, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=2, column=4)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=2, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=2, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=2, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=2, column=8)


slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="4", bd=16)
slno.grid(row=3, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="167", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=3, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Amy Rosy", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=3, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="op05", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=3, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value4, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=3, column=4)


btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=3, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=3, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=3, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=3,column=8)


slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="5", bd=16)
slno.grid(row=4, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="6784", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=4, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Sona Joseph", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=4, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="lo085", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=4, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value0, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=4, column=4)

box = ttk.Combobox(LeftMayFrame2, textvariable=value5, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=4, column=4)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=4, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=4, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=4, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=4, column=8)


slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="6", bd=16)
slno.grid(row=5, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="1674", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=5, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Sana Kuruvila", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=5, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="A", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=5, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value6, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=5, column=4)

box = ttk.Combobox(LeftMayFrame2, textvariable=value1, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=5, column=4)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=5, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=5, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=5, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=5, column=8)


slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="7", bd=16)
slno.grid(row=6, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="1288", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=6, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Anita Mariya", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=6, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="005", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=6, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value7, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=6, column=4)


btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=6, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=6, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=6, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=6, column=8)


slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="8", bd=16)
slno.grid(row=7, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="18834", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=7, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Taniya Elizabeth", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=7, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="maw05", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=7, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value8, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=7, column=4)

btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=7, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=7, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=7, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=7, column=8)

slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="9", bd=16)
slno.grid(row=8, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="907", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=8, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Neethu Charly", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=8, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="ju08", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=8, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value9, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=8, column=4)

btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=8, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=8, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=8, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=8, column=8)

slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="10", bd=16)
slno.grid(row=9, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="9089", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=9, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Leona Maria", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=9, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="CS309", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=9, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value10, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=9, column=4)

btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=9, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=9, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=9, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=9, column=8)

slno = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="11", bd=16)
slno.grid(row=10, column=0, sticky=W)
Student_no_1 = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="907", bd=2, width=18, padx=2, pady=2,
                     fg='black')
Student_no_1.grid(row=10, column=1, sticky=W)
Student_name = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="Liss Mathew", bd=2, width=12, padx=2, pady=2,
                     fg='black')
Student_name.grid(row=10, column=2, sticky=W)
course_code = Label(LeftMayFrame2, font=('arial', '10', "bold"), text="j908", bd=2, width=12, padx=2, pady=2,
                    fg='black')
course_code.grid(row=10, column=3, sticky=W)
box = ttk.Combobox(LeftMayFrame2, textvariable=value11, state='readonly')
box['values'] = (' ', '/', 'L', '0', 'A', 'S')
box.current(0)
box.grid(row=10, column=4)

btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=12,
                  height=1).grid(row=10, column=5)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=10, column=6)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=10, column=7)
btnSpace = Button(LeftMayFrame2, text=" ", padx=2, pady=2, bd=2, fg='black', font=('arial', 10, 'bold'), width=11,
                  height=1).grid(row=10, column=8)

#image
cont=Canvas(RightMayFrame2,width=350,height=215)
cont.grid(row=0,column=0)
img1=PhotoImage(file="download.png")
cont.create_image(200,200,image=img1)
#image
cont=Canvas(RightMayFrame1,width=350,height=215)
cont.grid(row=0,column=0)
img2=PhotoImage(file="Capture.PNG")
cont.create_image(200,200,image=img2)



root.mainloop()
