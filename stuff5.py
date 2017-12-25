from tkinter import*
master=Tk()
master.title("IDK what to call this")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
def ShowCoice():
    print(v.get())
l1=Label(master,text="The Nerd Test!").pack(anchor=W)
v=IntVar()
v.set(1)
stuff=[("pie",1),("pi",2)]
for txt,val in stuff:
    Radiobutton(master,text=txt,padx=20,variable=v,command=ShowCoice,value=val).pack(anchor=W)
