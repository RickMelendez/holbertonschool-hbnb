import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place(1, "Beach House", "A lovely beach house.", 200.0, "123 Beach Ave", 1, 1)

    def test_get_details(self):
        self.assertEqual(self.place.get_details(), "Beach House: A lovely beach house. at 123 Beach Ave")

    def test_calculate_price(self):
        self.assertEqual(self.place.calculate_price(3), 600.0)

if __name__ == "__main__":
    unittest.main()
