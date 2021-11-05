# sqlite3
# Transaction control with exception.

import sqlite3

filename = '/tmp/test.db'
with sqlite3.connect(filename) as conn:
    cursor = conn.cursor()
    sqls = [
        'DROP TABLE IF EXISTS test',
        'CREATE TABLE test (i integer)',
        'INSERT INTO "test" VALUES(99)',]
    for sql in sqls:
        cursor.execute(sql)
try:
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        sqls = [
            'update test set i = 1',
            'fnord',   # <-- trigger error
            'update test set i = 0',]
        for sql in sqls:
            cursor.execute(sql)
except sqlite3.OperationalError as err:
    print(err)
    # near "fnord": syntax error
with sqlite3.connect(filename) as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    for row in cursor:
        print(row)
        # (99,)
