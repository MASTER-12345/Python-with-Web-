##插入
import sqlite3

conn = sqlite3.connect('accountStock.db')

c = conn.cursor()

c.execute("INSERT INTO COMPANY (account,money) \
      VALUES ('%s','%d')" % ('888888',1000));
# 记得不可重复插入，因为里面每个值都是独一无二的
print('Table created successfully;')
conn.commit()
conn.close()
##查询
import sqlite3

conn = sqlite3.connect('charaB.db')
c = conn.cursor()
print("Opened database successfully");

cursor = c.execute("SELECT ID,技能,技能描述,ADDRESS,SALARY  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("技能 = ", row[1])
   print("技能描述 = ", row[2])
   print("ADDRESS= ", row[2], "\n")

print("Operation done successfully");
conn.close()
###更新
import sqlite3

conn = sqlite3.connect('test1.db')
c = conn.cursor()
print("Opened database successfully");

c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit()
print("Total number of rows updated :"), conn.total_changes

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully");
conn.close()

######删除
import sqlite3

conn = sqlite3.connect('testg.db')
c = conn.cursor()
print("Opened database successfully");

c.execute("DELETE from COMPANY where ID=1;")
conn.commit()
print ("Total number of rows deleted :"), conn.total_changes

cursor = conn.execute("SELECT id,name , address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully");
conn.close()


