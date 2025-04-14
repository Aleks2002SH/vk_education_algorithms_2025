from subtree import isSubtree
import unittest
from build_tree import buildTree, TreeNode
from same_trees import isSameTree


class TestIsSubtree(unittest.TestCase):

    def test_case_1(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [2, 4, 5]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertTrue(result)

    def test_case_2(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [3, 6]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertFalse(result)

    def test_case_3(self):
        arr1 = [1, 2, 3, 4, 5, 6]
        arr2 = [4, 5]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertFalse(result)

    def test_case_4(self):
        arr1 = [1, 2, 3, 4, 5, 6]
        arr2 = [1, 2, 3, 4]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertFalse(result)

    def test_case_5(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [2, 6, 5]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertFalse(result)

    def test_case_6(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertTrue(result)

    def test_case_7(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [5]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertTrue(result)

    def test_case_8(self):
        arr1 = [1, 2, 3, 4, 5, 6, 7]
        arr2 = [6]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertTrue(result)

    def test_case_9(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [4, 5, 6]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertFalse(result)

    def test_case_10(self):
        arr1 = [1]
        arr2 = [1]
        root1 = buildTree(arr1, 0)
        root2 = buildTree(arr2, 0)
        result = isSubtree(root1, root2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
