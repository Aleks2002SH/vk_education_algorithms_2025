import unittest
from reverse_array import reverse


class TestReverseArray(unittest.TestCase):
    
    def reverse_check(self, arr, expected):
        reverse(arr)
        self.assertEqual(arr, expected)

    def test_no_change(self):
        cases = [
            ([1], [1]),
            ([], []),
            ([1, 1, 1], [1, 1, 1]),
            ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),
        ]
        for arr, expected in cases:
            self.reverse_check(arr, expected)

    def test_basic(self):
        cases = [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([10, 20, 30], [30, 20, 10]),
            ([7, 8, 9], [9, 8, 7]),
            ([100, 200, 300, 400], [400, 300, 200, 100]),
            ([10, 20], [20, 10]),
            ([9, 8, 7, 6], [6, 7, 8, 9]),
        ]
        for arr, expected in cases:
            self.reverse_check(arr, expected)

    def test_large_reversals(self):
        cases = [
            ([1000, 2000, 3000, 4000, 5000], [5000, 4000, 3000, 2000, 1000]),
            ([11, 22, 33, 44, 55, 66], [66, 55, 44, 33, 22, 11]),
            ([10, 15, 20, 25, 30], [30, 25, 20, 15, 10]),
            ([100, 200, 300], [300, 200, 100]),
        ]
        for arr, expected in cases:
            self.reverse_check(arr, expected)

    
if __name__ == '__main__':
    unittest.main()