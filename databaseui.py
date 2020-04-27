import sqlite3

connect=sqlite3.connect('new.db')
cursor=connect.cursor()

print('what do you want to do?')
print('1=make table')
print('2=insert into table')
print('3=delete from table')
print('4=update table entries')
print('5=look at data')

r=int(input())

connect.commit()
connect.close()
