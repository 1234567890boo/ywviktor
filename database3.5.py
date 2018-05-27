import sqlite3
conn=sqlite3.connect('database101.db')
c=conn.cursor()
c.execute('SELECT COUNT(StudentID),Country FROM students GROUP BY Country ORDER BY Country;')
c.execute('SELECT COUNT(StudentID),Country FROM students GROUP BY Country ORDER BY StudentID;')


conn.commit()
for record in c.fetchall():
    print(record)
c.close()
