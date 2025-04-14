import unittest
from linked_list_cycle import ListNode, hasCycle

def build_linked_list(nodes, pos):
    if not nodes:
        return None
    head = ListNode(nodes[0])
    current = head
    cycle_node = head if pos == 0 else None
    nodes_map = [head]

    for i, val in enumerate(nodes[1:], start=1):
        new_node = ListNode(val)
        nodes_map.append(new_node)
        current.next = new_node
        current = new_node
        if i == pos:
            cycle_node = new_node

    if pos != -1:
        current.next = cycle_node
    return head

class TestHasCycle(unittest.TestCase):

    def test_case_cycle_at_position_0(self):
        self._test_cycle([1, 2, 3, 4, 5], 0, True)

    def test_case_cycle_at_position_2(self):
        self._test_cycle([1, 2, 3, 4, 5], 2, True)

    def test_case_no_cycle(self):
        self._test_cycle([1, 2, 3, 4, 5], -1, False)

    def test_case_single_node_no_cycle(self):
        self._test_cycle([10], -1, False)

    def test_case_single_node_cycle(self):
        self._test_cycle([10], 0, True)

    def test_case_cycle_at_position_1(self):
        self._test_cycle([3, 5, 7], 1, True)

    def test_case_cycle_at_position_3(self):
        self._test_cycle([1, 2, 3, 4], 3, True)

    def test_case_cycle_at_position_2_reverse(self):
        self._test_cycle([9, 8, 7, 6, 5, 4], 2, True)

    def test_case_cycle_at_position_1_small_list(self):
        self._test_cycle([1, 2], 1, True)

    def test_case_cycle_at_position_4(self):
        self._test_cycle([1, 2, 3, 4, 5], 4, True)

    def test_case_cycle_not_found(self):
        self._test_cycle([3, 2], -1, False)

    def test_case_multiple_nodes_no_cycle(self):
        self._test_cycle([10, 20, 30, 40, 50], -1, False)

    def test_case_cycle_at_position_5(self):
        self._test_cycle([1, 2, 3, 4, 5, 6], 5, True)

    def test_case_small_list_no_cycle(self):
        self._test_cycle([1, 2, 3], -1, False)

    def _test_cycle(self, nodes, pos, expected):
        head = build_linked_list(nodes, pos)
        self.assertEqual(hasCycle(head), expected)

if __name__ == "__main__":
    unittest.main()