from is_min_heap import isMinHeap, isMinHeap_tree
import unittest
from build_tree import *

class TestIsMinHeap(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 3, 5, 7, 9]
        self.assertTrue(isMinHeap(arr))

    def test_case_2(self):
        arr = [1, 3, 0, 7, 9]
        self.assertFalse(isMinHeap(arr))

    def test_case_3(self):
        arr = [1]
        self.assertTrue(isMinHeap(arr))

    def test_case_4(self):
        arr = []
        self.assertTrue(isMinHeap(arr))

    def test_case_5(self):
        arr = [2, 4, 6, 8, 10, 12, 14]
        self.assertTrue(isMinHeap(arr))

    def test_case_6(self):
        arr = [5, 3, 8, 4, 2]
        self.assertFalse(isMinHeap(arr))

    def test_case_7(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(isMinHeap(arr))


class TestIsMinHeapTree(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 3, 5, 7, 9]
        root = buildTree(arr, 0)
        self.assertTrue(isMinHeap_tree(root))

    def test_case_2(self):
        arr = [1, 3, 0, 7, 9]
        root = buildTree(arr, 0)
        self.assertFalse(isMinHeap_tree(root))

    def test_case_3(self):
        arr = [1]
        root = buildTree(arr, 0)
        self.assertTrue(isMinHeap_tree(root))

    def test_case_4(self):
        root = None
        self.assertTrue(isMinHeap_tree(root))

    def test_case_5(self):
        arr = [2, 4, 6, 8, 10, 12, 14]
        root = buildTree(arr, 0)
        self.assertTrue(isMinHeap_tree(root))

    def test_case_6(self):
        arr = [5, 3, 8, 4, 2]
        root = buildTree(arr, 0)
        self.assertFalse(isMinHeap_tree(root))

    def test_case_7(self):
        arr = [1, 2, 3, 4, 5]
        root = buildTree(arr, 0)
        self.assertTrue(isMinHeap_tree(root))


if __name__ == "__main__":
    unittest.main()
