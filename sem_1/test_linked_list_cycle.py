import pytest
from linked_list_cycle import ListNode, Solution

@pytest.mark.parametrize(
    "nodes, pos, expected", [
        ([1, 2, 3, 4, 5], 0, True),
        ([1, 2, 3, 4, 5], 2, True),
        ([1, 2, 3, 4, 5], -1, False),
        ([10], -1, False),
        ([10], 0, True),
        ([3, 5, 7], 1, True),
        ([1, 2, 3, 4, 5, 6, 7], -1, False),
        ([1, 2, 3, 4], 3, True),
        ([9, 8, 7, 6, 5, 4], 2, True),
        ([1, 2], 1, True),
        ([1, 2, 3, 4, 5], 4, True),
        ([3, 2], -1, False),
        ([10, 20, 30, 40, 50], -1, False),
        ([1, 2, 3, 4, 5, 6], 5, True),
        ([1, 2, 3], -1, False),
    ]
)
def test_has_cycle(nodes, pos, expected):
    solution = Solution()
    head = ListNode(nodes[0])
    current = head
    cycle_node = None

    for i, val in enumerate(nodes[1:], start=1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    if pos == 0:
        current.next = current
    assert solution.hasCycle(head) == expected


