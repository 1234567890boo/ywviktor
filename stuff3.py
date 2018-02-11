from tkinter import*
master=Tk()
master.title("guessing game")
import time
import random
'''l1=Label(master,text="First Name").grid(row=0)#label
b1=Button(master,text="click to close",command=master.quit).grid(row=1,column=0)#button
e1=Entry(master)#entry
e1.grid(row=0,column=1)#entry'''
num=random.randint(0,100)
num2=StringVar()
def button_command():
    c=e1.get()
    c=int(c)
    if c==num:
        num2.set('You guessed the correct number!')
    elif c>num:
        num2.set("You guessed a number that is to high!")
    elif c<num:
        num2.set("Your guess is to low!")
e1=Entry(master)
e1.grid(row=0,column=0)
b1=Button(master,text="Guess!!",command=button_command).grid(row=0,column=1)
l1=Label(master,text="pick a number between 1 and 100|").grid(row=1,column=0)
l2=Label(master,textvariable=num2).grid(row=1,column=1)



