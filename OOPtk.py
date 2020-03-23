from tkinter import *

class App:
    def __init__(self):
        self.window=Tk()
        self.window.title('OOP Tkinter')
        self.b=Button(self.window,text='Convert',command=self.countdown)
        self.e=Entry(self.window)
        self.l=Label(self.window,text='Label')
    def put(self):
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def convert(self):
        get=self.e.get().lower()
        self.l['text']=get.upper()
        self.e.delete(0,END)
        self.e.insert(0,get)
    def countdown(self):
        if self.e.get().isnumeric()==True:
            t=int(self.e.get())
            self.e.delete(0,END)
            self.e.insert(0,t-1)
            self.l['text']=t
            t-=1
            print(t)
            if t<=0:
                return
            self.window.after(1000,self.countdown)
        else:
            self.convert()
        
w=App()

w.put()
    
#HW:make coundown timer
