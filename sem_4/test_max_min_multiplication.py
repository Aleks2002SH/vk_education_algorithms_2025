from max_min_multiplication import maxMinMultiplication

import unittest
from build_tree import buildTree, TreeNode

class TestMaxMinMultiplicationBalancedTrees(unittest.TestCase):

    def test_case_1(self):
        data = [2, 1, 3]
        result = maxMinMultiplication(data)
        self.assertEqual(result, 3)

    def test_case_2(self):
        data = [4, 2, 6, 1, 3, 5, 7]
        result = maxMinMultiplication(data)
        self.assertEqual(result, 7)

    def test_case_3(self):
        data = [5, 2, 8, 1, 3, 6, 9]
        result = maxMinMultiplication(data)
        self.assertEqual(result, 9)

    def test_case_4(self):
        data = [3, 2, 5, 1, None, 4, None]
        result = maxMinMultiplication(data)
        self.assertEqual(result, 5)

    def test_case_5(self):
        data = [6, 3, 9, 2, 4, 7, 11, 1, None, None, 5, None, 8, 10, None]
        result = maxMinMultiplication(data)
        self.assertEqual(result,11)

    def test_case_6(self):
        data = [7, 4, 10, 2, 5, 8, 12, 1, 3, None, 6, None, 9, 11, 13]
        result = maxMinMultiplication(data)
        self.assertEqual(result, 13)

    def test_case_7(self):
        data = [5, 3]
        result = maxMinMultiplication(data)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
