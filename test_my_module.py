import unittest
from my_module import add_numbers

class TestMyModule(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5, "Expected result of adding 2 and 3 is 5")

    def test_add_numbers_negative(self):
        result = add_numbers(-2, 3)
        self.assertEqual(result, 1, "Expected result of adding -2 and 3 is 1")

if __name__ == '__main__':
    unittest.main()
