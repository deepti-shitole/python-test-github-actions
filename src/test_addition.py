

# test_addition.py

import unittest
from addition import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -1), 0)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

if __name__ == '__main__':
    unittest.main()
