
import pytest

from merge_two_sorted_linked_lists import Solution,ListNode

def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

@pytest.mark.parametrize(
    "list1, list2, expected_result", [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [], []),
        ([1], [2], [1, 2]),
        ([1, 1, 2], [1, 1, 3], [1, 1, 1, 1, 2, 3]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [0, 4, 5], [0, 1, 2, 3, 4, 5]),
        ([1, 3, 5], [1, 3, 5], [1, 1, 3, 3, 5, 5]),
        ([1, 2, 3], [2, 3, 4], [1, 2, 2, 3, 3, 4]),
        ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 2, 4], [2, 3, 4], [1, 2, 2, 2, 3, 4, 4]),
        ([5, 10, 15], [1, 7, 12], [1, 5, 7, 10, 12, 15]),
        ([1, 2, 3], [2, 3, 8], [1, 2, 2, 3, 3, 8]),
        ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
        ([5, 10, 20], [3, 8, 12], [3, 5, 8, 10, 12, 20]),
        ([0, 5, 10], [3, 8, 10], [0, 3, 5, 8, 10, 10]),
        ([1, 4, 6], [2, 3, 5], [1, 2, 3, 4, 5, 6]),
        ([2, 4, 6], [1, 3, 5], [1, 2, 3, 4, 5, 6]),
        ([0, 5, 10], [1, 3, 5], [0, 1, 3, 5, 5, 10]),
    ]
)

def test_merge_two_sorted_linked_lists(list1, list2, expected_result):
    solution = Solution()
    list1_linked = list_to_linkedlist(list1)
    list2_linked = list_to_linkedlist(list2)
    merged_list = solution.mergeTwoLists(list1_linked, list2_linked)
    assert linkedlist_to_list(merged_list) == expected_result