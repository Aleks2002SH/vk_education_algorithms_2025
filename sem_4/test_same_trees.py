from same_trees import isSameTree

import unittest
from build_tree import buildTree, TreeNode

class TestIsSameTree(unittest.TestCase):

    def test_case_1(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertTrue(result)

    def test_case_2(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, None]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertFalse(result)

    def test_case_3(self):
        arr1 = [1, 2, 3, 4, None, None, 5]
        arr2 = [1, 2, 3, 4, None, None, 5]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertTrue(result)

    def test_case_4(self):
        arr1 = [1, 2, 3, 4, 5, None, None]
        arr2 = [1, 2, 3, None, 5, None, None]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertFalse(result)

    def test_case_5(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertFalse(result)

    def test_case_6(self):
        arr1 = []
        arr2 = []
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertTrue(result)

    def test_case_7(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 4]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertFalse(result)

    def test_case_8(self):
        arr1 = [1, None, 3]
        arr2 = [1, None, 3]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertTrue(result)

    def test_case_9(self):
        arr1 = [1, 2, 3, 4]
        arr2 = [1, 2, 3, None, 4]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSameTree(root1, root2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
