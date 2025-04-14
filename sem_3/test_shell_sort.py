from shell_sort import shell_sort

import unittest

class TestShellSort(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(shell_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_case_2(self):
        self.assertEqual(shell_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_case_3(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_case_4(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_case_5(self):
        self.assertEqual(shell_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_case_6(self):
        self.assertEqual(shell_sort([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])

    def test_case_7(self):
        self.assertEqual(shell_sort([10, 20, 10, 40, 30, 50, 60, 70]), [10, 10, 20, 30, 40, 50, 60, 70])

    def test_case_8(self):
        self.assertEqual(shell_sort([3, 3, 3, 2, 1, 4, 5, 6]), [1, 2, 3, 3, 3, 4, 5, 6])

    def test_case_9(self):
        self.assertEqual(shell_sort([]), [])

    def test_case_10(self):
        self.assertEqual(shell_sort([1]), [1])

if __name__ == '__main__':
    unittest.main()
