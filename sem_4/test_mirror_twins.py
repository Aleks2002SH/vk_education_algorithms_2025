from mirror_twins import CountMirrorTwins

import unittest
from build_tree import buildTree, TreeNode

class TestCountMirrorTwins(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 2, 3, 4, 4, 3]
        root = buildTree(arr, 0)
        result = CountMirrorTwins(root)
        self.assertEqual(result, 3)

    def test_case_2(self):
        arr = [1, 2, 3, None, None, None, None]
        root = buildTree(arr, 0)
        result = CountMirrorTwins(root)
        self.assertEqual(result, 0)

    def test_case_3(self):
        arr = [1, 1, 1, 1, 1, 1, 1]
        root = buildTree(arr, 0)
        result = CountMirrorTwins(root)
        self.assertEqual(result, 3)

    def test_case_4(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = buildTree(arr, 0)
        result = CountMirrorTwins(root)
        self.assertEqual(result, 0)

    def test_case_5(self):
        arr = [1, 2, 2, 2, 2, 2, 2]
        root = buildTree(arr, 0)
        result = CountMirrorTwins(root)
        self.assertEqual(result, 3)

    def test_case_6(self):
        arr = [1, None, 2, None, 3, None, 4]
        root = buildTree(arr, 0)
        result = CountMirrorTwins(root)
        self.assertEqual(result, 0)

    def test_case_7(self):
        arr = [1, 2, 2, 2, 3, 3, 3]
        root = buildTree(arr, 0)
        result = CountMirrorTwins(root)
        self.assertEqual(result, 2)

    def test_empty(self):
        root = None
        result = CountMirrorTwins(root)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
