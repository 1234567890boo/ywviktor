import tkinter
from tkinter import messagebox
window=tkinter.Tk()
window.title('Button')
var=0
select1=tkinter.IntVar()
def even():
    a1=a.get()
    if int(a1)%2==0:
        l['text']=a1+' is even'
    else:
        l['text']=a1+' is not even'
        
def even1():
    if select1.get()==1:
        var=1
        
def prime():
    a1=a.get()
    p=int(int(a1)**0.5)
    if a1=='2' or a1=='3':
        l['text']=a1+' is prime'
    elif a1=='1' or a1=='0':
        messagebox.showwarning('Warning',a1+' is not prime')
    for n in range(2,p+1,1):
        if  int(a1)%n==0:
            messagebox.showwarning('Warning',a1+' is not prime')
            break
        else:
            l['text']=a1+' is prime'
            
def prime1():
    if select1.get()==2:
        var=2
        
def select():
    if var==1:
        prime()
    if var==2:
        even()



b=tkinter.Radiobutton(window,text='Find prime',value=1,command=prime1,variable=select1)
b2=tkinter.Radiobutton(window,text='Find Even',value=2,command=even1,variable=select1)

a=tkinter.Entry(window)
b3=tkinter.Button(window,text='Do the Calculate!!:D',command=select)
l=tkinter.Label(window,text='')

a.pack()
b.pack()
b2.pack()
b3.pack()
l.pack()

