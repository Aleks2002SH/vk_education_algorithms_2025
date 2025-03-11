import pytest
from remove_elements_from_linked_list import ListNode, Solution

def create_linked_list(nodes):
    head = ListNode(nodes[0])
    current = head
    for value in nodes[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

@pytest.mark.parametrize(
    "nodes, val, expected", [
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        ([7, 7, 7, 7], 7, []),
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
        ([1, 2, 2, 2, 3], 2, [1, 3]),
        ([10, 20, 30, 40], 25, [10, 20, 30, 40]),
        ([10], 10, []),
        ([1, 1, 1], 1, []),
        ([1, 2, 3], 2, [1, 3]),
        ([5, 4, 3, 2, 1], 2, [5, 4, 3, 1]),
        ([9, 8, 7, 6, 5, 4], 5, [9, 8, 7, 6, 4]),
        ([9, 9, 9, 9], 9, []),
        ([2, 4, 6, 8, 10], 10, [2, 4, 6, 8]),
        ([1, 1, 1, 1, 1], 1, []),
        ([3, 4, 5, 6, 7], 5, [3, 4, 6, 7]),
        ([10, 20, 30, 40, 50], 40, [10, 20, 30, 50])
    ]
)
def test_remove_elements(nodes, val, expected):
    head = create_linked_list(nodes)
    solution = Solution()
    result = solution.removeElements(head, val)
    result_values = []
    while result:
        result_values.append(result.val)
        result = result.next
    assert result_values == expected
