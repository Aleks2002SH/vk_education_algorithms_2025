from merge_ksortedarrays import mergeKSortedArrays

import unittest
from build_tree import *

class TestMergeKSortedArrays(unittest.TestCase):

    def test_case_1(self):
        sortedArrays = [
            [1, 5, 9],
            [2, 6, 10],
            [3, 7, 11]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [1, 2, 3, 5, 6, 7, 9, 10, 11])

    def test_case_2(self):
        sortedArrays = [
            [1, 3, 5],
            [2, 4, 6],
            [7, 8, 9]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_case_3(self):
        sortedArrays = [
            [10, 20, 30],
            [5, 15, 25],
            [12, 18, 24]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [5, 10, 12, 15, 18, 20, 24, 25, 30])

    def test_case_4(self):
        sortedArrays = [
            [1, 4, 5],
            [2, 3, 7],
            [6, 8]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_case_5(self):
        sortedArrays = [
            [1, 3, 5],
            [],
            [2, 4, 6]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_case_6(self):
        sortedArrays = [
            [1],
            [2],
            [3]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [1, 2, 3])

    def test_case_7(self):
        sortedArrays = [
            [],
            [],
            []
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [])

    def test_case_8(self):
        sortedArrays = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_case_9(self):
        sortedArrays = [
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_case_10(self):
        sortedArrays = [
            [10, 20, 30],
            [5, 15, 25],
            [12, 18, 24],
            [0, 7, 14]
        ]
        result = mergeKSortedArrays(sortedArrays)
        self.assertEqual(result, [0, 5, 7, 10, 12, 14, 15, 18, 20, 24, 25, 30])

if __name__ == "__main__":
    unittest.main()
