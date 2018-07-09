import sqlite3

conn = sqlite3.connect('test_again.db')
print ("Opened database successfully")


print("This is CROSS JOIN")
cursor_cross = conn.execute("SELECT EMP_ID, NAME, DEPT FROM COMPANY CROSS JOIN DEPARTMENT")
for row in cursor_cross:
   print ("EMP_ID = ", row[0])
   print ("NAME = ", row[1])
   print ("DEPT = ", row[2], "\n")

print("This is INNER JOIN")
cursor_innerjoin = conn.execute("SELECT EMP_ID, NAME, DEPT FROM COMPANY JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.ID") 
for row in cursor_innerjoin:
   print ("EMP_ID = ", row[0])
   print ("NAME = ", row[1])
   print ("DEPT = ", row[2], "\n")



print("This is OUTER JOIN")
cursor_outerjoin = conn.execute("SELECT EMP_ID, NAME, DEPT FROM DEPARTMENT LEFT OUTER JOIN COMPANY \
   ON COMPANY.ID = DEPARTMENT.EMP_ID");

for row in cursor_outerjoin:
   print ("EMP_ID = ", row[0])
   print ("NAME = ", row[1])
   print ("DEPT = ", row[2], "\n")

conn.commit()
conn.close()