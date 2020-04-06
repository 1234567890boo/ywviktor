from tkinter import *
from random import *

class Guess:
    def __init__(self):
        self.window=Tk()
        self.guess=['head','tail'][randint(0,1)]
        self.head=Radiobutton(self.window,text='head')
        self.tail=Radiobutton(self.window,text='tail')
        self.guess=Button(self.window,text='guess')
        self.show=Label(self.window,text='label')
    def draw(self):
        self.show.grid(row=0,column=0,columnspan=2)
        self.guess.grid(row=1,column=0,columnspan=2)
        self.tail.grid(row=2,column=0)
        self.head.grid(row=2,column=1)

w=Guess()
w.draw()
