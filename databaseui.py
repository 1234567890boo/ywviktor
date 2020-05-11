import sqlite3

connect=sqlite3.connect('new.db')
cursor=connect.cursor()
table='create TABLE if not exists '

print('what do you want to do?')
print('1=make table')
print('2=insert into table')
print('3=delete from table')
print('4=update table entries')
print('5=look at data')

r=int(input())

if r==1:
    pk=False
    print('what is the table name?')
    
    a=input()
    table=table+a+'('

    print('how many columns do you want?')
    c=int(input())
    for q in range(0,c,1):
        print('What is the name of column'+str(q+1))
        n=input()
        print('What is the type of column?')
        t=input()

        if pk!=True:
            print('Do you want to make this column a primary key?(y/n)')
            p=input()
            if p=='y':
                pk=True
                table=table+n+' '+t+' PRIMARY KEY,'
            else:
                table=table+n+' '+t+','
        else:
            table=table+n+' '+t+','
    table=table.strip(',')
    table=table+')'
    print('Table Created')
    cursor.execute(table)
if r==2:
    print('what table would you like to insert into?')
    i=input()
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(i))
    if cursor.fetchone()[0]==1:
        print('Table exists.')
    else:
        print('Table Does not exist. Please make one.')
connect.commit()
connect.close()

#HOMEWORK: find what the columns are and ask for data. once done, use inser query
