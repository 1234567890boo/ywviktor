from tkinter import *

class Fruit:
    def __init__(self):
        self.window=Tk()
        self.select=StringVar()
        self.select.set('apple')
        self.1=Radiobutton(self.window,text='apple',variable=self.select,value='apple')
        self.2=Radiobutton(self.window,text='banana',variable=self.select,value='banana')
        self.3=Radiobutton(self.window,text='orange',variable=self.select,value='orange')
        self.4=Radiobutton(self.window,text='mango',variable=self.select,value='mango')
        self.5=Radiobutton(self.window,text='grape',variable=self.select,value='grape')
        self.6=Radiobutton(self.window,text='peach',variable=self.select,value='peach')
        self.l=Label(self.window,text='Enter the quantitiy of fruit you want.')
        self.l2=Label(self.window,text='you have to pay $(selected fruit*num)')
        self.e=Entry(self.window)
        self.b=Button(self.window,text='Pay',command=self.findprice)
    def draw(self):
        self.apple.grid(row=0,column=0)
        self.banana.grid(row=0,column=1)
        self.orange.grid(row=0,column=2)
        self.mango.grid(row=1,column=0)
        self.grape.grid(row=1,column=1)
        self.peach.grid(row=1,column=2)
        self.l.grid(row=2,column=0,columnspan=3)
        self.e.grid(row=3,column=0,columnspan=3)
        self.l2.grid(row=4,column=0,columnspan=3)
        self.b.grid(row=5,column=0,columnspan=3)
    def findprice(self):
        num=int(self.e.get())
        fruit=self.select.get()
        fprice={'apple':1.32,'banana':0.24,'orange':2.5,'mango':3.00,'grape':0.05,'peach':1.63}
        self.l2['text']='you have to pay $'+str(fprice[fruit]*num)+' for '+str(self.select.get())
        
w=Fruit()
w.draw()
w.window.mainloop()
#Homework:give class dictionary with fruits and prices and display it on screen

#f1 f2 f3
#f4 f5 f6
#enter quantity of fruit
#________
#you have to pay $(selected fruit*num), "pay"
