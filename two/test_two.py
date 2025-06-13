
# test_calculator.py
import unittest
from two import is_adult

class TestCalculator(unittest.TestCase):
    def test_is_adult(self):
        self.assertTrue(is_adult(18))
        self.assertTrue(is_adult(30))
        self.assertFalse(is_adult(10))

if __name__ == '__main__':
    unittest.main()