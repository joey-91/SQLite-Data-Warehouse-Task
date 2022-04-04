import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
            DROP TABLE IF EXISTS delivery
            
          ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS delivery(
                DeliveryId INTEGER PRIMARY KEY AUTOINCREMENT,
                ClientName NVARCHAR (30) NOT NULL,
                DeliveryAddress NVARCHAR (30) NOT NULL,
                DeliveryCity NVARCHAR (30) NOT NULL,
                DeliveryPostcode NVARCHAR (30) NOT NULL,
                DeliveryCountry NVARCHAR (30) NOT NULL,
                DeliveryContactNumber NVARCHAR (30)
                )
          ''')
                     
conn.commit()


print('created delivery table')