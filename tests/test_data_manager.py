import unittest
from Persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def test_data_manager(self):
        data_manager = DataManager()
        self.assertIsInstance(data_manager, DataManager)

if __name__ == "__main__":
    unittest.main()
