import unittest
from helpers import scd
import pandas as pd
from pandas._testing import assert_frame_equal

product_columns = ['ProductName', 'ProductType', 'UnitPrice']
product_key = 'ProductName'
product_lookup = pd.DataFrame(
    [   
        {
            "ProductName": "hong kong 4000",
            "ProductType": "all in one",
            "UnitPrice": 500000,
            "location": "here"
        },
        {
            "ProductName": "bing bong 5000",
            "ProductType": "all in one",
            "UnitPrice": 1000000,
            "location": "here now"
        }
    ]
)
input_df = pd.DataFrame(
    [
        {
            "ProductName": "bing bong 5000",
            "ProductType": "all in one",
            "UnitPrice": 1000000,
            "location": "here"
        },
        {
            "ProductName": "dong wand 6000",
            "ProductType": "all in one",
            "UnitPrice": 2000000,
            "location": "here now"
        }
    ]
)


class TestUnstageFunction(unittest.TestCase):
    def test_scd(self):

        func_output = scd.new_values(input_df, product_lookup, product_key, product_columns)

        expected_output = pd.DataFrame(
            [
                {
                    "ProductName": "dong wand 6000",
                    "ProductType": "all in one",
                    "UnitPrice": 2000000
                }   
            ]
        )

        assert_frame_equal(
            left=func_output.reset_index(drop=True), 
            right=expected_output.reset_index(drop=True), 
            check_dtype=True, 
            check_index_type=1 
            )

