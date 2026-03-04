import unittest
import pandas as pd
from EDA import date_difference

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.test_df = pd.DataFrame(
        {
            'start':
            pd.to_datetime(['01/01/2025', '05/01/2025', '01/01/2025'], dayfirst=True),
            'end':
            pd.to_datetime(['05/01/2025', '01/01/2025', '01/01/2025'], dayfirst=True)
        })
    
    def test_date_difference(self):
        test_df = date_difference(self.test_df, 'start', 'end', 'diff')
        test_diffs = test_df['diff'].tolist()
        correct_diff = [4,-4,0]
        self.assertEqual(test_diffs, correct_diff, "wrong")

if __name__ == '__main__':
    unittest.main()