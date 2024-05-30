import unittest
from src.addition import add  # Update the import path
import coverage

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

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, delta=0.0001)

    def test_add_string_numbers(self):
        with self.assertRaises(TypeError):
            add("1", "2")

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    
    unittest.main(exit=False)
    
    cov.stop()
    cov.save()
    cov.xml_report(outfile='coverage.xml')
