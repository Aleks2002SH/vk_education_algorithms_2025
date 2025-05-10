import unittest

from subarraySum import subarraySum


class TestSubarraySum(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(subarraySum([1,1,1], 2), 2)

    def test_case_2(self):
        self.assertEqual(subarraySum([1,2,3], 3), 2)

    def test_case_3(self):
        self.assertEqual(subarraySum([1,-1,0], 0), 3)

    def test_case_4(self):
        self.assertEqual(subarraySum([3,4,7,2,-3,1,4,2], 7), 4)

    def test_case_5(self):
        self.assertEqual(subarraySum([], 0), 0)

    def test_case_6(self):
        self.assertEqual(subarraySum([0,0,0,0,0], 0), 15)  # 5 elements → 15 subarrays that sum to 0

    def test_case_7(self):
        self.assertEqual(subarraySum([-1,-1,1], 0), 1)

    def test_case_8(self):
        self.assertEqual(subarraySum([1], 0), 0)

if __name__ == "__main__":
    unittest.main()