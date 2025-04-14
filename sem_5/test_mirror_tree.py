from mirror_tree import mirrorTree,mirrorTreeIterative

import unittest
from build_tree import *

class TestMirrorTree(unittest.TestCase):

    def test_case_1(self):
        tree = buildTree([5, 3, 7, 2, 4, 6, 8],0)
        mirrored_tree = mirrorTree(tree)
        self.assertEqual(mirrored_tree.left.data, 7)
        self.assertEqual(mirrored_tree.right.data, 3)

    def test_case_2(self):
        tree = buildTree([1, 2, 3],0)
        mirrored_tree = mirrorTree(tree)
        self.assertEqual(mirrored_tree.left.data, 3)
        self.assertEqual(mirrored_tree.right.data, 2)

    def test_case_3(self):
        tree = buildTree([10, 5, 15, 2, 8, 12, 20],0)
        mirrored_tree = mirrorTree(tree)
        self.assertEqual(mirrored_tree.left.data, 15)
        self.assertEqual(mirrored_tree.right.data, 5)
        self.assertEqual(mirrored_tree.left.left.data, 20)
        self.assertEqual(mirrored_tree.left.right.data, 12)

    def test_case_4(self):
        tree = buildTree([2, 1, 3],0)
        mirrored_tree = mirrorTree(tree)
        self.assertEqual(mirrored_tree.left.data, 3)

    def test_case_5(self):
        tree = None
        mirrored_tree = mirrorTree(tree)
        self.assertIsNone(mirrored_tree)

    def test_case_6(self):
        tree = buildTree([42],0)
        mirrored_tree = mirrorTree(tree)
        self.assertEqual(mirrored_tree.data, 42)

    def test_case_7(self):
        tree = buildTree([1, 2, 3, 4, 5, 6, 7],0)
        mirrored_tree = mirrorTree(tree)
        self.assertEqual(mirrored_tree.left.data, 3)
        self.assertEqual(mirrored_tree.right.data, 2)

    def test_case_8(self):
        tree = buildTree([1, 3, 2],0)
        mirrored_tree = mirrorTreeIterative(tree)
        self.assertEqual(mirrored_tree.left.data, 2)
        self.assertEqual(mirrored_tree.right.data, 3)

    def test_case_9(self):
        tree = buildTree([5, 3, 8, 1, 4, 7, 9],0)
        mirrored_tree = mirrorTreeIterative(tree)
        self.assertEqual(mirrored_tree.left.data, 8)
        self.assertEqual(mirrored_tree.right.data, 3)

    def test_case_10(self):
        tree = buildTree([10, 5, 20, 3, 8, 15, 25],0)
        mirrored_tree = mirrorTreeIterative(tree)
        self.assertEqual(mirrored_tree.left.data, 20)
        self.assertEqual(mirrored_tree.right.data, 5)

if __name__ == "__main__":
    unittest.main()