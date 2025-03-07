import pytest
from reverse_linked_list import ListNode, Solution


def create_linked_list(nodes):
    head = ListNode(nodes[0])
    current = head
    for value in nodes[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

@pytest.mark.parametrize(
    "nodes, expected", [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1], [1]),
        ([], []),
        ([10, 20, 30], [30, 20, 10]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([7, 8, 9], [9, 8, 7]),
        ([100, 200, 300, 400], [400, 300, 200, 100]),
        ([1, 1, 1], [1, 1, 1]),
        ([10, 20], [20, 10]),
        ([9, 8, 7, 6], [6, 7, 8, 9]),
    ]
)
def test_reverse_linked_list(nodes, expected):
    if nodes!=[]:
        head = create_linked_list(nodes)
    else:
        head = None
    solution = Solution()
    reversed_head = solution.reverseList(head)
    reversed_values = linked_list_to_list(reversed_head)

    assert reversed_values == expected
