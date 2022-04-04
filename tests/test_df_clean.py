import unittest
from helpers import cleaning
import pandas as pd
from pandas._testing import assert_frame_equal

test_dirty_df= pd.DataFrame(
    [
        {
            "UnitPrice": "4,75",
            "TotalPrice": "8,965",
            "ClientName": "jo eY",
            "DeliveryAddress": "7 fajaloompa dingDong",
            "DeliveryCity": "Ham SANDWICH",
            "DeliveryCountry": "UNITED KINGDOM",
            "DeliveryContactNumber": "0 7 7 654 567 45",
            "DeliveryPostcode": "BN3 fj2",
        }      
    ]
)


class TestCleaningFunction(unittest.TestCase):
    def test_clean_df(self):

        func_output = cleaning.clean_df(test_dirty_df)

        expected_output = pd.DataFrame(
            [
                {
                    "UnitPrice": 475,
                    "TotalPrice": 8965,
                    "ClientName": "joey",
                    "DeliveryAddress": "7 fajaloompa dingdong",
                    "DeliveryCity": "ham sandwich",
                    "DeliveryCountry": "united kingdom",
                    "DeliveryContactNumber": "07765456745",
                    "DeliveryPostcode": "bn3fj2",
                }
            ]
        )

        assert_frame_equal(left=func_output, right=expected_output, check_dtype=False)

