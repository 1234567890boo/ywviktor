'''Database=Set of rows
table=set of rows
record=set of fields(columns)
atribute=type-type of column: NULL,INTEGER,REAL,TEXT,BLOB
key=unique identifier for each record
    Primary-Uniquely idenyifies record in the table
    foreighn key-Uniquley identifies record in a relaxed table(tables are also retations)
schema=Defines the structures of database
join=combines attributes from one or more tables'''

from tkinter import *
import sqlite3
root=Tk()
root.title("simple exersize using pack")
root.geometry("350x300")
conn=sqlite3.connect('phonebook.db')
c=conn.cursor()


first_name=StringVar()
last_name=StringVar()
email=StringVar()
phone_number=StringVar()


def insert():
    first_name=f_name.get()
    last_name=l_name.get()
    email1=email.get()
    phone_number=phonenumber.get()
    c.execute('insert into phone_book(first_name,last_name,email,phone_number)values(?,?,?,?)',(first_name,last_name,email1,phone_number))
    conn.commit()
    print("First,Last,email, and Phone number entered into database")
def read_from_db():
    listbox=Listbox(root,width=40)
    listbox.grid(row=7,column=1,stickey=W)
    c.execute('select * from phone_book')
    for row in c.fechall():
        listbox.insert(END,row)

def del_record():
    first=f_name.get()
    c.execute('delete from phone_book where first_name=?',(first,))
    conn.commit()
    listbox=Listbox(root)
    listbox.grid(row=7,column=2)
    c.execute('select * from phone_book')
    for row in c.fetchall():
        listbox.insert(END,row)
    print('deleted')
def update_record():
    first=first_name.get()
    last=last_name.get()
    email1=email.get()
    phone_number=phonenumber.get()
    c.execute('update phone_book set first_name=?,last_name=?,email=?,phone_number=?, first_name=?',(first,last,email1,phone_number,first,))
    conn.commit()
    listbox=Listbox(root)
    listbox.grid(row=8,column=2)
    c.execute('select * from phone_book')
    for row in c.fetchall():
        listbox.insert(END,row)
    print('updated')


def read_all():
    listbox=Listbox(root)
    listbox.grid(row=8,column=2)
    c.execute('select *from phone_book')
    for row in c.fetchall():
        listbox.insert(END,row)
def clear():
    f_name.delete(0,END)
    l_name.delete(0,END)
    email.delete(0,END)
    phonenumber.delete(0,END)
    print('cleared')

#Create f_name_label,l_name_label,email_label, and phonenumber_label
f_name=Label(root,text="First name")
f_name.grid(row=1,column=1)
f_name=Entry(root)
f_name.grid(row=1,column=2,)

l_name=Label(root,text="Last name")
l_name.grid(row=2,column=1)
l_name=Entry(root)
l_name.grid(row=2,column=2,)

email=Label(root,text="Email")
email.grid(row=3,column=1)
email=Entry(root)
email.grid(row=3,column=2,)

phonenumber=Label(root,text="Phone number")
phonenumber.grid(row=4,column=1)
phonenumber=Entry(root)
phonenumber.grid(row=4,column=2,)

b1=Button(root,text='Clear',command=clear).grid(row=1,column=3)
b1=Button(root,text='Enter',command=insert).grid(row=2,column=3)
b1=Button(root,text='Delete',command=del_record).grid(row=3,column=3)
b1=Button(root,text='Update',command=update_record).grid(row=4,column=3)
b1=Button(root,text='Read all',command=read_all).grid(row=5,column=3)
