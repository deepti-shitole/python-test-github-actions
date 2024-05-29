# test_addition.py

import unittest
from addition import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -1), 0)

if __name__ == '__main__':
    unittest.main()
