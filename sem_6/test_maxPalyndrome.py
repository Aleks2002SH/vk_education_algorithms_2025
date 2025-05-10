from maxPalyndrome import maxPalyndrome
import unittest

class TestMaxPalyndrome(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(maxPalyndrome("babad") in ["bab", "aba"], True)

    def test_case_2(self):
        self.assertEqual(maxPalyndrome("cbbd"), "bb")

    def test_case_3(self):
        self.assertEqual(maxPalyndrome("a"), "a")

    def test_case_4(self):
        self.assertIn(maxPalyndrome("ac"), ["a","c"]) 

    def test_case_5(self):
        self.assertEqual(maxPalyndrome("racecar"), "racecar")

    def test_case_6(self):
        self.assertEqual(maxPalyndrome("abcdcba"), "abcdcba")

    def test_case_7(self):
        self.assertEqual(maxPalyndrome("forgeeksskeegfor"), "geeksskeeg")

    def test_case_8(self):
        self.assertEqual(maxPalyndrome(""), "")

    def test_case_9(self):
        self.assertEqual(maxPalyndrome("aa"), "aa")

    def test_case_10(self):
        self.assertEqual(maxPalyndrome("abacdfgdcaba"), "aba")

if __name__ == "__main__":
    unittest.main()