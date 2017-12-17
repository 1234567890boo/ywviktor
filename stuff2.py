from tkinter import*
master=Tk()
master.title("temp convert")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
num=StringVar()
def ctf():
    c=e1.get()
    c=float(c)
    f=c*9/5+32
    num.set(f)
def ftc():
    f=e1.get()
    f=float(f)
    c=f/9*5-32
    num.set(c)
l1=Label(master,textvariable=num).grid(row=1)
e1=Entry(master)
e1.grid(row=0,column=0)
b1=Button(master,text="celcius to fahrenheit",command=ctf)
b1.grid(row=0,column=1)
b2=Button(master,text="fahrenheit to celcius",command=ftc)
b2.grid(row=1,column=1)
mainloop()
