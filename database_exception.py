# Advaced Database class.

import random
import datetime , time
import sqlite3

conn=sqlite3.connect("Advanced12.db")
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS TABLENAME(COLUMNNAME1 INTEGER,DATESTAMP TEXT,COLUMNO3 TEXT,VALUE REAL)")

def dynamic_data_entry():
    COLUMNNAME1=time.time()
    print("time.time():",time.time())
#create_table()
#dynamic_data_entry()
#break
#exit()

    DATE=str(datetime.datetime.fromtimestamp(COLUMNNAME1).strftime("%Y-%m-%d %H:%M:%S"))
    COLUMNO3='Python database'
    VALUE=random.randrange(0,10)
    #"INSERT INTO TABLENAME VALUES(1,"jOHN","INDIA")"
    c.execute("INSERT INTO TABLENAME(COLUMNNAME1,DATESTAMP,COLUMNO3,VALUE)VALUES(?,?,?,?)",
              (COLUMNNAME1,DATE,COLUMNO3,VALUE))

    conn.commit()
###############################################################################
    
def read_from_db():
    print("select *from tabename")
    c.execute("SELECT * FROM TABLENAME ")
    #c.execute("SELECT * FROM TABLENAME  WHERE VALUE<2")
    c.execute("SELECT COLUMNNAME1,COLUMNO3 FROM TABLENAME  WHERE VALUE<2")
    dataoneline=c.fetchone()
    print("fetching only dataonline 1 row:",dataoneline)
    #dataall=c.fetchall()
    
    #print("dataoneline :",dataoneline)
    #print("data allL:",dataall)
    print("c.fetchall()")

    for row in c.fetchall():
        print(row)
        #print(row[0])


def del_and_update():
    c.execute('SELECT * FROM TABLENAME3333333')
    [print(row) for row in c.fetchall()]
    print(50 *'*')
    c.execute("UPDATE TABLENAME SET VALUE=88 WHERE VALUE=4")
    # update done at above line.
    conn.commit()
    c.execute("SELECT * FROM TABLENAME")
    print("Length of rows after update :",len(c.fetchall()))

    c.execute("DELETE FROM TABLENAME WHERE VALUE=1")
    conn.commit()
    print(50*'#')
    c.execute("SELECT * FROM TABLENAME")
    print("Length of rows after delete:",len(c.fetchall()))
    [print(row )for row in c.fetchall()]
  
  

print("starting of db operation.")
create_table()
for i in range(3):
    dynamic_data_entry()
    time.sleep(2)


read_from_db()
del_and_update()
read_from_db()
c.close()

print("End line execution")
conn.close()                                                                   
                                                                   
