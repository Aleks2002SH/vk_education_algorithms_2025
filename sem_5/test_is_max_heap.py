from is_max_heap import isMaxHeap,isMaxHeap_tree

import unittest
from build_tree import *

class TestIsMaxHeap(unittest.TestCase):

    def test_case_1(self):
        arr = [10, 5, 3, 2, 4]
        self.assertTrue(isMaxHeap(arr))

    def test_case_2(self):
        arr = [10, 5, 3, 8, 4]
        self.assertFalse(isMaxHeap(arr))

    def test_case_3(self):
        arr = [1]
        self.assertTrue(isMaxHeap(arr))

    def test_case_4(self):
        arr = []
        self.assertTrue(isMaxHeap(arr))

    def test_case_5(self):
        arr = [20, 15, 10, 5, 8, 7, 3]
        self.assertTrue(isMaxHeap(arr))

    def test_case_6(self):
        arr = [3, 5, 8, 4, 6, 7]
        self.assertFalse(isMaxHeap(arr))

    def test_case_7(self):
        arr = [1, 2, 3, 4, 5]
        self.assertFalse(isMaxHeap(arr))


class TestIsMaxHeapTree(unittest.TestCase):

    def test_case_1(self):
        arr = [10, 5, 3, 2, 4]
        root = buildTree(arr, 0)
        self.assertTrue(isMaxHeap_tree(root))

    def test_case_2(self):
        arr = [10, 5, 3, 8, 4]
        root = buildTree(arr, 0)
        self.assertFalse(isMaxHeap_tree(root))

    def test_case_3(self):
        arr = [1]
        root = buildTree(arr, 0)
        self.assertTrue(isMaxHeap_tree(root))

    def test_case_4(self):
        root = None
        self.assertTrue(isMaxHeap_tree(root))

    def test_case_5(self):
        arr = [20, 15, 10, 5, 8, 7, 3]
        root = buildTree(arr, 0)
        self.assertTrue(isMaxHeap_tree(root))

    def test_case_6(self):
        arr = [3, 5, 8, 4, 6, 7]
        root = buildTree(arr, 0)
        self.assertFalse(isMaxHeap_tree(root))

    def test_case_7(self):
        arr = [1, 2, 3, 4, 5]
        root = buildTree(arr, 0)
        self.assertFalse(isMaxHeap_tree(root))


if __name__ == "__main__":
    unittest.main()