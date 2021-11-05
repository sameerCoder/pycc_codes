# Data base Advaced Python code .

import sqlite3


def create() :

  conn = sqlite3.connect ("lite355.db")

  cur =conn.cursor()
  cur.execute ("CREATE TABLE IF NOT EXISTS store2 (Item Text , Quantity INTEGER, Price REAL)")

  conn.commit ()
  conn.close ()

create()
def insert (Item,Quantity ,Price ):

  conn =sqlite3.connect ("lite33.db")
  cur = conn.cursor()
  cur.execute ("INSERT INTO store2 VALUES(?,?,?)",(Item,Quantity,Price))

  conn.commit()
  conn.close()

insert("Gla",11,23.8)
#insert(33.45,11,"523.8") # Example for database exceptional
insert("Cold ",12,32.3)
insert ("Pip",13,123.2)


def view():

  conn=sqlite3.connect("lite33.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM store2")

  row=cur.fetchall()
  #row=cur.fetchone()
  for r in row:
    print (r)

  conn.close()
  #return row
# It will return rows in List.

def query():

  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  print(" Total Rows :")
  nrows=cur.execute("SELECT count(*) FROM store2")
  values=nrows.fetchone()
  #no=nrows.rowcount()
  #print(no)
  print("values:",values)
  return (values[0])

#print(view())
#print(query())

def delete(Item):
  conn=sqlite3.connect("lite33.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM store2 WHERE Item=?",(Item,))
  conn.commit()
  conn.close()

def update(Quantity,Price,Item):
  conn=sqlite3.connect("lite33.db")
  cur=conn.cursor()
  cur.execute("UPDATE store2 SET Quantity=?,Price=? WHERE Item=?",(Quantity,Price,Item))

  conn.commit()
  conn.close()



print(view())
print(query())
print("Above data before delete operation.")

delete("Glass1")
print("After deleting Glass item.")
print(view())
print(query())
# All Rows having Items = Glass will get delete.

update(20,233.32,"Cold ")
print("Below data after update")
print(view())
print(query())

#print("After Updating Cold drink item.")
#print(view())
#print(query())
'''
'''

#create()
#insert("Glass1",11,23.8)

#insert(33.45,11,523.8) # Example for database exceptional
#insert("Cold ",12,32.3)
#insert ("Pip",13,123.2)
#print(view())


#print(query())

#delete("Pip")
#print(view())

#print(view())
#update(242,243.3,"Cold ")

#print("After Updating Cold drink item.")
#print(view())










  

































