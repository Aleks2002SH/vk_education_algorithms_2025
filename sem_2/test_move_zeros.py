import pytest
from move_zeros import Solution

@pytest.mark.parametrize(
    "nums, expected", [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1, 2, 3], [1, 2, 3, 0, 0]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        ([1, 0, 2, 0, 3, 0, 4], [1, 2, 3, 4, 0, 0, 0]),
        ([4, 5, 0, 6, 0, 7], [4, 5, 6, 7, 0, 0]),
        ([1, 2, 3, 0, 0, 4, 5], [1, 2, 3, 4, 5, 0, 0]),
        ([0, 1], [1, 0]),
        ([1, 0], [1, 0]),
        ([0], [0]),
        ([1], [1]),
        ([2, 1, 0, 0, 0, 3], [2, 1, 3, 0, 0, 0]),
        ([1, 2, 0, 3, 0, 4, 0, 5], [1, 2, 3, 4, 5, 0, 0, 0]),
        ([3, 0, 2, 0, 1, 0], [3, 2, 1, 0, 0, 0]),
        ([0, 0, 1, 0, 2, 3], [1, 2, 3, 0, 0, 0]),
        ([5, 0, 6, 7, 0, 8, 9, 0], [5, 6, 7, 8, 9, 0, 0, 0]),
        ([10, 0, 20, 30, 0, 40, 50], [10, 20, 30, 40, 50, 0, 0]),
        ([0, 2, 3, 4, 5, 0, 6], [2, 3, 4, 5, 6, 0, 0]),
        ([0, 9, 8, 7, 6, 0, 0], [9, 8, 7, 6, 0, 0, 0]),
        ([1, 0, 0, 2, 3, 4, 0], [1, 2, 3, 4, 0, 0, 0])
    ]
)
def test_move_zeroes(nums, expected):
    solution = Solution()
    solution.move_zeroes(nums)
    assert nums == expected
