from two_sum import twoSum

import unittest

class TestTwoSum(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_case_2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])

    def test_case_3(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])

    def test_case_4(self):
        self.assertEqual(twoSum([1, 5, 6, 7, 9], 10), [0, 4])

    def test_case_5(self):
        self.assertEqual(twoSum([1, 2, 7, 4, 5], 5), [0, 3])

    def test_case_6(self):
        self.assertEqual(twoSum([0, 4, 3, 0], 0), [0, 3])

    def test_case_7(self):
        self.assertEqual(twoSum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_case_8(self):
        self.assertEqual(twoSum([1, 0, -1, -2, 3], 2), [2, 4])

    def test_case_9(self):
        self.assertEqual(twoSum([5, 5, 20, 40], 10),[0, 1])

    def test_case_10(self):
        self.assertEqual(twoSum([10, 20, 30, 40], 50), [1, 2])

if __name__ == '__main__':
    unittest.main()
