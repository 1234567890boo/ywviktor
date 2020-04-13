from tkinter import *
from random import *

class Guess:
    def __init__(self):
        self.window=Tk()
        self.select=StringVar()
        self.select.set('head')
        self.guess=['head','tail'][randint(0,1)]
        self.head=Radiobutton(self.window,text='head',variable=self.select,value='head')
        self.tail=Radiobutton(self.window,text='tail',variable=self.select,value='tail')
        self.b=Button(self.window,text='guess',command=self.find)
        self.show=Label(self.window,text='label')
    def find(self):
        if self.select.get()==self.guess:
            self.show['text']='Correct'
        else:
            self.show['text']='Wrong'
    def draw(self):
        self.show.grid(row=0,column=0,columnspan=2)
        self.b.grid(row=1,column=0,columnspan=2)
        self.tail.grid(row=2,column=0)
        self.head.grid(row=2,column=1)

w=Guess()
w.draw()
w.window.mainloop()
#Homework:

#f1 f2 f3
#f4 f5 f6
#enter quantity of fruit
#________
#you have to pay (selected fruit*num)
