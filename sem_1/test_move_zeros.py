import unittest
from move_zeros import move_zeroes

class TestMoveZeroes(unittest.TestCase):

    def check_move_zeroes(self, nums, expected):
        move_zeroes(nums)
        self.assertEqual(nums, expected)

    def test_basic(self):
        cases = [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0, 0, 1, 2, 3], [1, 2, 3, 0, 0]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        ]
        for nums, expected in cases:
            
            self.check_move_zeroes(nums, expected)

    def test_mixed_zeros(self):
        cases = [
            ([1, 0, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0]),
            ([4, 5, 0, 6, 0, 7], [4, 5, 6, 7, 0, 0]),
            ([1, 2, 3, 0, 0, 4, 5], [1, 2, 3, 4, 5, 0, 0]),
            ([2, 1, 0, 0, 0, 3], [2, 1, 3, 0, 0, 0]),
        ]
        for nums, expected in cases:
            
            self.check_move_zeroes(nums, expected)

    def test_edge_cases(self):
        cases = [
            ([0], [0]),
            ([1], [1]),
            ([0, 1], [1, 0]),
            ([1, 0], [1, 0]),
        ]
        for nums, expected in cases:
            self.check_move_zeroes(nums, expected)

        

if __name__ == '__main__':
    unittest.main()