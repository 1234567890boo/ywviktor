from tkinter import*
master=Tk()
master.title("temp convert")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''

def ctf():
    c=num.get()
    c=float(c)
    f=c*9/5+32
    print(f)
e1=Entry(master)
e1.pack()
num=IntVar()
b1=Button(master,text="celcius to fahrenheit",command=ctf)
b1.pack()
b1=Button(master,text="fahrenheit to celcius")
mainloop()
