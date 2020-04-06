from tkinter import *

class App:
    def __init__(self):
        self.window=Tk()
        self.window.title('OOP Tkinter')
        self.b=Button(self.window,text='Convert',command=self.ts)
        self.e=Entry(self.window)
        self.l=Label(self.window,text='Label')
        self.time=IntVar()
    def put(self):
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def convert(self):
        get=self.e.get().lower()
        self.l['text']=get.upper()
        self.e.delete(0,END)
        self.e.insert(0,get)
    def ts(self):
        self.time.set((int(self.e.get())))
        self.countdown()
    def countdown(self):
        if self.e.get().isnumeric()==True:
            self.l['text']=self.time.get()
            self.b['state']=DISABLED
            self.time.set(self.time.get()-1)
            print(self.time.get())
            if self.time.get()<=-1:
                self.b['state']=NORMAL
            else:
                self.window.after(1000,self.countdown)
        else:
            self.convert()
            self.b['state']=NORMAL

        
w=App()

w.put()
    
#HW:make coundown timer
