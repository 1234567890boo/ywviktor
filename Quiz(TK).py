import tkinter
window=tkinter.Tk()
window.title('Game Start')
f1=tkinter.Frame(window)
f2=tkinter.Frame(window)
f3=tkinter.Frame(window)
f4=tkinter.Frame(window)

def yes():
    f1.grid_forget()
    f2.grid()
def no():
    f1.grid_forget()
    f3.grid()
def two():
    f2.grid_forget()
    f4.grid()
def eleven():
    pass

#frame 1
l=tkinter.Label(f1,text='Do you want to take a quiz')
b=tkinter.Button(f1,text='Yes',command=yes)
b2=tkinter.Button(f1,text='No',command=no)
l.grid(row=0,column=0,columnspan=2)
b.grid(row=1,column=0)
b2.grid(row=1,column=1)
f1.grid(row=0,column=0)

#frame yes
l2=tkinter.Label(f2,text='what is 1+1')
b3=tkinter.Button(f2,text='2',command=two)
b4=tkinter.Button(f2,text='11',command=eleven)
l2.grid(row=0,column=0,columnspan=2)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)

#frame no
l3=tkinter.Label(f3,text='THEN GO AWAY!')
b5=tkinter.Button(f3,text='exit',command=exit)
l3.grid(row=0,column=0)
b5.grid(row=1,column=0)

# frame 2
l4=tkinter.Label(f4,text='WRONG!!')
b6=tkinter.Button(f4,text='exit',command=exit)
l4.grid(row=0,column=0)
b6.grid(row=1,column=0)
