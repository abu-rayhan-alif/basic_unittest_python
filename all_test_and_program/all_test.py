# test_my_functions.py

import unittest
from all_program import (
    add, square, is_even, longer_name, multiply_list,
    is_palindrome, count_vowels, factorial, average,
    reverse_string, is_divisible_by_3_and_5, max_in_list,
    count_capitals, lower_names, is_anagram
)

class TestMyFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_square(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(-4), 16)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_longer_name(self):
        self.assertEqual(longer_name("Alif", "Rayhan"), "Rayhan")
        self.assertEqual(longer_name("Hello", "Hi"), "Hello")

    def test_multiply_list(self):
        self.assertEqual(multiply_list([2, 3, 4]), 24)
        self.assertEqual(multiply_list([1]), 1)
        self.assertEqual(multiply_list([]), 1)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("sky"), 0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_average(self):
        self.assertEqual(average([2, 4, 6]), 4.0)
        self.assertEqual(average([]), 0)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_is_divisible_by_3_and_5(self):
        self.assertTrue(is_divisible_by_3_and_5(15))
        self.assertFalse(is_divisible_by_3_and_5(9))

    def test_max_in_list(self):
        self.assertEqual(max_in_list([4, 9, 1]), 9)

    def test_count_capitals(self):
        self.assertEqual(count_capitals("AbCdeF"), 3)

    def test_lower_names(self):
        self.assertEqual(lower_names(["Alif", "Rayhan"]), ["alif", "rayhan"])

    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("hello", "world"))

if __name__ == '__main__':
    unittest.main()
