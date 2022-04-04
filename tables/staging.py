import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
            DROP TABLE IF EXISTS staging
            
          ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS staging(
                OrderNumber NVARCHAR (30) NOT NULL,
                ClientName NVARCHAR (30) NOT NULL,
                ProductName NVARCHAR (30) NOT NULL,
                ProductType  NVARCHAR (30) NOT NULL,
                UnitPrice INT NOT NULL,
                ProductQuantity INT NOT NULL,
                TotalPrice INT NOT NULL,
                Currency NVARCHAR (30) NOT NULL,
                DeliveryAddress NVARCHAR (30) NOT NULL,
                DeliveryCity NVARCHAR (30) NOT NULL,
                DeliveryPostcode NVARCHAR (30) NOT NULL,
                DeliveryCountry NVARCHAR (30) NOT NULL,
                DeliveryContactNumber NVARCHAR (30) NOT NULL,
                PaymentType NVARCHAR (30) NOT NULL,
                PaymentBillingCode NVARCHAR (30) NOT NULL,
                PaymentDate DATE NOT NULL
                )
          ''')

conn.commit()

                