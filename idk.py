import time
from tkinter import*
master=Tk()
master.title("stuff")
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry



canvasw=200
canvash=100
w=Canvas(master,width=canvasw,height=canvash)
w.pack()
w.create_rectangle(50,20,150,80,fill="#476042")
w.create_rectangle(65,35,135,65,fill="yellow")
w.create_line(0,0,50,20,fill="#476042",width=3)
w.create_line(0,100,50,80,fill="#476042",width=3)
w.create_line(150,20,200,0,fill="#476042",width=3)
w.create_line(150,80,200,100,fill="#476042",width=3)



canvasw=190
canvash=150
w=Canvas(master,width=canvasw,height=canvash)
w.pack()
w.create_oval(50,50,100,100)'''
canvasw=500
canvash=150
def paint(event):
    python_green="#476042"
    x1,y1=(event.x-1),(event.y-100)
    x2,y2=(event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2,fill=python_green)
w=Canvas(master,width=canvasw,height=canvash)
w.pack(expand=YES,fill=BOTH)
w.bind("<B1-Motion>",paint)
message=Label(master,text="click and drag the mouse to draw")
message.pack(side=BOTTOM)
mainloop()
