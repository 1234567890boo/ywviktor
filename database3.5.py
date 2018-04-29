import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()
#c.execute('UPDATE Students SET City="Kost" AND country="Armenia" WHERE studentid=1')
#c.execute('SELECT * FROM Students WHERE Country="USA" OR Country="China" ORDER BY gpa AND dateStarted DESC;')
c.execute('DELETE  FROM Students WHERE Studentname="Tanya Anand"')
conn.commit()
c.execute('SELECT * FROM Students')
for record in c.fetchall():
    print(record)

c.close()
