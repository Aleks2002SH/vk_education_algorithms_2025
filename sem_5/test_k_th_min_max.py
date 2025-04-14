from k_th_min_max import inorderMax,inorderMin,inorderMinIterative,inorderMaxIterative

import unittest
from build_tree import *

class TestInorderMinMax(unittest.TestCase):

    def test_case_1(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        root = buildTree(arr, 0)
        k = 3
        cnt = [0]
        result = inorderMin(root, k, cnt)
        self.assertEqual(result, 3)

    def test_case_2(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        root = buildTree(arr, 0)
        k = 2
        cnt = [0]
        result = inorderMin(root, k, cnt)
        self.assertEqual(result, 2)

    def test_case_3(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        root = buildTree(arr, 0)
        k = 5
        cnt = [0]
        result = inorderMin(root, k, cnt)
        self.assertEqual(result, 5)

    def test_case_4(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        root = buildTree(arr, 0)
        k = 1
        result = inorderMinIterative(root, k)
        self.assertEqual(result, 1)

    def test_case_5(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        root = buildTree(arr, 0)
        k = 7
        cnt = [0]
        result = inorderMin(root, k, cnt)
        self.assertEqual(result, 7)

    def test_case_6(self):
        arr = [5, 3, 8, 1, 4, 6, 10]
        root = buildTree(arr, 0)
        k = 4
        result = inorderMinIterative(root, k)
        self.assertEqual(result, 5)

    def test_case_7(self):
        arr = [5, 3, 8, 1, 4, 6, 10]
        root = buildTree(arr, 0)
        k = 6
        cnt = [0]
        result = inorderMin(root, k, cnt)
        self.assertEqual(result, 8)


    def test_case_8(self):
        arr = [5, 3, 8, 1, 4, 6, 10]
        root = buildTree(arr, 0)
        k = 7
        cnt = [0]
        result = inorderMax(root, k, cnt)
        self.assertEqual(result, 1)

    def test_case_9(self):
        arr = [5, 3, 8, 1, 4, 6, 10]
        root = buildTree(arr, 0)
        k = 1
        cnt = [0]
        result = inorderMax(root, k, cnt)
        self.assertEqual(result, 10)

    def test_case_10(self):
        arr = [5, 3, 8, 1, 4, 6, 10]
        root = buildTree(arr, 0)
        k = 4
        cnt = [0]
        result = inorderMax(root, k, cnt)
        self.assertEqual(result, 5)

    def test_case_11(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        root = buildTree(arr, 0)
        k = 3
        result = inorderMaxIterative(root, k)
        self.assertEqual(result, 5)

    def test_case_12(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        root = buildTree(arr, 0)
        k = 6
        cnt = [0]
        result = inorderMax(root, k, cnt)
        self.assertEqual(result, 2)

    def test_case_13(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = buildTree(arr, 0)
        k = 2
        result = inorderMaxIterative(root, k)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
