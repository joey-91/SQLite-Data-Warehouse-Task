import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
            DROP TABLE IF EXISTS fact
            
          ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS fact(
                OrderNumber INT NOT NULL,
                DeliveryId INT NOT NULL,
                ProductId INT NOT NULL,
                ProductQuantity INT NOT NULL,
                TotalPrice INT NOT NULL,
                Currency NVARCHAR (30) NOT NULL,
                PaymentType INTEGER NOT NULL,
                PaymentBillingCode INTEGER NOT NULL,
                PaymentDate NVARCHAR (30) NOT NULL
                )
          ''')

                     
conn.commit()

print('created fact table')