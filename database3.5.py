import sqlite3
conn=sqlite3.connect('database101.db')
c=conn.cursor()
c.execute('SELECT COUNT(studentId) FROM Classes GROUP BY StudentId HAVING StudentId >10 ORDER BY StudentId')
#Inner Join:SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name=table2.column;
#Left Join:SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name=table2.column;
#Self Join:SELECT column_name(s) FROM table1 T1, table2 T2 WHERE condition;
#Union SQL:SELECT column_name(s) FROM table1 UNION SELECT column_name(s) table2;
#Group Statement:SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) ORDER BY column_name(s);
#Having Statement:SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) HAVING condition ORDER BY column_name(s);

conn.commit()
for record in c.fetchall():
    print(record)
c.close()
