from tkinter import*
master=Tk()
master.title("stuff")
def save():
    g1=e1.get()
    print(g1)
    g2=e2.get()
    print(g2)
    g3=e3.get()
    print(g3)
    g4=e4.get()
    print(g4)
    file_var=open("stuff.txt",'a')
    file_var.write(g1+' ' +g2+' ' +g3+' '+g4+'\n')
    file_var.close()
def show():
    r=5
    file_var=open("stuff.txt",'r')
    for s in file_var:
        print(s)
        l1=Label(master,text=str(s)).grid(row=r)
        r=r+1
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
l1=Label(master,text="First Name").grid(row=0)
l1=Label(master,text="Last Name").grid(row=1)
l1=Label(master,text="Email Address").grid(row=2)
l1=Label(master,text="Phone Number").grid(row=3)
e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e4=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
b1=Button(master,text="Save",command=save).grid(row=4,column=1)
b2=Button(master,text="Show",command=show).grid(row=5,column=1)
mainloop()
