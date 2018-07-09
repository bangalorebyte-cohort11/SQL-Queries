#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test_again.db')
print ("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 35000.00 where AGE >= 25")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)



#cursor = conn.execute("SELECT id, name, address, salary from COMPANY WHERE SALARY >= 10000 AND AGE >=25")
#cursor = conn.execute("SELECT id, name, address, salary from COMPANY WHERE SALARY >= 10000 OR AGE >=25")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY WHERE SALARY >= 10000")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

# all the records where AGE starts with '2',
# does not matter what comes after '2'


cursor = conn.execute("SELECT * FROM COMPANY WHERE AGE LIKE '2%'")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

cursor = conn.execute("SELECT * FROM COMPANY WHERE AGE >= 25 AND SALARY >= 65000")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

cursor = conn.execute('SELECT * FROM COMPANY WHERE AGE IN ( 25, 27 )')
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()