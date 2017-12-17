from tkinter import*
master=Tk()
master.title("Mooculatr")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
def button1():
    c=e1.get()
    c=int(c)
e1=Entry(master)
e1.grid(row=0,column=0,columnspan=3)
b1=Button(master,text='1').grid(row=1,column=0)
b1=Button(master,text='2').grid(row=1,column=1)
b1=Button(master,text='3').grid(row=1,column=2)
b1=Button(master,text='4').grid(row=2,column=0)
b1=Button(master,text='5').grid(row=2,column=1)
b1=Button(master,text='6').grid(row=2,column=2)
b1=Button(master,text='7').grid(row=3,column=0)
b1=Button(master,text='8').grid(row=3,column=1)
b1=Button(master,text='9').grid(row=3,column=2)
b1=Button(master,text='+').grid(row=0,column=4)
b1=Button(master,text='-').grid(row=1,column=4)
b1=Button(master,text='*').grid(row=2,column=4)
b1=Button(master,text='/').grid(row=3,column=4)
b1=Button(master,text='clear').grid(row=4,column=0)
b1=Button(master,text='enter').grid(row=4,column=1)


