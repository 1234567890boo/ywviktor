import sqlite3
conn=sqlite3.connect('database101.db')
c=conn.cursor()
c.execute('SELECT * FROM Teachers WHERE teacherid=2')
conn.commit()
for record in c.fetchall():
    print(record)
c.close()
