from tkinter import*
master=Tk()
master.title("Mooculatr")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
button2=StringVar()
button1=''
def button(num):
    global button1
    button1=button1+str(num)
    button2.set(button1)
def clear():
    global button1
    button1=''
    button2.set(button1)
def equal():
    global button1
    button3=str(eval(button1))
    button2.set(button3)
e1=Entry(master,textvariable=button2)
e1.grid(row=0,column=0,columnspan=4)
b1=Button(master,text='1',command=lambda:button(1)).grid(row=1,column=0)
b1=Button(master,text='2',command=lambda:button(2)).grid(row=1,column=1)
b1=Button(master,text='3',command=lambda:button(3)).grid(row=1,column=2)
b1=Button(master,text='4',command=lambda:button(4)).grid(row=2,column=0)
b1=Button(master,text='5',command=lambda:button(5)).grid(row=2,column=1)
b1=Button(master,text='6',command=lambda:button(6)).grid(row=2,column=2)
b1=Button(master,text='7',command=lambda:button(7)).grid(row=3,column=0)
b1=Button(master,text='8',command=lambda:button(8)).grid(row=3,column=1)
b1=Button(master,text='9',command=lambda:button(9)).grid(row=3,column=2)
b1=Button(master,text='0',command=lambda:button(0)).grid(row=1,column=3)
b1=Button(master,text='+',command=lambda:button('+')).grid(row=2,column=3)
b1=Button(master,text='-',command=lambda:button('-')).grid(row=3,column=3)
b1=Button(master,text='*',command=lambda:button('*')).grid(row=2,column=5)
b1=Button(master,text='/',command=lambda:button('/')).grid(row=3,column=5)
b1=Button(master,text='C',command=clear).grid(row=0,column=5)
b1=Button(master,text='=',command=equal).grid(row=1,column=5)


