import time
from tkinter import*
master=Tk()
master.title("Timer")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
SSS=0
MMM=0
HHH=0
def start():
    global SSS,MMM,HHH, state
    if state:
        SSS=SSS+1
        if SSS>=60:
            MMM=MMM+1
            SSS=0
        if MMM>=60:
            HHH=HHH+1
            MMM=0
        show='{0:02d}:{1:02d}:{3:02d}'.format(HHH,MMM,SSS)
        timetext.configure(text=show)
        master.update()
def start1():
    state=True
def reset():
    global state,SSS,MMM,HHH
    SSS=0
    MMM=0
    HHH=0
    state=False
def pause():
    global state
    state=False
b1=Button(master,text="start",command=start1).grid(row=1,column=0)
b1=Button(master,text="pause",command=pause).grid(row=1,column=2)
b1=Button(master,text="reset",command=reset).grid(row=1,column=3)
l1.Label(master,text=
