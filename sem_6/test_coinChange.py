from coinChange import coinChange
import unittest

class TestCoinChange(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)

    def test_case_2(self):
        self.assertEqual(coinChange([2], 3), -1)

    def test_case_3(self):
        self.assertEqual(coinChange([1], 0), 0)

    def test_case_4(self):
        self.assertEqual(coinChange([1], 2), 2)

    def test_case_5(self):
        self.assertEqual(coinChange([2, 5, 10, 1], 27), 4)

    def test_case_6(self):
        self.assertEqual(coinChange([186, 419, 83, 408], 6249), 20)

    def test_case_7(self):
        self.assertEqual(coinChange([3, 7, 405, 436], 8839), 25)

    def test_case_8(self):
        self.assertEqual(coinChange([], 7), -1)

if __name__ == "__main__":
    unittest.main()