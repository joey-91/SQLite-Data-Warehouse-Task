import pandas as pd
import sqlite3
from helpers.cleaning import clean_df
from helpers import unstage


product_columns = ['ProductName', 'ProductType', 'UnitPrice']
product_key = 'ProductName'
product_lookup = pd.DataFrame(
    [   
        {
            "ProductName": "dong wand 4000",
            "ProductType": "all in one",
            "UnitPrice": 500000,
            "location": "here"
        },
        {
            "ProductName": "dong wand 5000",
            "ProductType": "all in one",
            "UnitPrice": 1000000,
            "location": "here"
        }
    ]
)
input_df = pd.DataFrame(
    [
        {
            "ProductName": "dong wand 5000",
            "ProductType": "all in one",
            "UnitPrice": 1000000,
            "location": "here"
        },
        {
            "ProductName": "dong wand 6000",
            "ProductType": "all in one",
            "UnitPrice": 2000000,
            "location": "here"
        }
    ]
)

test = unstage.new_values(input_df, product_lookup, product_key, product_columns)
test2 = pd.DataFrame(
            [
                {
                    "ProductName": "dong wand 6000",
                    "ProductType": "all in one",
                    "UnitPrice": 2000000
                }   
            ]
        ).reset_index()

# print(test == test2)

print(test)
print(test2)