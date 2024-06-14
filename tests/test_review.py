import unittest
from Models.review import Review

class TestReview(unittest.TestCase):
    def test_review(self):
        review = Review(place_id="place1", user_id="user1", text="Test Review", comment="Test Comment")
        self.assertEqual(review.comment, "Test Comment")

if __name__ == '__main__':
    unittest.main()
