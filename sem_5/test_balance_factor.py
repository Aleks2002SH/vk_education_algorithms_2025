from balance_factor import calculateHeightAndBalance

import unittest
from build_tree import buildTree, TreeNode

class TestCalculateHeightAndBalance(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = buildTree(arr, 0)
        calculateHeightAndBalance(root)
        self.assertEqual(root.balanceFactor, 0)
        self.assertEqual(root.left.balanceFactor, 0)
        self.assertEqual(root.right.balanceFactor, 0)
        self.assertEqual(root.left.left.balanceFactor, 0)
        self.assertEqual(root.left.right.balanceFactor, 0)
        self.assertEqual(root.right.left.balanceFactor, 0)
        self.assertEqual(root.right.right.balanceFactor, 0)

    def test_case_2(self):
        root = None
        height = calculateHeightAndBalance(root)
        self.assertEqual(height, 0)

    def test_case_3(self):
        root = TreeNode(1)
        height = calculateHeightAndBalance(root)
        self.assertEqual(height, 1)
        self.assertEqual(root.balanceFactor, 0)

    def test_case_4(self):
        arr = [1, 2, None, 3, None, None,None]
        root = buildTree(arr, 0)
        calculateHeightAndBalance(root)
        self.assertEqual(root.balanceFactor, 2)
        self.assertEqual(root.left.balanceFactor, 1)
        self.assertEqual(root.left.left.balanceFactor, 0)

    def test_case_5(self):
        arr = [1, 2, None, 3, None]
        root = buildTree(arr, 0)
        height = calculateHeightAndBalance(root)
        self.assertEqual(height, 3)
        self.assertEqual(root.balanceFactor, 2)
        self.assertEqual(root.left.balanceFactor, 1)
        self.assertEqual(root.left.left.balanceFactor, 0)

    def test_case_6(self):
        arr = [1, None, 2, None, None,3,4]
        root = buildTree(arr, 0)
        height = calculateHeightAndBalance(root)
        self.assertEqual(height, 3)
        self.assertEqual(root.balanceFactor, -2)
        self.assertEqual(root.right.balanceFactor, 0)
        self.assertEqual(root.right.right.balanceFactor, 0)

if __name__ == "__main__":
    unittest.main()
