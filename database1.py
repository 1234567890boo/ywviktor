import sqlite3

connect=sqlite3.connect('new.db')
cursor=connect.cursor()

maketable='create TABLE if not exists phone(name STRING,phone INTEGER)'
insert='insert INTO phone VALUES("{}", {})'.format("Viktor",6692598280)
delete='delete FROM phone WHERE name="{}"'.format("Bob")
update='update phone set phone={} WHERE name="{}"'.format(1111111111,"Bob")
select='select * FROM phone'

cursor.execute(insert)
cursor.execute(select)

for n in cursor:
	print(n)

connect.commit()
connect.close()
