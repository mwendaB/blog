import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.random_quote = Quote("Brian Mwenda", "The greatest glory in living lies not in never falling, but in rising every time we fall.")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        self.assertEqual(self.random_quote.author, "Brian Mwenda")
        self.assertEqual(self.random_quote.quote,"The greatest glory in living lies not in never falling, but in rising every time we fall.")