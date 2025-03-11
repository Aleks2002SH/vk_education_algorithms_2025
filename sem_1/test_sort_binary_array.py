import pytest
from sort_binary_array import Solution  
@pytest.mark.parametrize(
    "arr, expected", [
        ([0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1]),
        ([1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([1, 0], [0, 1]),
        ([0, 1], [0, 1]),
        ([1, 0, 1, 0, 1], [0, 0, 1, 1, 1]),
        ([0], [0]),
        ([1], [1]),
        ([1, 1, 0, 0], [0, 0, 1, 1]),
        ([0, 1, 0, 1, 1], [0, 0, 1, 1, 1]),
        ([0, 1, 1, 0], [0, 0, 1, 1]),
        ([1, 0, 0, 1], [0, 0, 1, 1]),
        ([1, 0, 1], [0, 1, 1]),
        ([0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1]),
        ([0, 1, 1, 0, 1], [0, 0, 1, 1, 1]),
        ([0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1]),
    ]
)
def test_sort_binary_array(arr, expected):
    solution = Solution()
    result = solution.sort_binary_array(arr)
    assert result == expected
