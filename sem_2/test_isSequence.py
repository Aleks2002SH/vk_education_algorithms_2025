import unittest
from isSequence import isSubsequence
from isSequence_queue import isSubsequence_q

class TestIsSubsequence(unittest.TestCase):
    def check(self, s, t, expected):
        self.assertEqual(isSubsequence(s, t), expected)
        self.assertEqual(isSubsequence_q(s, t), expected)

    def test_case_abc_ahbgdc(self):
        self.check("abc", "ahbgdc", True)

    def test_case_axc_ahbgdc(self):
        self.check("axc", "ahbgdc", False)

    def test_case_empty_s(self):
        self.check("", "ahbgdc", True)

    def test_case_empty_t(self):
        self.check("abc", "", False)

    def test_case_ace_abcde(self):
        self.check("ace", "abcde", True)

    def test_case_aec_abcde(self):
        self.check("aec", "abcde", False)

    def test_case_aaa_aaaaaa(self):
        self.check("aaa", "aaaaaa", True)

    def test_case_aab_aabbcc(self):
        self.check("aab", "aabbcc", True)

    def test_case_aab_fail(self):
        self.check("aab", "abacadaeafagaha", False)

    def test_case_aab_pass(self):
        self.check("aab", "abacadaeafagahb", True)

    def test_case_ab_aabbcc(self):
        self.check("ab", "aabbcc", True)

    def test_case_ab_ababababab(self):
        self.check("ab", "ababababab", True)

    def test_case_ab_bababababab(self):
        self.check("ab", "bababababab", True)

    def test_case_alphabet_in_order(self):
        self.check("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", True)

    def test_case_alphabet_reverse(self):
        self.check("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba", False)

    def test_case_long_a(self):
        self.check("a" * 100, "a" * 500, True)

    def test_case_long_a_vs_b(self):
        self.check("a" * 100, "b" * 100, False)

if __name__ == "__main__":
    unittest.main()
