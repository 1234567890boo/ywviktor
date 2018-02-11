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
w.create_oval(50,50,100,100)



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



w=Canvas(master,width=600,height=300)
w.pack()
img=PhotoImage(file="runcat1.png")
w.create_image(20,20,anchor=NW,image=img)



canvasw=200
canvash=200
python_green="#476042"
w=Canvas(master,width=canvasw,height=canvash)
w.pack()
points=[100,140,110,110,140,100,110,90,100,60,90,90,60,100,90,110]
w.create_polygon(points,outline=python_green,fill='yellow',width=3)



w=Scale(master,from_=0,to_=42)
w.pack()
w=Scale(master,from_=0,to_=200,orient=HORIZONTAL)
w.pack()


root=Tk()
T=Text(root,height=2,width=30)
T.pack()
T.insert(END,"Just a text widget\nin two lines\n")



root=Tk()
S=Scrollbar(root)
T=Text(root,height=4,width=50)
S.pack(side=RIGHT,fill=Y)
T.pack(side=LEFT,fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote="""STUFF:The sky is blue birds are singing. This is a perfect day to DIE!!!!!!HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"""
T.insert(END,quote)'''
mainloop()
