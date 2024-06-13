import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_creation(self):
        review = Review(user_id="1", place_id="2", text="Great place!", rating=5)
        self.assertEqual(review.user_id, "1")
        self.assertEqual(review.place_id, "2")
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.rating, 5)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_review_save(self):
        review = Review(user_id="1", place_id="2", text="Great place!", rating=5)
        old_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
