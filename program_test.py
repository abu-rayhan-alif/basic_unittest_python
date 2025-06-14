import unittest
def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

class TestNotEqual(unittest.TestCase):
    def test_not_equal(self):
        self.assertNotEqual(2 + 2, 5)

a = b = [1, 2]
c = [1, 2]

class TestIs(unittest.TestCase):
    def test_is(self):
        self.assertIs(a, b)      # True, same object
        self.assertIsNot(a, c)   # False, different objects


def get_none():
    return None

class TestIsNone(unittest.TestCase):
    def test_is_none(self):
        self.assertIsNone(get_none())


def get_value():
    return 5

class TestIsNotNone(unittest.TestCase):
    def test_is_not_none(self):
        self.assertIsNotNone(get_value())

class TestIn(unittest.TestCase):
    def test_in(self):
        self.assertIn('a', 'cat')
        self.assertIn(3, [1, 2, 3])

class TestNotIn(unittest.TestCase):
    def test_not_in(self):
        self.assertNotIn('z', 'cat')
        self.assertNotIn(5, [1, 2, 3])


class TestIsInstance(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(5, int)
        self.assertIsInstance("hello", str)


class TestNotIsInstance(unittest.TestCase):
    def test_not_is_instance(self):
        self.assertNotIsInstance(5, str)
        self.assertNotIsInstance("hello", int)
