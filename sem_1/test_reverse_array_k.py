import unittest
from reverse_array_k import rotate

class TestRotateArray(unittest.TestCase):
  

    def rotate_and_check(self, nums, k, expected):
        rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_no_rotation(self):
        cases = [
            ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
            ([1, 2, 3], 3, [1, 2, 3]),
            ([5, 4, 3, 2, 1], 5, [5, 4, 3, 2, 1]),
            ([1, 1, 1, 1], 2, [1, 1, 1, 1]),
        ]
        for nums, k, expected in cases:       
            self.rotate_and_check(nums, k, expected)

    def test_small_rotations(self):
        cases = [
            ([1], 10, [1]),
            ([1, 2], 1, [2, 1]),
            ([1, 2, 3], 3, [1, 2, 3]),
            ([1, 2, 3], 4, [3, 1, 2]),
        ]
        for nums, k, expected in cases:  
            self.rotate_and_check(nums, k, expected)

    def test_rotations(self):
        cases = [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
            ([10, 20, 30], 2, [20, 30, 10]),
        ]
        for nums, k, expected in cases:
            self.rotate_and_check(nums, k, expected)

    def test_large_rotations(self):
        cases = [
            ([1, 2, 3, 4, 5], 6, [5, 1, 2, 3, 4]),
            ([100, 200, 300, 400], 1, [400, 100, 200, 300]),
            ([1, 3, 5, 7, 9], 2, [7, 9, 1, 3, 5]),
            ([2, 4, 6, 8, 10], 3, [6, 8, 10, 2, 4]),
        ]
        for nums, k, expected in cases:
            self.rotate_and_check(nums, k, expected)


if __name__ == '__main__':
    unittest.main()