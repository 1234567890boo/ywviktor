import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()


c.execute('CREATE TABLE Students (StudentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,StudentName NVARCHAR(255),ParentName NVARCHAR(255),City  NVARCHAR(255),Country NVARCHAR(255) , GPA FLOAT(4,2), dateStarted DATE)' )
c.execute('CREATE TABLE Teachers (TeacherID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,TeacherName NVARCHAR(255),Phone NVARCHAR(255),city NVARCHAR(255),country NVARCHAR(255) )')
c.execute('CREATE TABLE Classes (ClassID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,ClassName NVARCHAR(255),StudentID INT,TeacherID INT,CreditUnits INT)')

conn.commit()
c.close()
print('These tables have been created successfully')



c.execute('INSERT INTO Students (StudentName,ParentName, City,Country  , GPA, dateStarted) VALUES ("Tanya Anand","Amit Anand","Delhi","India",3.31,"2015-01-12")');
c.execute('INSERT INTO Students (StudentName,ParentName, City,Country  , GPA ,  dateStarted) VALUES ("Ishita Reddy","Aditya Reddy","Bangalore","India",3.12,"2013-10-23")');
c.execute('INSERT INTO Students (StudentName,ParentName, City,Country  , GPA , dateStarted) VALUES ("Ankit Babu","Raj Babu","Banerjee","India",2.73,"2015-04-05")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Suhani Burman","Anusha Burman","Bangalore","India",2.57,"2014-10-22")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Soham Chawla","Pavithra Chawla","Delhi","India",4.00,"2011-07-21")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Suhani Datta","Raghav Datta","Delhi","India",4.20,"2015-03-07")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Anisha Iyer","Kunal Iyer","Bangalore","India",3.74,"2016-04-19")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Angel Puri","Anusha Puri","Bangalore","India",3.52,"2017-08-25")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Niti Pandey","Pavithra Pandey","Delhi","India",4.40,"2012-04-11")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Shreya Singh","Mayank Singh","Mumbai","India",2.71,"2016-02-09")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Rohan Pandey","Parth Pandey","Bangalore","India",2.33,"2017-01-20")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Nikita Singh","Karan Singh","Bangalore","India",2.94,"2015-10-02")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ayushi Pandey","Pavithra Pandey","Delhi","India",2.45,"2012-04-11")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Mary Singh","Rohan Singh","Mumbai","India",2.97,"2017-10-09")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Sam Pandey","Ram Pandey","Bangalore","India",3.61,"2017-04-11")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Nick He","Mike He","Shanghai","China",3.34,"2015-07-11")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Mary Lee","Henry Lee","Seoul","South Korea",3.12,"2013-11-22")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Lily Wang","Mary Wang","Hongzhou","China",3.61,"2015-5-11")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Steve Liu","Sam Liu","Beijing","China",2.34,"2015-11-30")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("James Tang","Kelly Tang","Hong Kong","China",4.12,"2016-08-29")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ricky Ma","Jack Ma","Shanghai","China",3.33,"2015-05-23")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Eric Zhou","Edward Zhou","Shanghai","China",4.21,"2017-05-12")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Jessica Lu","Andy Lu","Beijing","China",3.75,"2017-06-10")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Alice Chen","Jacky Chen","Seoul","South Korea",3.49,"2015-02-25")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ethan Roberson","Sue Roberson","San Jose","USA",3.21,"2017-12-31")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("John Smith","Eve Smith","San Francisco","USA",4.05,"2016-04-15")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Grace Davis","Bill Davis","San Jose","USA",2.71,"2015-06-23")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("William Johnson","Sean Johnson","San Jose","USA",2.39,"2017-06-21")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ken Nelson","Nick Nelson","San Francisco","USA",3.51,"2015-10-04")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Michell Cook","King Cook","San Jose","USA",2.87,"2017-05-19")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Anna Neckson","Amy Neckson","San Jose","USA",2.53,"2014-07-22")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Sophie Brown","Sue Brown","San Francisco","USA",4.32,"2013-09-05")');
c.execute('INSERT INTO Students (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Bob Smith","Susan Smith","San Jose","USA",3.34,"2016-07-05")');


conn.commit()
c.close()

c.execute('select * from students')

for record in c.fetchall():
    print(record)

conn.commit()



c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Scrach", 5,1,1)')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Python set 1", 11,2,2 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Python set 2", 10,1,3 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Python set 3", 9,3,4 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Python set 4", 8,4,5 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Python set 5", 11,2,6 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Python set 6", 12,5,7 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Pygame basic set", 9,7,10 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Pygame tic tac toe", 8,6,11 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Pygame menu", 11,2,12 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Pygame pong game", 10,1,13 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Pygame flappy bird", 12,3,14 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Pygame snake", 14,1,15 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Pygame animation", 15,2,16) ')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("GPIO Robot", 13,1,21) ')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("GPIO PWM mode", 21,3,22 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("GPIO sensor", 22,4,23 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Tkinter basic ", 31,6,40 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Tkinter Advanced", 10,1,41 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Object Oriented Programming", 24,5,30 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("OOP pong game", 26,5,31)')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("OOP aircraft game", 26,5,32)')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Final Tkinter", 30,8,43 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("SQL Tkinter", 29,5,44)')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("HTML", 28,5,50)')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("JavaScript", 24,5,51) ')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("GPIO breadboard", 25,7,21 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("GPIO 7-segment", 28,8, 24)')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("MongoDB", 28,5,52)')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("Flask", 24,5,53 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("GPIO stepper motor", 29,5,54 )')
c.execute('INSERT INTO Classes (ClassName,StudentID,TeacherID,CreditUnits) VALUES ("GPIO camera", 27,5,55) ')

conn.commit()
c.close()


c.execute('select * from classes')
for record in c.fetchall():
    print(record)

conn.commit()
c.close()
