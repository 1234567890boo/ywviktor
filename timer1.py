import time
from tkinter import*
master=Tk()
master.title("Timer")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
v=StringVar()
def timer():
    t=int(e1.get())
    for n in range(t,-1,-1):
        sf="{:02d}:{:02d}".format(*divmod(n,60))
        time.sleep(1)
        v.set(sf)
        master.update()
l1=Label(master,textvariable=v,font=(None,30)).grid(row=0,column=0)
e1=Entry(master)
e1.grid(row=1,column=0)
b1=Button(master,text="Start",command=timer).grid(row=2,column=0)
