import tkinter
window=tkinter.Tk()
window.title('Game Start')

def left():
    pass
def right():
    pass

l=tkinter.Label(window,text='')
b=tkinter.Button(window,text='sefer3qr4wtetgd',command=left)
b2=tkinter.Button(window,text='efdffsfsfs',command=right)


l.grid(row=0,column=0,columnspan=1)
b.grid(row=1,column=0)
b2.grid(row=1,column=1)
