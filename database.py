import sqlite3
conn=sqlite3.connect('sample3.db')
c=conn.cursor()

c.execute('Create table users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)')
name1='Vishal'
phone1='855-987-2342'
email1='vishal@gmail.com'
password1='123'

name2='Richard'
phone2='510-123-3456'
email2='richard@gmail.com'
password2='456'

c.execute('INSERT INTO users(name, phone, email, password)VALUES(?,?,?,?)', (name1,phone1, email1, password1))

c.execute('INSERT INTO users(name, phone, email, password)VALUES(?,?,?,?)', (name2,phone2, email2, password2))

print('users inserted')

c.execute('SELECT name, email, phone FROM users')
rows=c.fetchall()
for r in rows:
     print(r)

     
newphone='431-421-5435'
userid=1
c.execute('UPDATE users SET phone=? WHERE id=?',(newphone,userid))
try:
    conn=sqlite3.connect('example.db')
    c=conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS \
                        users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)')
    conn.commit()
except Exception as e:
    conn.rollback()
    print('rollback')
conn.commit()
c.close()
