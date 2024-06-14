import unittest
from Models.place import Place

class TestPlace(unittest.TestCase):
    def test_place(self):
        place = Place(address="123 Main St")
        self.assertIsInstance(place, Place)

if __name__ == "__main__":
    unittest.main()
