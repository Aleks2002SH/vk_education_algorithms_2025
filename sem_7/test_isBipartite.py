from isBipartite import isBipartite_bfs,isBipartite_dfs
import unittest


class TestIsBipartiteBFS(unittest.TestCase):
    def test_case_1(self):
        graph = [[1,3],[0,2],[1,3],[0,2]]
        self.assertTrue(isBipartite_bfs(graph))

    def test_case_2(self):
        graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
        self.assertFalse(isBipartite_bfs(graph))

    def test_case_3(self):
        graph = [[]]
        self.assertTrue(isBipartite_bfs(graph))

    def test_case_4(self):
        graph = [[1],[0,3],[3],[1,2]]
        self.assertTrue(isBipartite_bfs(graph))

    def test_case_5(self):
        graph = [[1],[0,2,3],[1,3],[1,2]]
        self.assertFalse(isBipartite_bfs(graph))

    def test_case_6(self):
        graph = [[1],[0]]
        self.assertTrue(isBipartite_bfs(graph))

    def test_case_7(self):
        graph = [[1,2,3],[0],[0],[0]]
        self.assertTrue(isBipartite_bfs(graph))

    def test_case_8(self):
        graph = [[1,3],[0,2],[1,3],[0,2]]
        self.assertTrue(isBipartite_bfs(graph))


class TestIsBipartiteDFS(unittest.TestCase):
    def test_case_1(self):
        graph = [[1,3],[0,2],[1,3],[0,2]]
        self.assertTrue(isBipartite_dfs(graph))

    def test_case_2(self):
        graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
        self.assertFalse(isBipartite_dfs(graph))

    def test_case_3(self):
        graph = [[]]
        self.assertTrue(isBipartite_dfs(graph))

    def test_case_4(self):
        graph = [[1],[0,3],[3],[1,2]]
        self.assertTrue(isBipartite_dfs(graph))

    def test_case_5(self):
        graph = [[1],[0,2,3],[1,3],[1,2]]
        self.assertFalse(isBipartite_dfs(graph))

    def test_case_6(self):
        graph = [[1],[0]]
        self.assertTrue(isBipartite_dfs(graph))

    def test_case_7(self):
        graph = [[1,2,3],[0],[0],[0]]
        self.assertTrue(isBipartite_dfs(graph))

    def test_case_8(self):
        graph = [[1,3],[0,2],[1,3],[0,2]]
        self.assertTrue(isBipartite_dfs(graph))


if __name__ == "__main__":
    unittest.main()