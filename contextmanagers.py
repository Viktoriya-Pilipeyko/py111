#####################################
#подключение к БД

import sqlite3
from sqlite3 import Error
 
 
class DataConn:
 
    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name
    try:
        def __enter__(self):
            """
            Открываем подключение с базой данных.
            """
            self.conn = sqlite3.connect(self.db_name)
            return self.conn
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        def __exit__(self, exc_type, exc_val, exc_tb):
            """
            Закрываем подключение.
            """
            self.conn.close()
            if exc_val:
                raise
 
with DataConn('example.db') as conn:
    try:
        c = conn.cursor()
        # Insert a row of data
        c.execute("INSERT INTO stocks VALUES ('2009-01-05','BUY','ЗЗГЩ',120,36.15)")
        # Save (commit) the changes
        conn.commit()
        t = ('ЗЗГЩ',)
        c.execute('SELECT * FROM stocks WHERE symbol = ?', t)
        print (c.fetchone())
    except Error as e:
        print(f"The error '{e}' occurred")



######################################
