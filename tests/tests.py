import unittest
from src.ans import generate_squares


class TestGenerateSquares(unittest.TestCase):
    def test_generate_squares(self):
        self.assertEqual(generate_squares(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    def test_generate_squares_empty(self):
        self.assertEqual(generate_squares(0), {})

    def test_generate_squares_negative(self):
        self.assertEqual(generate_squares(-3), {})


if __name__ == '__main__':
    unittest.main()
