from complete_binary_tree import isCompleteTree

import unittest
from build_tree import *

class TestIsCompleteTree(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 3, 4, 5, 6]
        root = buildTree(arr, 0)
        self.assertTrue(isCompleteTree(root))

    def test_case_2(self):
        arr = [1, 2, 3, 4, 5, None, None]
        root = buildTree(arr, 0)
        self.assertTrue(isCompleteTree(root))

    def test_case_3(self):
        arr = [1, 2, 3, 4, None, 6, 7]
        root = buildTree(arr, 0)
        self.assertFalse(isCompleteTree(root))

    def test_case_4(self):
        arr = [1, 2, 3, None, 5, None, None]
        root = buildTree(arr, 0)
        self.assertFalse(isCompleteTree(root))

    def test_case_5(self):
        root = None
        self.assertTrue(isCompleteTree(root))

    def test_case_6(self):
        arr = [1, 2, 3]
        root = buildTree(arr, 0)
        self.assertTrue(isCompleteTree(root))

if __name__ == "__main__":
    unittest.main()