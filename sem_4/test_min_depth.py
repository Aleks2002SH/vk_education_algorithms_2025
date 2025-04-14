from min_depth import minDepth
import unittest
from build_tree import buildTree, TreeNode

class TestMinDepth(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 3, 4, 5, None, 6]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 3)

    def test_case_2(self):
        arr = [1, 2, 3, 4, None, None, 5]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 3)

    def test_case_3(self):
        arr = [1, None, 2, None, None, 3]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 3)

    def test_case_4(self):
        arr = [1, 2, 3, None, None, 4, 5]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 2)

    def test_case_5(self):
        arr = [1, 2, 3]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 2)

    def test_case_6(self):
        arr = [1, None, 2]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 2)

    def test_case_7(self):
        arr = [1]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 1)

    def test_case_8(self):
        arr = [1, None, None]
        root = buildTree(arr, 0)
        result = minDepth(root)
        self.assertEqual(result, 1)

    def test_case_9(self):
        root = None
        result = minDepth(root)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
