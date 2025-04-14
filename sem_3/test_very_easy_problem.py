from very_easy_problem import copyTime
import unittest

class Test_very_easy_problem(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(copyTime(4, 1, 1), 3)

    def test_case_2(self):
        self.assertEqual(copyTime(4, 1, 2), 3)

    def test_case_3(self):
        self.assertEqual(copyTime(1, 1, 2), 1)

    def test_case_4(self):
        self.assertEqual(copyTime(5, 2, 3), 7)

    def test_case_5(self):
        self.assertEqual(copyTime(10, 1, 5), 9)

    def test_case_6(self):
        self.assertEqual(copyTime(2, 5, 6), 8)

    def test_case_7(self):
        self.assertEqual(copyTime(3, 3, 3), 6)

    def test_case_8(self):
        self.assertEqual(copyTime(6, 1, 2), 5)

    def test_case_9(self):
        self.assertEqual(copyTime(7, 3, 4), 14)

    def test_case_10(self):
        self.assertEqual(copyTime(10, 2, 2), 11)

if __name__ == '__main__':
    unittest.main()