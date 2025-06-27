import unittest
from unittest.mock import patch
from question1 import calculate_total, book_movie

class TestMovieBooking(unittest.TestCase):

    def setUp(self):
        print("\n[SETUP] Starting test...")

    def tearDown(self):
        print("[TEARDOWN] Test finished.")



    def test_calculate_total(self):
        self.assertEqual(calculate_total(100, 2), 200)


    @patch('builtins.input', side_effect=['1', '2'])  # Choose "Inception", 2 tickets
    def test_book_movie_with_mock(self, mock_inputs):
        book_movie()  

        
if __name__ == '__main__':
    unittest.main()
