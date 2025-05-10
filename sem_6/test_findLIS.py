from findLIS import findLIS
import unittest

class TestFindLIS(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(findLIS([]), 0)

    def test_case_2(self):
        self.assertEqual(findLIS([42]), 1)

    def test_case_3(self):
        self.assertEqual(findLIS([1, 2, 3, 4, 5]), 5)

    def test_case_4(self):
        self.assertEqual(findLIS([5, 4, 3, 2, 1]), 1)

    def test_case_5(self):
        self.assertEqual(findLIS([1, 3, 5, 4, 7]), 3)

    def test_case_6(self):
        self.assertEqual(findLIS([1, 2, 1, 2, 3, 0, 1]), 3)

    def test_case_7(self):
        self.assertEqual(findLIS([2, 2, 2, 2]), 1)

    def test_case_8(self):
        self.assertEqual(findLIS([1, 2, 3, 1, 2, 3, 4]), 4)

if __name__ == "__main__":
    unittest.main()