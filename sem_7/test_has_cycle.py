import unittest
from has_cycle import has_cycle


class TestHasCycle(unittest.TestCase):

    def test_case_1(self):
        graph = {0: [1], 1: [0]}
        self.assertFalse(has_cycle(graph))

    def test_case_2(self):
        graph = {0: [1], 1: [2], 2: [0]}
        self.assertTrue(has_cycle(graph))

    def test_case_3(self):
        graph = {0: [1], 1: [2], 2: []}
        self.assertFalse(has_cycle(graph))

    def test_case_4(self):
        graph = {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1]
        }
        self.assertFalse(has_cycle(graph))

    def test_case_5(self):
        graph = {
            0: [1],
            1: [2],
            2: [0]
        }
        self.assertTrue(has_cycle(graph))

    def test_case_6(self):
        graph = {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        }
        self.assertFalse(has_cycle(graph))

    def test_case_7(self):
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 0]
        }
        self.assertTrue(has_cycle(graph))

    def test_case_8(self):
        graph = {}
        self.assertFalse(has_cycle(graph))

    def test_case_9(self):
        graph = {0: []}
        self.assertFalse(has_cycle(graph))

if __name__ == '__main__':
    unittest.main()