import unittest
from one import max_num
class TestMathFunctions(unittest.TestCase):
    def test_max_num(self):
        self.assertEqual(max_num(2, 3), 3)
        self.assertEqual(max_num(-1, 1), 1)

if __name__ == '__main__':
    unittest.main()