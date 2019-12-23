import tkinter
import random
from tkinter import messagebox
def GCM(a,b):
        if a%b==0:
            return b
        else:
            return GCM(b,a%b)
def sample():
    if e.get()=='':
        messagebox.showwarning('warning','Please type something in entry Box 1')
    if e2.get()=='':
        messagebox.showwarning('warning','Please type something in entry Box 2')
    if e2.get()!='' and e.get()!='':
        a=int(e.get())
        b=int(e2.get())
        answer=GCM(a,b)
        #a2['text']=answer
        messagebox.showinfo('GCM answer!!!!!!!!!!!!!','the GCM is'+str(answer))
window=tkinter.Tk()
window.title('GCM Finder')
e=tkinter.Entry(window)
e2=tkinter.Entry(window)
b=tkinter.Button(window,text='Find GCM',command=sample)
l=tkinter.Label(window,text='Number 1')
l2=tkinter.Label(window,text='Number 2')
a2=tkinter.Label(window,text='')
l.pack()
e.pack()
l2.pack()
e2.pack()
b.pack()
a2.pack()
