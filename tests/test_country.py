import unittest
from Models.country import Country

class TestCountry(unittest.TestCase):
    def test_country(self):
        country = Country(name="Test Country")
        self.assertIsInstance(country, Country)

if __name__ == "__main__":
    unittest.main()
