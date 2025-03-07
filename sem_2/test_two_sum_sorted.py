import pytest
from two_sum_sorted import Solution  # Assuming your solution class is named Solution

@pytest.mark.parametrize(
    "nums, target, expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([1, 3, 5, 7], 10, [1, 3]),
        ([1, 2, 3, 4, 5, 6], 7, [0, 5]),
        ([1, 5, 3, 4], 8, [1, 2]),
        ([5, 10, 15, 20], 25, [0, 3]),
        ([2, 4, 6, 8, 10], 14, [1, 4]),
        ([1, 2, 3, 4, 5, 6], 10, [3, 5]),
        ([10, 15, 20, 25, 30], 35, [0, 3]),
        ([3, 4, 5, 6, 7, 8], 10, [0, 4]),
        ([1, 3, 5, 7, 9], 16, [3, 4]),
        ([2, 6, 8, 10], 16, [1, 3]),
        ([5, 7, 10, 11, 16], 23, [1, 4]),
        ([1, 4, 5, 6], 10, [1, 3]),
        ([2, 6, 8, 10], 18, [2, 3]),
        ([3, 6, 9, 12, 15], 18, [0, 4]),
        ([2, 5, 8, 12, 14], 20, [2, 3]),
        ([1, 2, 3, 5, 7], 9, [1, 4]),
        ([5, 10, 15, 20], 35, [2, 3]),
    ]
)
def test_two_sum(nums, target, expected):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert result == expected
