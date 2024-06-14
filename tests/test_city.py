import unittest
from Models.city import City

class TestCity(unittest.TestCase):
    def test_city(self):
        self.assertIsInstance(City(), City)

if __name__ == "__main__":
    unittest.main()
