import sqlite3
conn=sqlite3.connect('sample4.db')
c=conn.cursor()
SELECT COUNT(studentid) FROM STUDENTS
conn.commit()
c.close()

