from dijkstra import dijkstra
import unittest

class TestDijkstra(unittest.TestCase):

    def test_case_1(self):
        graph = {
            0: {1: 4, 2: 1},
            1: {3: 1},
            2: {1: 2, 3: 5},
            3: {}
        }
        expected = {0: 0, 1: 3, 2: 1, 3: 4}
        self.assertEqual(dijkstra(graph, 0), expected)

    def test_case_2(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        expected = {'A': 0, 'B': 1, 'C': 3, 'D': 4}
        self.assertEqual(dijkstra(graph, 'A'), expected)

    def test_case_3(self):
        graph = {
            0: {},
            1: {0: 10}
        }
        expected = {0: 10, 1: 0}
        self.assertEqual(dijkstra(graph, 1), expected)

    def test_case_4(self):
        graph = {
            0: {1: 2},
            1: {2: 2},
            2: {3: 2},
            3: {}
        }
        expected = {0: 0, 1: 2, 2: 4, 3: 6}
        self.assertEqual(dijkstra(graph, 0), expected)

    def test_case_5(self):
        graph = {
            0: {},
        }
        expected = {0: 0}
        self.assertEqual(dijkstra(graph, 0), expected)

    def test_case_6(self):
        graph = {
            0: {1: 7, 2: 9, 5: 14},
            1: {0: 7, 2: 10, 3: 15},
            2: {0: 9, 1: 10, 3: 11, 5: 2},
            3: {1: 15, 2: 11, 4: 6},
            4: {3: 6, 5: 9},
            5: {0: 14, 2: 2, 4: 9}
        }
        expected = {0: 0, 1: 7, 2: 9, 3: 20, 4: 20, 5: 11}
        self.assertEqual(dijkstra(graph, 0), expected)

    def test_case_7(self):
        graph = {
            0: {1: 2, 2: 5},
            1: {2: 1},
            2: {3: 3},
            3: {}
        }
        expected = {0: 0, 1: 2, 2: 3, 3: 6}
        self.assertEqual(dijkstra(graph, 0), expected)

if __name__ == '__main__':
    unittest.main()