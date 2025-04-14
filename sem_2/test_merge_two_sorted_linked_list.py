import unittest

from merge_two_sorted_linked_lists import mergeTwoLists,ListNode

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

class TestMergeTwoSortedLists(unittest.TestCase):
    

    def check_merge(self, list1, list2, expected):
        list1_linked = list_to_linkedlist(list1)
        list2_linked = list_to_linkedlist(list2)
        result = mergeTwoLists(list1_linked, list2_linked)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_basic_merges(self):
        self.check_merge([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
        self.check_merge([1], [2], [1, 2])
        self.check_merge([1, 2, 3], [2, 3, 4], [1, 2, 2, 3, 3, 4])

    def test_empty_lists(self):
        self.check_merge([], [1, 2, 3], [1, 2, 3])
        self.check_merge([1, 2, 3], [], [1, 2, 3])
        self.check_merge([], [], [])

    def test_duplicates(self):
        self.check_merge([1, 1, 2], [1, 1, 3], [1, 1, 1, 1, 2, 3])
        self.check_merge([1, 3, 5], [1, 3, 5], [1, 1, 3, 3, 5, 5])
        self.check_merge([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1])

    def test_alternating_merge(self):
        self.check_merge([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6])
        self.check_merge([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8])

    def test_mixed_order(self):
        self.check_merge([5, 10, 15], [1, 7, 12], [1, 5, 7, 10, 12, 15])
        self.check_merge([5, 10, 20], [3, 8, 12], [3, 5, 8, 10, 12, 20])
        self.check_merge([0, 5, 10], [3, 8, 10], [0, 3, 5, 8, 10, 10])
        self.check_merge([0, 5, 10], [1, 3, 5], [0, 1, 3, 5, 5, 10])

    def test_crossed_merge(self):
        self.check_merge([1, 2, 3], [0, 4, 5], [0, 1, 2, 3, 4, 5])
        self.check_merge([1, 2, 2, 4], [2, 3, 4], [1, 2, 2, 2, 3, 4, 4])
        self.check_merge([1, 4, 6], [2, 3, 5], [1, 2, 3, 4, 5, 6])
        self.check_merge([2, 4, 6], [1, 3, 5], [1, 2, 3, 4, 5, 6])
        self.check_merge([1, 2, 3], [2, 3, 8], [1, 2, 2, 3, 3, 8])

if __name__ == "__main__":
    unittest.main()