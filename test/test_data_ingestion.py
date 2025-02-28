import unittest
import pandas as pd
from io import StringIO
from src.data_cleaning import load_data, clean_data, save_data

class TestDataIngestion(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_data = StringIO("""date,age,name
2025-02-11,25,John Doe
2025-02-12,30,Jane Doe
,35,Invalid Date
2025-02-14,,Invalid Age
""")
        self.df = pd.read_csv(self.sample_data)

    def test_load_data(self):
        # Test loading data
        df = load_data(self.sample_data)
        self.assertEqual(len(df), 4)
        self.assertEqual(list(df.columns), ['date', 'age', 'name'])

    def test_clean_data(self):
        # Test cleaning data
        cleaned_df = clean_data(self.df)
        self.assertEqual(len(cleaned_df), 2)  # Only valid rows should remain
        self.assertFalse(cleaned_df.isnull().values.any())  # No missing values

    def test_save_data(self):
        # Test saving data
        cleaned_df = clean_data(self.df)
        output = StringIO()
        save_data(cleaned_df, output)
        output.seek(0)
        saved_df = pd.read_csv(output)
        self.assertEqual(len(saved_df), 2)
        self.assertEqual(list(saved_df.columns), ['date', 'age', 'name'])

if __name__ == '__main__':
    unittest.main()