import tkinter
window=tkinter.Tk()
window.title('The Quiz Of The Wrong')
f1=tkinter.Frame(window)
f2=tkinter.Frame(window)
f3=tkinter.Frame(window)
f5=tkinter.Frame(window)
f6=tkinter.Frame(window)
f7=tkinter.Frame(window)
f8=tkinter.Frame(window)

points=0

def yes():
    f1.grid_forget()
    f2.grid()
    global points
    points=1

def no():
    f1.grid_forget()
    f3.grid()

def two():
    f2.grid_forget()
    f5.grid()

def eleven():
    f2.grid_forget()
    f5.grid()
    global points
    points+=1

def nineteen():
    f5.grid_forget()
    f6.grid()

def twentyone():
    f5.grid_forget()
    f6.grid()
    global points
    points+=1

def dumb():
    f6.grid_forget()
    f7.grid()
    global points
    points+=1

def nice():
    f6.grid_forget()
    f7.grid()

def baygull():
    f7.grid_forget()
    f8.grid()
    global points
    points+=1
    l9['text']='you had '+str(points)+' points'

def muffin():
    f7.grid_forget()
    f8.grid()
    l9['text']='you had '+str(points)+' points'

def restart():
    f8.grid_forget()
    f1.grid()

    
#frame 1
l=tkinter.Label(f1,text='Do you want to take a quiz')
b=tkinter.Button(f1,text='Yes',command=yes)
b2=tkinter.Button(f1,text='No',command=no)
l.grid(row=0,column=0,columnspan=2)
b.grid(row=1,column=0)
b2.grid(row=1,column=1)
f1.grid(row=0,column=0)

#frame yes
l2=tkinter.Label(f2,text='what is 1+1')
b3=tkinter.Button(f2,text='2',command=two)
b4=tkinter.Button(f2,text='11',command=eleven)
l2.grid(row=0,column=0,columnspan=2)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)

#frame no
l3=tkinter.Label(f3,text='THEN GO WAY')
b5=tkinter.Button(f3,text='exit',command=exit)
l3.grid(row=0,column=0)
b5.grid(row=1,column=0)

# frame eleven
l5=tkinter.Label(f5,text='what is 9+10?')
b7=tkinter.Button(f5,text='19',command=nineteen)
b8=tkinter.Button(f5,text='21',command=twentyone)
l5.grid(row=0,column=0,columnspan=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)

#frame twentyone
l6=tkinter.Label(f6,text='what is the square of 13?')
b9=tkinter.Button(f6,text='Im to dumb to know',command=dumb)
b10=tkinter.Button(f6,text='169',command=nice)
l6.grid(row=0,column=0,columnspan=2)
b9.grid(row=1,column=0)
b10.grid(row=1,column=1)

#frame dumb
l7=tkinter.Label(f7,text='why dont seagulls fly over the bay')
b11=tkinter.Button(f7,text='becuse baygulls',command=baygull)
b12=tkinter.Button(f7,text='because muffin',command=muffin)
l7.grid(row=0,column=0,columnspan=2)
b12.grid(row=1,column=1)
b11.grid(row=1,column=0)

#frame Baygull
l8=tkinter.Label(f8,text='YAY, YOU WON!! YOU WON BRAGGING WRIGHTS!!')
l9=tkinter.Label(f8,text='you had '+str(points)+' points')
b13=tkinter.Button(f8,text='Do You Want To Restart?',command=restart)
l8.grid(row=0,column=0)
l9.grid(row=1,column=0)
b13.grid(row=2,column=0)
