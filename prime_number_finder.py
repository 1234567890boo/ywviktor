import tkinter
from tkinter import messagebox
def even():
    a1=a.get()
    if int(a1)%2==0:
        l['text']=a1+' is even'
    else:
        l['text']=a1+' is not even'

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

window=tkinter.Tk()
window.title('Prime Number Finder!!!!!!!')
a=tkinter.Entry(window)
b1=tkinter.Button(window,text='Find Prime Number',command=prime)
b2=tkinter.Button(window,text='Find Even Number',command=even)
l=tkinter.Label(window,text='')
a.grid(row=0,column=1)
b1.grid(row=1,column=0)
b2.grid(row=1,column=2)
l.grid(row=1,column=1)
