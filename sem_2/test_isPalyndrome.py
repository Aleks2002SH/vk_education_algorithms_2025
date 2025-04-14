import unittest
from isPalyndrome import isPalindrome

class TestIsPalindrome(unittest.TestCase):
    

    def test_common_palindromes(self):
        test_data = [
            ("A man, a plan, a canal: Panama", True),
            ("Able was I, ere I saw Elba", True),
            ("No 'x' in Nixon", True),
            ("Was it a car or a cat I saw?", True),
            ("aba", True),
        ]
        for s, expected in test_data:
            with self.subTest(s=s):
                self.assertEqual(isPalindrome(s), expected)

    def test_non_palindromes(self):
        test_data = [
            ("race a car", False),
            ("ab", False),
            ("1a2b3c2b1a", False),
            ("1a2b3c4d5e", False),
            ("12345", False),
        ]
        for s, expected in test_data:
            with self.subTest(s=s):
                self.assertEqual(isPalindrome(s), expected)

    def test_empty_and_single_char(self):
        test_data = [
            ("", True),
            (" ", True),
            ("a", True),
        ]
        for s, expected in test_data:
            with self.subTest(s=s):
                self.assertEqual(isPalindrome(s), expected)

    def test_numeric_palindromes(self):
        test_data = [
            ("12321", True),
        ]
        for s, expected in test_data:
            with self.subTest(s=s):
                self.assertEqual(isPalindrome(s), expected)

if __name__ == "__main__":
    unittest.main()
