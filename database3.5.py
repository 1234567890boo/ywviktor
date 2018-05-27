import sqlite3
conn=sqlite3.connect('database101.db')
c=conn.cursor()
c.execute('SELECT * FROM Students WHERE StudentName LIKE "";')
conn.commit()
for record in c.fetchall():
    print(record)
c.close()
