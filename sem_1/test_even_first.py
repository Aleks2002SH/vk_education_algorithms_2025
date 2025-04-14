import unittest
from even_first import even_first

class TestEvenFirst(unittest.TestCase):

    def check(self, arr, expected):
        self.assertEqual(even_first(arr), expected)

    def test_mixed_even_odd(self):
        self.check([1, 2, 3, 4, 5, 6], [2, 4, 6, 1, 5, 3])
        self.check([6, 5, 4, 3, 2, 1], [6, 4, 2, 3, 5, 1])
        self.check([5, 3, 2, 8, 7, 6], [2, 8, 6, 3, 7, 5])
        self.check([10, 9, 8, 7, 6, 5, 4, 3], [10, 8, 6, 4, 9, 5, 7, 3])
        self.check([0, 1, 2, 3, 4, 5], [0, 2, 4, 3, 1, 5])
        self.check([4, 7, 9, 2, 8, 3, 6, 5], [4, 2, 8, 6, 9, 3, 7, 5])
        self.check([13, 15, 17, 19, 20], [20, 15, 17, 19, 13])
        self.check([11, 22, 33, 44, 55, 66], [22, 44, 66, 11, 55, 33])

    def test_all_even(self):
        self.check([2, 4, 6, 8], [2, 4, 6, 8])
        self.check([2, 2, 2, 2], [2, 2, 2, 2])

    def test_all_odd(self):
        self.check([1, 3, 5, 7], [1, 3, 5, 7])
        self.check([1, 1, 1, 1], [1, 1, 1, 1])

    def test_single_element(self):
        self.check([1], [1])
        self.check([2], [2])

    def test_empty_list(self):
        self.check([], [])

    def test_two_elements(self):
        self.check([1, 2], [2, 1])
        self.check([2, 1], [2, 1])

    def test_repeated_pattern(self):
        self.check([1, 2, 1, 2, 1, 2], [2, 2, 2, 1, 1, 1])
        self.check([100, 101, 102, 103], [100, 102, 101, 103])
        self.check([2, 4, 6, 8, 10, 1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 1, 3, 5, 7, 9])

if __name__ == "__main__":
    unittest.main()
