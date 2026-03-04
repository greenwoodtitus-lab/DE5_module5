import unittest
import pandas as pd
from EDA import date_difference

class TestOperations(unittest.TestCase):

    def setUp(self):
        test_data = {
            'start':
            pd.to_datetime(['01/01/2025']),
            'end':
            pd.to_datetime(['05/01/2025'])
        }
    
    def test_date_difference(self):
        test_result = date_difference(self.df, 'start', 'end', 'diff')

