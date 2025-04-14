from extra_letter import extra_letter
import unittest

class TestExtraLetter(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(extra_letter("abcd", "abcde"), "e")

    def test_case_2(self):
        self.assertEqual(extra_letter("hello", "helloo"), "o")

    def test_case_3(self):
        self.assertEqual(extra_letter("apple", "applle"), "l")

    def test_case_4(self):
        self.assertEqual(extra_letter("abcd", "abced"), "e")

    def test_case_5(self):
        self.assertEqual(extra_letter("", "a"), "a")

    def test_case_6(self):
        self.assertEqual(extra_letter("z", "yz"), "y")

    def test_case_7(self):
        self.assertEqual(extra_letter("same", "sames"), "s")

    def test_case_8(self):
        self.assertEqual(extra_letter("xyz", "xyzv"), "v")

if __name__ == '__main__':
    unittest.main()
