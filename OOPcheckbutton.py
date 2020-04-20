from tkinter import *
import json

##fruits={'apple':{'price':1.32,'row':0,'column':0},
##          'banana':{'price':0.24,'row':0,'column':1},
##          'orange':{'price':2.5,'row':0,'column':2},
##          'mango':{'price':3.00,'row':1,'column':0},
##          'grape':{'price':0.05,'row':1,'column':1},
##          'peach':{'price':1.63,'row':1,'column':2}}


##fruits_json = json.dumps(fruits, sort_keys=True, indent=2)
##f = open("fruits.json","w")
##f.write(fruits_json)
##f.close()

##vim fruits.json to read/wright json file
##:x to save and close

with open('fruits.json') as f:
  fruits=json.load(f)

class Fruit:
    def __init__(self,fruits):
        self.window=Tk()
        self.fruits=fruits
        self.butt={}
        self.select={'apple':IntVar(),'banana':IntVar(),'orange':IntVar(),'mango':IntVar(),'grape':IntVar(),'peach':IntVar(),}
        for n in self.fruits.keys():
            self.butt[n]=Checkbutton(self.window,text=n,variable=self.select[n])
        self.l=Label(self.window,text='Enter the quantitiy of fruit you want.')
        self.l2=Label(self.window,text='you have to pay $(selected fruit*num)')
        self.e=Entry(self.window)
        self.b=Button(self.window,text='Pay',command=self.findprice)
    def draw(self):
        for s in self.fruits.keys():
            self.butt[s].grid(row=self.fruits[s]['row'],column=self.fruits[s]['column'])
        self.l.grid(row=3,column=0,columnspan=3)
        self.e.grid(row=4,column=0,columnspan=3)
        self.l2.grid(row=5,column=0,columnspan=3)
        self.b.grid(row=6,column=0,columnspan=3)
    def findprice(self):
        num=int(self.e.get())
        total=0
        for e in self.select:
            p=self.fruits[e]['price']
            v=self.select[e].get()
            total=total+(p*v*num)
        self.l2['text']='you have to pay $'+str(total)+' for '+str(self.select.keys())

w=Fruit(fruits)
w.draw()
w.window.mainloop()
#Homework:give class dictionary with fruits and prices and display it on screen

#f1 f2 f3
#f4 f5 f6
#enter quantity of fruit
#________
#you have to pay $(selected fruit*num), "pay"
