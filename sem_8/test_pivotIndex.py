from pivotIndex import pivotIndex
import unittest

class TestPivotIndex(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(pivotIndex([1, 7, 3, 6, 5, 6]), 3)

    def test_case_2(self):
        self.assertEqual(pivotIndex([1, 2, 3]), -1)

    def test_case_3(self):
        self.assertEqual(pivotIndex([2, 1, -1]), 0)

    def test_case_4(self):
        self.assertEqual(pivotIndex([0, 0, 0, 0]), 0)

    def test_case_5(self):
        self.assertEqual(pivotIndex([1, -1, 0]), 2)

    def test_case_6(self):
        self.assertEqual(pivotIndex([1, 2, 3, 4, 0, 10]), 4)

    def test_case_7(self):
        self.assertEqual(pivotIndex([1]), 0)

    def test_case_8(self):
        self.assertEqual(pivotIndex([]), -1)

if __name__ == '__main__':
    unittest.main()