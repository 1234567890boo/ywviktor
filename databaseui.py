import sqlite3

connect=sqlite3.connect('new.db')
cursor=connect.cursor()
student='create TABLE if not exists student'
teacher='create TABlE if not exist teacher'
admin='create TABLE if not exists admin'

print('what do you want to do?')
print('1=make table')
print('2=insert into table')
print('3=delete from table')
print('4=update table entries')
print('5=look at data')

r=int(input())

if r==1:
    print('Choose from following templates')
    print('1=student table')
    print('2=teacher table')
    print('3=admin table')
    
    a=int(input())
    
    print('how namy columns do you want?')
    c=int(input())
    for q in range(0,c,1):
        print('What is the name of column'+str(q+1))
        n=input()
    if a==1:
        student=student+n
        cursor.execute(student)


connect.commit()
connect.close()
