# Data base Sql lite 3

'''
import sqlite3

conn=sqlite3.connect("lite2.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER,price REAL)")
cur.execute ("INSERT INTO store VALUES ('Glass',8,10.5)")

conn.commit()
conn.close()
print("connection Closed .")

'''

import sqlite3

#conn=sqlite3.connect("tut2.db")
conn=sqlite3.connect("tut355.db")# connection to a database
c=conn.cursor() # cursor creation.

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS TableName4(Srno INTEGER, Name TEXT, studentClass TEXT, Address TEXT)")
    # query exection with help of c.execute()

def data_entry():
    c.execute("INSERT INTO TableName4 VALUES(1,'ravi','1','Jntu')")
    c.execute("INSERT INTO TableName4 VALUES(2,'srinivas','1A','Jntu')")
    print("inside data entry function")
    conn.commit()# Storing the data permanently. 
    c.execute("INSERT INTO TableName4 VALUES(3,'mohan','1','kukatpally')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()

        
        






















    
