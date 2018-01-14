import time
from tkinter import*
master=Tk()
master.title("Timer")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
textt=StringVar()
def update_time():
    global SSS,MMM,HHH, state
    if state:
        SSS=SSS+1
        if SSS>=60:
            MMM=MMM+1
            SSS=0
        if MMM>=60:
            HHH=HHH+1
            MMM=0
        t=p.format(HHH,MMM,SSS)
        textt.set(t)
    master.after(1,update_time)
def start1():
    global state
    state=True
    update_time()
def reset():
    global state,SSS,MMM,HHH
    SSS=0
    MMM=0
    HHH=0
    state=False
    t=p.format(HHH,MMM,SSS)
    textt.set(t)
def pause():
    global state
    state=False
p='{0:02d}:{1:02d}:{2:02d}'
SSS=0
MMM=0
HHH=0
state=False
timetext=Label(master,textvariable=textt,font=('None',25)).pack()
b1=Button(master,text="start",command=start1).pack()
b1=Button(master,text="pause",command=pause).pack()
b1=Button(master,text="reset",command=reset).pack()
update_time()
mainloop()
