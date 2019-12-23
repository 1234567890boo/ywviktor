#tkinter homework: Calculator
import tkinter
from tkinter import messagebox

def add():
    if a.get()=='' or a2.get()=='':
        messagebox.showwarning('WARNING','All Fields Must Be Filled Out')
    else:
        add1=int(a.get())+int(a2.get())
        l['text']=add1
def minus():
    if a.get()=='' or a2.get()=='':
        messagebox.showwarning('WARNING','All Fields Must Be Filled Out')
    else:
        minus1=int(a.get())-int(a2.get())
        l['text']=minus1
def devide():
    if a.get()=='' or a2.get()=='':
        messagebox.showwarning('WARNING','All Fields Must Be Filled Out')
    else:
        devide1=int(a.get())//int(a2.get())
        l['text']=devide1
def multiply():
    if a.get()=='' or a2.get()=='':
        messagebox.showwarning('WARNING','All Fields Must Be Filled Out')
    else:
        multiply1=int(a.get())*int(a2.get())
        l['text']=multiply1

window=tkinter.Tk()
window.title('The Best Calculator!!!!!')
a=tkinter.Entry(window)
a2=tkinter.Entry(window)
b=tkinter.Button(window,text='ADD',command=add)
b2=tkinter.Button(window,text='SUBTRACT',command=minus)
b3=tkinter.Button(window,text='DIVIDE',command=devide)
b4=tkinter.Button(window,text='MULTIPLY',command=multiply)
l=tkinter.Label(window)


a.grid(row=0,column=0)
a2.grid(row=0,column=1)
b.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=2,column=0)
b4.grid(row=2,column=1)
l.grid(row=3,column=1)
