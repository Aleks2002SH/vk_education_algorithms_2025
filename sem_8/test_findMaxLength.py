import unittest 
from findMaxLength import findMaxLength

class TestFindMaxLength(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(findMaxLength([0, 1]), 2)

    def test_case_2(self):
        self.assertEqual(findMaxLength([0, 1, 0]), 2)

    def test_case_3(self):
        self.assertEqual(findMaxLength([0, 1, 0, 1]), 4)

    def test_case_4(self):
        self.assertEqual(findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]), 6)

    def test_case_5(self):
        self.assertEqual(findMaxLength([1, 1, 1, 1]), 0)

    def test_case_6(self):
        self.assertEqual(findMaxLength([0, 0, 0, 1, 1, 1]), 6)

    def test_case_7(self):
        self.assertEqual(findMaxLength([]), 0)

    def test_case_8(self):
        self.assertEqual(findMaxLength([1, 0, 1, 0, 1, 0]), 6)

if __name__ == '__main__':
    unittest.main()