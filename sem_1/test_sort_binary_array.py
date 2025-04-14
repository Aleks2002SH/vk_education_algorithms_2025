import unittest
from sort_binary_array import sort_binary_array  
class TestSortBinaryArray(unittest.TestCase):


    def sort_check(self, arr, expected):
        result = sort_binary_array(arr)
        self.assertEqual(result, expected)

    def test_simple(self):
        cases = [
            ([0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1]),
            ([1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1]),
            ([1, 0], [0, 1]),
            ([0, 1], [0, 1]),
            ([1, 1, 0, 0], [0, 0, 1, 1]),
            ([0, 1, 0, 1, 1], [0, 0, 1, 1, 1]),
            ([0, 1, 1, 0], [0, 0, 1, 1]),
            ([1, 0, 0, 1], [0, 0, 1, 1]),
            ([1, 0, 1], [0, 1, 1]),
            ([0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1]),
            ([0, 1, 1, 0, 1], [0, 0, 1, 1, 1]),
            ([0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1]),
        ]
        for arr, expected in cases:
            self.sort_check(arr, expected)

    def test_edge(self):
        edge_cases = [
            ([1, 1, 1, 1], [1, 1, 1, 1]),
            ([0, 0, 0, 0], [0, 0, 0, 0]),
            ([0], [0]),
            ([1], [1]),
        ]
        for arr, expected in edge_cases:
            self.sort_check(arr, expected)

if __name__ == '__main__':
    unittest.main()