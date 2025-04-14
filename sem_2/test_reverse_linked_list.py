import unittest
from reverse_linked_list import ListNode,reverseList


def create_linked_list(nodes):
    if nodes != []:
        head = ListNode(nodes[0])
        current = head
        for value in nodes[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    else:
        return None

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class TestReverseLinkedList(unittest.TestCase):

    def check(self, nodes, expected):
        head = create_linked_list(nodes)
        reversed_head = reverseList(head)
        self.assertEqual(linked_list_to_list(reversed_head), expected)

    def test_multiple_elements(self):
        self.check([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        self.check([10, 20, 30], [30, 20, 10])
        self.check([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
        self.check([7, 8, 9], [9, 8, 7])
        self.check([100, 200, 300, 400], [400, 300, 200, 100])
        self.check([9, 8, 7, 6], [6, 7, 8, 9])

    def test_repeated_elements(self):
        self.check([1, 1, 1], [1, 1, 1])

    def test_two_elements(self):
        self.check([10, 20], [20, 10])

    def test_single_element(self):
        self.check([1], [1])

    def test_empty_list(self):
        self.check([], [])

if __name__ == "__main__":
    unittest.main()