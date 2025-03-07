import pytest
from isPalyndrome import Solution  

@pytest.mark.parametrize(
    "s, expected", [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        ("a", True),
        ("ab", False),
        ("aba", True),
        ("Able was I, ere I saw Elba", True),
        ("No 'x' in Nixon", True),
        ("Was it a car or a cat I saw?", True),
        ("12321", True),
        ("12345", False),
        ("1a2b3c2b1a", False),
        ("1a2b3c4d5e", False)
    ]
)
def test_is_palindrome(s, expected):
    solution = Solution()
    assert solution.isPalindrome(s) == expected

