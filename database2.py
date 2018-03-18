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
root.geometry("300x200")
conn=sqlite3.connect('phone_book.db')
c=conn.cursor()


first_name=StringVar()
last_name=StringVar()
email=StringVar()
phone_number=StringVar()


def insert():
    first_name=f_name.get()
    last_name=l_name.get()
    email=email.get()
    phone_number=phonenumber.get()
    c.execute('insert into phone_book(first_name,last_name,email,phone_number)values(?,?,?,?)',(first_name,lats_name,email,phone_number))

def read_from_db():
    listbox=Listbox(root,width=40)
    listbox.grid(row=7,column=1,stickey=W)
    c.execute('select * from phone_book')
    for row in c.fechall():
        listbox.insert(END,row)

def del_record():
    first=f_name.get()
    e.execute('delete from phone_book where firts_name=?',(first,))
    conn.commit()
    listbox=Listbox(root)
    istbox.grid(row=7,column=2)
    c.execute('select * from phone_book')
    for row in c.fechall():
        listbox.insert(END,row)

def update_record():
    first=first_name.get()
    last=last_name.get()
    email=email.get()
    phone_number.get()
    c.execute('update phone_book set first_name=?,last_name=?,email=?,phone_number=?\ where first_name=?',(first,last,email,phone_number,first,))
    conn.commit()


def clear():
    first_name.delete(0,END)
    last_name.delete(0,END)
    email_address.delete(0,END)
    phone_number.delete(0,END)

#Create f_name_label,l_name_label,email_label, and phonenumber_label
f_name=Label(root,text="First name")
f_name.grid(row=1,column=1)
f_name=Entry(root)
f_name.grid(row=1,column=2)

l_name=Label(root,text="Last name")
l_name.grid(row=2,column=1)
l_name=Entry(root)
l_name.grid(row=2,column=2)

email_name=Label(root,text="Email")
email_name.grid(row=3,column=1)
email_name=Entry(root)
email_name.grid(row=3,column=2)

phone_number_name=Label(root,text="Phone number")
phone_number_name.grid(row=4,column=1)
phone_number_name=Entry(root)
phone_number_name.grid(row=4,column=2)
