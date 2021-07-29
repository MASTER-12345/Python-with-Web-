import sqlite3

conn = sqlite3.connect('testB.db')
print ("Opened database successfully");
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID  PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully");
conn.commit()
conn.close()
