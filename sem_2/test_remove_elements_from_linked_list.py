import unittest
from remove_elements_from_linked_list import ListNode,removeElements

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

class TestRemoveElements(unittest.TestCase):

    def check(self, nodes, val, expected):
        head = create_linked_list(nodes)
        result = removeElements(head, val)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_removal_of_existing_values(self):
        self.check([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])
        self.check([1, 2, 3, 4, 5], 3, [1, 2, 4, 5])
        self.check([1, 2, 2, 2, 3], 2, [1, 3])
        self.check([1, 2, 3], 2, [1, 3])
        self.check([5, 4, 3, 2, 1], 2, [5, 4, 3, 1])
        self.check([9, 8, 7, 6, 5, 4], 5, [9, 8, 7, 6, 4])
        self.check([2, 4, 6, 8, 10], 10, [2, 4, 6, 8])
        self.check([3, 4, 5, 6, 7], 5, [3, 4, 6, 7])
        self.check([10, 20, 30, 40, 50], 40, [10, 20, 30, 50])

    def test_removal_of_nonexistent_values(self):
        self.check([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5])
        self.check([10, 20, 30, 40], 25, [10, 20, 30, 40])

    def test_complete_removal(self):
        self.check([7, 7, 7, 7], 7, [])
        self.check([10], 10, [])
        self.check([1, 1, 1], 1, [])
        self.check([9, 9, 9, 9], 9, [])
        self.check([1, 1, 1, 1, 1], 1, [])

if __name__ == "__main__":
    unittest.main()
