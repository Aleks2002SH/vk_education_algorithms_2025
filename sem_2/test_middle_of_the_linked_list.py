import unittest
from middle_of_the_linked_list import ListNode, middleNode

def create_linked_list(nodes):
    head = ListNode(nodes[0])
    current = head
    for value in nodes[1:]:
        node = ListNode(value)
        current.next = node
        current = node
    return head

class TestMiddleNode(unittest.TestCase):

    def check_middle(self, nodes, expected):
        head = create_linked_list(nodes)
        result = middleNode(head)
        self.assertEqual(result.val, expected)

    def test_odd_length_lists(self):
        self.check_middle([1, 2, 3, 4, 5, 6, 7], 4)
        self.check_middle([5, 10, 15, 20, 25, 30, 35], 20)
        self.check_middle([100, 200, 300, 400, 500], 300)
        self.check_middle([10, 20, 30], 20)
        self.check_middle([1, 2, 3], 2)
        self.check_middle([9, 8, 7, 6, 5], 7)
        self.check_middle([1, 1, 1, 1, 1], 1)

    def test_even_length_lists(self):
        self.check_middle([1, 2, 3, 4, 5, 6], 4)
        self.check_middle([2, 3, 4, 5, 6, 7], 5)
        self.check_middle([1, 2, 3, 4], 3)
        self.check_middle([7, 14, 21, 28, 35, 42], 28)
        self.check_middle([15, 20, 25, 30], 25)
        self.check_middle([1, 2, 3, 4, 5, 6, 7, 8], 5)
        self.check_middle([1, 2, 3, 4, 5, 6], 4)

    def test_varied_sequences(self):
        self.check_middle([8, 9, 10, 11, 12, 13, 14, 15], 12)
        self.check_middle([1000, 2000, 3000, 4000, 5000], 3000)
        self.check_middle([10, 20, 30, 40, 50], 30)
        self.check_middle([1, 2], 2)
        self.check_middle([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)

if __name__ == "__main__":
    unittest.main()