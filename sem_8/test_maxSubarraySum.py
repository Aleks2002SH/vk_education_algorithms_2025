from maxSubarraySum import maxSubarraySum
import unittest

class TestMaxSubarraySum(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(maxSubarraySum([1, 2, 3, 4, 5], 2), 9)

    def test_case_2(self):
        self.assertEqual(maxSubarraySum([5, 1, 3, 2, 6, 1], 3), 11)

    def test_case_3(self):
        self.assertEqual(maxSubarraySum([-1, -2, -3, -4], 2), -3)

    def test_case_4(self):
        self.assertEqual(maxSubarraySum([2, 1, 5, 1, 3, 2], 3), 9)

    def test_case_5(self):
        self.assertEqual(maxSubarraySum([10, -2, -1, 4, 5], 2), 9)

    def test_case_6(self):
        self.assertEqual(maxSubarraySum([100], 1), 100)

    def test_case_7(self):
        self.assertEqual(maxSubarraySum([1, 2], 3), None)

    def test_case_8(self):
        self.assertEqual(maxSubarraySum([], 1), None)

if __name__ == "__main__":
    unittest.main()