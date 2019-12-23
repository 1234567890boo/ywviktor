import tkinter
from tkinter import messagebox

window=tkinter.Tk()
window.title('Search?')

data={'viktor':'likes color black','rohit':'is a teacher at youngwonks','henry':'is a very good writer','andrew':'likes programing','olga':'is a profetional parent','dylan':'like video games'}
def search():
    if e.get().lower() in data:
        l.insert(0.0,e.get().lower()+' : '+data[e.get().lower()])
    else:
        l.insert(0.0,'we have no dat on that person')
def clear():
    l.delete(0.0,tkinter.END)
    e.delete(0,tkinter.END)
e=tkinter.Entry(window)
b=tkinter.Button(window,text='Search',command=search)
b2=tkinter.Button(window,text='Clear',command=clear)
l=tkinter.Text(window,height=2,width=35)

e.grid(row=0,column=0)
b.grid(row=0,column=1)
b2.grid(row=0,column=2)
l.grid(row=1,column=0,columnspan=2)
