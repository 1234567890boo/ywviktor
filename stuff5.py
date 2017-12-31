from tkinter import*
master=Tk()
master.title("IDK what to call this")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
def ShowCoice():
    g=v.get()
    v.set(g)
    l2=Label(master,textvariable=v).grid(row=6,sticky=W)
a=1
l1=Label(master,text="What's your Favorte Color?").grid(row=0,sticky=W)
v=StringVar()
stuff=[("Blue",'Correct'),("Green",'Incorrect'),("Red",'Wrong'),("Orange",'Not Right'),("Yellow",'Not Correct')]
for txt,val in stuff:
    Radiobutton(master,text=txt,padx=20,variable=v,command=ShowCoice,value=val).grid(row=a,column=0)
    a=a+1
