import unittest
from isTree import isTree


class TestIsTree(unittest.TestCase):

    def test_case_1(self):
        graph = {
            0: [1],
            1: [0, 2],
            2: [1]
        }
        self.assertTrue(isTree(graph, 0))

    def test_case_2(self):
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 0]
        }
        self.assertFalse(isTree(graph, 0))

    def test_case_3(self):
        graph = {
            0: [1, 2],
            1: [0],
            2: [0]
        }
        self.assertTrue(isTree(graph, 0))

    def test_case_4(self):
        graph = {
            0: [1],
            1: [0],
            2: []
        }
        self.assertFalse(isTree(graph, 0))

    def test_case_5(self):
        graph = {
            0: []
        }
        self.assertTrue(isTree(graph, 0))

    def test_case_6(self):
        graph = {
            0: [1],
            1: [0, 2, 3],
            2: [1],
            3: [1, 4],
            4: [3]
        }
        self.assertTrue(isTree(graph, 0))

    def test_case_7(self):
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2, 0]
        }
        self.assertFalse(isTree(graph, 0))

if __name__ == '__main__':
    unittest.main()