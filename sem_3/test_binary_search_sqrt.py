from binary_search_sqrt import binarySearchSqrt
import unittest

class TestBinarySearchSqrt(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearchSqrt(0), 0)

    def test_case_2(self):
        self.assertEqual(binarySearchSqrt(1), 1)

    def test_case_3(self):
        self.assertEqual(binarySearchSqrt(2), 1)

    def test_case_4(self):
        self.assertEqual(binarySearchSqrt(3), 1)

    def test_case_5(self):
        self.assertEqual(binarySearchSqrt(4), 2)

    def test_case_6(self):
        self.assertEqual(binarySearchSqrt(9), 3)

    def test_case_7(self):
        self.assertEqual(binarySearchSqrt(10), 3)

    def test_case_8(self):
        self.assertEqual(binarySearchSqrt(15), 3)

    def test_case_9(self):
        self.assertEqual(binarySearchSqrt(16), 4)

    def test_case_10(self):
        self.assertEqual(binarySearchSqrt(26), 5)

    def test_case_11(self):
        self.assertEqual(binarySearchSqrt(100), 10)

if __name__ == '__main__':
    unittest.main()