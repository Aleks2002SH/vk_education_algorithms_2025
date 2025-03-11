import pytest
from middle_of_the_linked_list import ListNode, Solution

def create_linked_list(nodes):
    head = ListNode(nodes[0])
    current = head
    for value in nodes[1:]:
        node = ListNode(value)
        current.next = node
        current = node
    return head

@pytest.mark.parametrize(
    "nodes, expected_middle_value", [
        ([1, 2, 3, 4, 5, 6, 7], 4),
        ([1, 2, 3, 4, 5, 6], 4),
        ([5, 10, 15, 20, 25, 30, 35], 20),
        ([100, 200, 300, 400, 500], 300),
        ([10, 20, 30, 40, 50], 30),
        ([1, 2], 2),
        ([2, 3, 4, 5, 6, 7], 5),
        ([1, 2, 3, 4], 3),
        ([1, 1, 1, 1, 1], 1),
        ([8, 9, 10, 11, 12, 13, 14, 15], 12),
        ([1000, 2000, 3000, 4000, 5000], 3000),
        ([1, 2, 3], 2),
        ([7, 14, 21, 28, 35, 42], 28),
        ([1, 2, 3, 4, 5, 6, 7, 8], 5),
        ([15, 20, 25, 30], 25),
        ([9, 8, 7, 6, 5], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
        ([1, 2, 3, 4, 5, 6], 4),
        ([10, 20, 30], 20)
    ]
)


def test_middle_node(nodes, expected_middle_value):
    head = create_linked_list(nodes)
    solution = Solution()
    middle = solution.middleNode(head)
    assert middle.val == expected_middle_value