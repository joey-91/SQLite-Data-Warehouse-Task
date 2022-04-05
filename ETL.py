import pandas as pd
import sqlite3
from helpers.cleaning import clean_df
from helpers.scd import new_values


conn = sqlite3.connect('test_database') 
c = conn.cursor()

csv_file = 'data/Data Engineer Task.csv'

try:
    df = pd.read_csv(csv_file)
except:
    print("couldn't read csv")
    df = None
    

if df is not None:

    try:
        df = clean_df(df)
         # inserting df to staging table
        df.to_sql('staging', con=conn, if_exists='replace')
    except:
        print("couldn't upload to staging table")

    try:
        # update product lookup
        product_columns = ['ProductName', 'ProductType', 'UnitPrice']
        product_key = 'ProductName'
        existing_products = pd.read_sql_query("SELECT * FROM product", conn)
        new_products_df = new_values(df, existing_products, product_key, product_columns)
        new_products_df.to_sql('product', con=conn, if_exists='append', index=False)
        print(len(new_products_df), 'new records added to product table')
        # print(pd.read_sql_query("SELECT * FROM product", conn))
    except:
        print("couldn't update product lookup")

    try:
        # update delivery lookup
        delivery_columns = ['ClientName', 'DeliveryAddress', 'DeliveryCity', 'DeliveryPostcode', 'DeliveryCountry', 'DeliveryContactNumber']
        delivery_key = 'DeliveryAddress'
        existing_delivery = pd.read_sql_query("SELECT * FROM delivery", conn)
        new_delivery_df = new_values(df, existing_delivery, delivery_key, delivery_columns)
        new_delivery_df.to_sql('delivery', con=conn, if_exists='append', index=False)
        print(len(new_delivery_df), 'new records added to delivery table')
        # print(pd.read_sql_query("SELECT * FROM delivery", conn))
    except:
        print("couldn't update delivery lookup")

    try:
        # converting to form ready for fact table
        fact_formatted = pd.read_sql_query(
            """
            SELECT 
            OrderNumber,
            DeliveryId,
            ProductId,
            ProductQuantity,
            TotalPrice,
            Currency,
            PaymentType,
            PaymentBillingCode,
            PaymentDate

            FROM staging

            LEFT JOIN delivery
            ON staging.DeliveryPostcode = delivery.DeliveryPostcode

            LEFT JOIN product
            ON staging.ProductName = product.ProductName

            """, 
            conn
        )
    except:
        print("couldn't read from one of the tables")


    assert len(fact_formatted) == len(df), 'a one-to-many join has occured'
    assert fact_formatted['DeliveryId'].isnull().sum() == 0, "the delivery lookup hasn't updated correctly"
    assert fact_formatted['ProductId'].isnull().sum() == 0, "the product lookup hasn't updated correctly"
    assert fact_formatted['OrderNumber'].isnull().sum() == 0, "data contains null-value product IDs"

    try:
        # update fact table
        fact_key = 'OrderNumber'
        fact_table = pd.read_sql_query("SELECT * FROM fact", conn)
        new_orders_df = new_values(fact_formatted, fact_table, fact_key, fact_formatted.columns)
        new_orders_df.to_sql('fact', con=conn, if_exists='append', index=False)
        print(len(new_orders_df), 'new records added to fact table')
        # print(pd.read_sql_query("SELECT * FROM fact", conn))
    except:
        print("couldn't upload to fact table")