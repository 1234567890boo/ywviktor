import sqlite3

connect=sqlite3.connect('new.db')
cursor=connect.cursor()
table='create TABLE if not exists '

def maketable():
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
def insertinto():
    print('what table would you like to insert into?')
    i=input()
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' ".format(i))
    if cursor.fetchone()[0]==0:
        print('Table Does not exist. Please make one.')
    else:
        insert=('INSERT into {} VALUES('.format(i))
        cursor.execute('SELECT * FROM {}'.format(i))
        for c in cursor.description:
            print('What do you want to insert into {}?'.format(c[0]))
            q=input()
            if c[0]!='id':
                insert=insert+"'"+q+"'"+", "
            else:
                insert=insert+q+', '
        insert=insert.strip(', ')
        insert=insert+')'
        print(insert)
        cursor.execute(insert)
        
def read_data():
    n=1
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    fetch=cursor.fetchall()
    print('what table do you want to see?')
    for t in fetch:
                   print(n,'=',t[0])
                   n+=1
    i=int(input())
    if i<len(fetch):
        cursor.execute("SELECT * FROM {}".format(fetch[i-1][0]))
        f=cursor.fetchall()
        for c in cursor.description:
            print(c[0],end=' ')
        print('')
        for s in range(0,len(f),1):
            print(f[s])

print('what do you want to do?')
print('1=make table')
print('2=insert into table')
print('3=delete from table')
print('4=update table entries')
print('5=look at data')

r=int(input())

if r==3:
    n=1
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    fetchtable=cursor.fetchall()
    print('what table do you want to delete from?')
    for t in fetchtable:
                   print(n,'=',t[0])
                   n+=1
    i=int(input())
    if i<len(fetchtable):
        f=1
        cursor.execute("SELECT * FROM {}".format(fetchtable[i-1][0]))
        fetchvalue=cursor.fetchall()
        print('what do you want to delete?')
        for s in fetchvalue:
            print(f,'=',s)
            f+=1
        p=int(input())
        if p>f:
            print('That is not in the table. Plese try again.')
        else:
            print('DELETE FROM {} WHERE id in (SELECT id FROM {} LIMIT 1 OFFSET 1)'.format(fetchtable[i-1][0],fetchtable[i-1][0]))
connect.commit()
connect.close()

#HOMEWORK: move code into functions
