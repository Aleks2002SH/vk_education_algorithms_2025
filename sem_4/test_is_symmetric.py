import unittest
from build_tree import buildTree, TreeNode
from queue import Queue
from is_symmetric import isSymmetricBFS,isSymmetricDFS

class TestSymmetryFunctions(unittest.TestCase):
    
    def test_isSymmetricBFS_case_1(self):
        arr = [1, 2, 2, 3, 4, 4, 3]
        root = buildTree(arr, 0)
        self.assertTrue(isSymmetricBFS(root))

    def test_isSymmetricBFS_case_2(self):
        arr = [1, 2, 2, None, 3, None, 3]
        root = buildTree(arr, 0)
        self.assertFalse(isSymmetricBFS(root))

    def test_isSymmetricBFS_case_3(self):
        arr = [1, 2, 2, 3, 4, 4, 3]
        root = buildTree(arr, 0)
        self.assertTrue(isSymmetricBFS(root))

    def test_isSymmetricBFS_case_4(self):
        arr = [1, 2, 2, None, None, 3, 3]
        root = buildTree(arr, 0)
        self.assertFalse(isSymmetricBFS(root))

    def test_isSymmetricDFS_case_1(self):
        arr = [1, 2, 2, 3, 4, 4, 3]
        root = buildTree(arr, 0)
        self.assertTrue(isSymmetricDFS(root))

    def test_isSymmetricDFS_case_2(self):
        arr = [1, 2, 2, None, 3, None, 3]
        root = buildTree(arr, 0)
        self.assertFalse(isSymmetricDFS(root))

    def test_isSymmetricDFS_case_3(self):
        arr = [1, 2, 2, 3, 4, 4, 3]
        root = buildTree(arr, 0)
        self.assertTrue(isSymmetricDFS(root))

    def test_isSymmetricDFS_case_4(self):
        arr = [1, 2, 2, None, None, 3, 3]
        root = buildTree(arr, 0)
        self.assertFalse(isSymmetricDFS(root))

    def test_isSymmetricBFS_case_5(self):
        root = None
        self.assertTrue(isSymmetricBFS(root))

    def test_isSymmetricDFS_case_5(self):
        root = None
        self.assertTrue(isSymmetricDFS(root))

    def test_isSymmetricBFS_case_6(self):
        arr = [1]
        root = buildTree(arr, 0)
        self.assertTrue(isSymmetricBFS(root))

    def test_isSymmetricDFS_case_6(self):
        arr = [1]
        root = buildTree(arr, 0)
        self.assertTrue(isSymmetricDFS(root))

if __name__ == '__main__':
    unittest.main()
