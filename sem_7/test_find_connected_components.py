from find_connected_components import find_connected_componenets, find_connected_components_color
import unittest

class TestFindConnectedComponents(unittest.TestCase):

    def assertComponentsEqual(self, result, expected):
        self.assertCountEqual([set(c) for c in result], [set(c) for c in expected])

    def test_case_1(self):
        graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
        expected = [[0, 1], [2, 3], [4]]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

    def test_case_2(self):
        graph = {0: [], 1: [], 2: []}
        expected = [[0], [1], [2]]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

    def test_case_3(self):
        graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}
        expected = [[0, 1, 2], [3, 4]]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

    def test_case_4(self):
        graph = {0: [1], 1: [2], 2: [0]}
        expected = [[0, 1, 2]]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

    def test_case_5(self):
        graph = {0: [1], 1: [2], 2: [], 3: []}
        expected = [[0, 1, 2], [3]]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

    def test_case_6(self):
        graph = {i: [] for i in range(10)}
        expected = [[i] for i in range(10)]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

    def test_case_7(self):
        graph = {0: [1], 1: [2], 2: [3], 3: []}
        expected = [[0, 1, 2, 3]]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

    def test_case_8(self):
        graph = {0: [1], 1: [2], 2: [3], 3: [0]}
        expected = [[0, 1, 2, 3]]
        result = find_connected_componenets(graph)
        self.assertComponentsEqual(result, expected)

class TestFindConnectedComponentsColor(unittest.TestCase):

    def test_case_1(self):
        graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 3)

    def test_case_2(self):
        graph = {0: [], 1: [], 2: []}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 3)

    def test_case_3(self):
        graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 2)

    def test_case_4(self):
        graph = {0: [1], 1: [2], 2: [0]}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 1)

    def test_case_5(self):
        graph = {0: [1], 1: [2], 2: [], 3: []}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 2)

    def test_case_6(self):
        graph = {i: [] for i in range(10)}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 10)

    def test_case_7(self):
        graph = {0: [1], 1: [2], 2: [3], 3: []}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 1)

    def test_case_8(self):
        graph = {0: [1], 1: [2], 2: [3], 3: [0]}
        result = find_connected_components_color(graph)
        self.assertEqual(len(set(result.values())), 1)

if __name__ == "__main__":
    unittest.main()