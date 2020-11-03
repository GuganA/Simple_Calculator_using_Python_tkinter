from tkinter import *
from math import *
cal=Tk()
cal.title("Calulator")
cal.iconbitmap("E:\python demo\Python Tkinter demo\calculator\c.ico")
cal.configure(bg="#333333")
e=Entry(cal, width=30,borderwidth=2,font=("Calibri",15))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20,ipady=5)

def click(num):
    n=e.get()
    e.delete(0,END)
    e.insert(1,str(n)+str(num))

def clearAll():
    e.delete(0,END)

def clearone():
    e.delete(1,END)

def add():
    num1=e.get()
    global n1
    global c1
    c1="add"
    n1=int(num1)
    e.delete(0,END)
def subtract():
    num1=e.get()
    global n1
    global c1
    c1="difference"
    n1=num1
    e.delete(0,END)
def multiply():
    num1=e.get()
    global n1
    global c1
    c1="product"
    n1=num1
    e.delete(0,END)
def division():
    num1=e.get()
    global n1
    global c1
    c1="divide"
    n1=num1
    e.delete(0,END)
def mod():
    num1=e.get()
    global n1
    global c1
    c1="module"
    n1=num1
    e.delete(0,END)

def b_equal():
    num2=e.get()
    n2=num2
    e.delete(0,END)
    if c1=='add':
        e.insert(0,float(n1) + float(n2))
    elif c1=='difference':
        e.insert(0,float(n1) - float(n2))
    elif c1=='divide':
        e.insert(0,int(n1) / int(n2))
    elif c1=='product':
        e.insert(0,float(n1) * float(n2))
    elif c1=='module':
        e.insert(0,float(n1) % float(n2))

b1=Button(cal,text='1',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(1)).grid(row=3,column=0)
b2=Button(cal,text='2',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(2)).grid(row=3,column=1)
b3=Button(cal,text='3',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(3)).grid(row=3,column=2)
b4=Button(cal,text='4',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(4)).grid(row=2,column=0)
b5=Button(cal,text='5',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(5)).grid(row=2,column=1)
b6=Button(cal,text='6',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(6)).grid(row=2,column=2)
b7=Button(cal,text='7',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(7)).grid(row=1,column=0)
b8=Button(cal,text='8',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(8)).grid(row=1,column=1)
b9=Button(cal,text='9',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(9)).grid(row=1,column=2)
b0=Button(cal,text='0',font=(10),padx=50,pady=15,bg='black',fg='white',command=lambda:click(0)).grid(row=4,column=1)
b=Button(cal,text='.',font=(10),padx=52,pady=15,bg='black',fg='white',command=lambda:click(".")).grid(row=4,column=0)
clear=Button(cal,text='CE',font=(10),padx=45,pady=15,bg='black',fg='red',command=clearAll).grid(row=4,column=2)
clear=Button(cal,text='%',font=(10),padx=50,pady=15,bg='black',fg='red',command=mod).grid(row=5,column=2)
add=Button(cal,text='+',font=(10),padx=50,pady=15,bg='black',fg='white',command=add).grid(row=5,column=0)
sub=Button(cal,text='-',font=(10),padx=52,pady=15,bg='black',fg='white',command=subtract).grid(row=6,column=1)
mul=Button(cal,text='x',font=(10),padx=50,pady=15,bg='black',fg='white',command=multiply).grid(row=5,column=1)
div=Button(cal,text='/',font=(10),padx=52,pady=15,bg='black',fg='white',command=division).grid(row=6,column=0)
equal=Button(cal,text='=',font=(10),padx=50,pady=15,bg='black',fg='blue',command=b_equal).grid(row=6,column=2)

cal.mainloop()
