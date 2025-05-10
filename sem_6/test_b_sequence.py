import unittest
from b_sequence import b_sequence


class TestBSequence(unittest.TestCase):

    def test_length_1(self):
        self.assertEqual(b_sequence(1), 2)

    def test_length_2(self):
        self.assertEqual(b_sequence(2), 3)

    def test_length_3(self):
        self.assertEqual(b_sequence(3), 5)

    def test_length_4(self):
        self.assertEqual(b_sequence(4), 8)

    def test_length_5(self):
        self.assertEqual(b_sequence(5), 13)

    def test_length_10(self):
        self.assertEqual(b_sequence(10), 144)

    def test_length_20(self):
        self.assertEqual(b_sequence(20), 17711)

    def test_large_input(self):
        self.assertEqual(b_sequence(30), 2178309)

if __name__ == "__main__":
    unittest.main()