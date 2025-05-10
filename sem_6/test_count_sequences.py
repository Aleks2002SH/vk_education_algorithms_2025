from count_sequences import count_sequences
import unittest

class TestCountSequences(unittest.TestCase):

    def test_base_case_0(self):
        self.assertEqual(count_sequences(0), 1)

    def test_base_case_1(self):
        self.assertEqual(count_sequences(1), 2)

    def test_base_case_2(self):
        self.assertEqual(count_sequences(2), 4)

    def test_case_3(self):
        self.assertEqual(count_sequences(3), 7)

    def test_case_4(self):
        self.assertEqual(count_sequences(4), 13)

    def test_case_5(self):
        self.assertEqual(count_sequences(5), 24)

    def test_case_6(self):
        self.assertEqual(count_sequences(6), 44)

    def test_case_10(self):
        self.assertEqual(count_sequences(10), 504)

    def test_case_15(self):
        self.assertEqual(count_sequences(15), 10609)

if __name__ == "__main__":
    unittest.main()