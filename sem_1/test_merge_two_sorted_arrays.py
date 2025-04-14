import unittest
from merge_two_sorted_arrays import merge_sorted_arrays 

class TestMergeSortedArrays(unittest.TestCase):

    def check_merge(self, arr1, arr2, expected):
        result =merge_sorted_arrays(arr1, arr2)
        self.assertEqual(result, expected)

    def test_basic(self):
        
        cases = [
            ([1, 2, 3], [], [1, 2, 3]),
            ([], [4, 5, 6], [4, 5, 6]),
            ([1, 2, 3], [3, 4, 5], [1, 2, 3, 3, 4, 5]),
        ]
        for arr1, arr2, expected in cases:
            self.check_merge(arr1, arr2, expected)

    def test_duplicates(self):
        
        cases = [
            ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
            ([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]),
        ]
        for arr1, arr2, expected in cases:
            self.check_merge(arr1, arr2, expected)

    def test_sorted(self):

        cases = [
            ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([10, 20, 30], [5, 15, 25], [5, 10, 15, 20, 25, 30]),
            ([1, 4, 7], [2, 3, 8], [1, 2, 3, 4, 7, 8]),
        ]
        for arr1, arr2, expected in cases:
            self.check_merge(arr1, arr2, expected)

    def test_interleaved(self):
        cases = [
            ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
            ([1, 5, 9], [2, 6, 10], [1, 2, 5, 6, 9, 10]),
            ([3, 6, 9], [1, 4, 7], [1, 3, 4, 6, 7, 9]),
        ]
        for arr1, arr2, expected in cases:
            self.check_merge(arr1, arr2, expected)

if __name__ == '__main__':
    unittest.main()