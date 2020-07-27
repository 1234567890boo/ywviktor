import tkinter
from tkinter import messagebox
window=tkinter.Tk()
window.title('Button')
select1=tkinter.IntVar()
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


def select():
    if select1.get()==1:
        prime()
    if select1.get()==2:
        even()
    if select1.get()==3:
        factorial()



b=tkinter.Radiobutton(window,text='Find prime',value=1,variable=select1)
b2=tkinter.Radiobutton(window,text='Find Even',value=2,variable=select1)
b3=tkinter.Radiobutton(window,text='Find Factorial',value=3,variable=select1)

a=tkinter.Entry(window)
b4=tkinter.Button(window,text='Do the Calculate!!:D',command=select)
l=tkinter.Label(window,text='Question 1')

a.pack()
b.pack()
b2.pack()
b3.pack()
b4.pack()
l.pack()
window.mainloop()