from tkinter import*
master=Tk()
master.title("stuff")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
l1=Label(master,text="First Name").grid(row=0)
l1=Label(master,text="Last Name").grid(row=1)
l1=Label(master,text="Address").grid(row=2)
l1=Label(master,text="Phone Number").grid(row=3)
e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e4=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)

mainloop()
