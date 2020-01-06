import tkinter
window=tkinter.Tk()
window.title('Game Start')
f1=tkinter.Frame(window)

def left():
    pass
def right():
    pass

l=tkinter.Label(f1,text='Do you want to take a quiz')
b=tkinter.Button(f1,text='Yes',command=left)
b2=tkinter.Button(f1,text='No',command=right)


l.grid(row=0,column=0,columnspan=2)
b.grid(row=1,column=0)
b2.grid(row=1,column=1)
f1.grid(row=0,column=0)
#homework:make at least 3 more frames and find/make factorial
