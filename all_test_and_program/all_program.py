
def add(a, b):
    return a + b

def square(x):
    return x * x

def is_even(n):
    return n % 2 == 0

def longer_name(name1, name2):
    return name1 if len(name1) > len(name2) else name2

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def average(nums):
    return sum(nums) / len(nums) if nums else 0

def reverse_string(s):
    return s[::-1]

def is_divisible_by_3_and_5(n):
    return n % 3 == 0 and n % 5 == 0

def max_in_list(lst):
    return max(lst)

def count_capitals(s):
    return sum(1 for char in s if char.isupper())

def lower_names(names):
    return [name.lower() for name in names]

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
