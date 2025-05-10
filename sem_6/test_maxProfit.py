from maxProfit import maxProfit
import unittest

class TestMaxProfit(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(maxProfit([7,1,5,3,6,4]), 5)

    def test_case_2(self):
        self.assertEqual(maxProfit([7,6,4,3,1]), 0)

    def test_case_3(self):
        self.assertEqual(maxProfit([1,2,3,4,5]), 4)

    def test_case_4(self):
        self.assertEqual(maxProfit([2,1,2,1,0,1,2]), 2)

    def test_case_5(self):
        self.assertEqual(maxProfit([3,3,3,3,3]), 0)

    def test_case_6(self):
        self.assertEqual(maxProfit([1]), 0)

    def test_case_7(self):
        self.assertEqual(maxProfit([2, 4, 1]), 2)

if __name__ == "__main__":
    unittest.main()