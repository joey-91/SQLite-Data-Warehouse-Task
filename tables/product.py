import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
            DROP TABLE IF EXISTS product
            
          ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS product(
                ProductId INTEGER PRIMARY KEY AUTOINCREMENT,
                ProductName NVARCHAR (30) NOT NULL,
                ProductType NVARCHAR (30) NOT NULL,
                UnitPrice INTEGER NOT NULL)
          ''')
                     
conn.commit()

print('created product table')