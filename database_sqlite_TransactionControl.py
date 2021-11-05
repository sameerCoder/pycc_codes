# sqlite3
# Transaction Control.

import sqlite3

sql = sqlite3.connect("/tmp/test.db")
sql.isolation_level = None
c = sql.cursor()
c.execute("begin")
try:
    c.execute("update test set i = 1")
    c.execute("fnord")
    c.execute("update test set i = 0")
    c.execute("commit")
except sql.Error:
    print("failed!")
    c.execute("rollback")
