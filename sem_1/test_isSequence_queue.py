import pytest
from isSequence_queue import Solution  

@pytest.mark.parametrize(
    "s, t, expected", [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "ahbgdc", True),
        ("abc", "", False),
        ("ace", "abcde", True),
        ("aec", "abcde", False),
        ("aaa", "aaaaaa", True),
        ("aab", "aabbcc", True),
        ("aab", "abacadaeafagaha", False),
        ("aab", "abacadaeafagahb", True),
        ("ab", "aabbcc", True),
        ("ab", "ababababab", True),
        ("ab", "bababababab", True),
        ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba", False),
        ("a" * 100, "a" * 500, True),
        ("a" * 100, "b" * 100, False)
    ]
)

   
def test_is_subsequence(s, t, expected):
    solution = Solution()
    assert solution.isSubsequence(s, t) == expected