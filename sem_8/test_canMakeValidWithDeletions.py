from canMakeValidWithDeletions import canMakeValidWithDeletions
import unittest 

class TestCanMakeValidWithDeletions(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(canMakeValidWithDeletions("(()())", 2))

    def test_case_2(self):
        self.assertTrue(canMakeValidWithDeletions("((())", 1))

    def test_case_3(self):
        self.assertTrue(canMakeValidWithDeletions(")(", 2))

    def test_case_4(self):
        self.assertTrue(canMakeValidWithDeletions("(()", 1))

    def test_case_5(self):
        self.assertTrue(canMakeValidWithDeletions("()", 0))

    def test_case_6(self):
        self.assertTrue(canMakeValidWithDeletions("())(", 2))

    def test_case_7(self):
        self.assertTrue(canMakeValidWithDeletions("((((((((", 8))

    def test_case_8(self):
        self.assertFalse(canMakeValidWithDeletions("))))))))", 7))

    def test_case_9(self):
        self.assertTrue(canMakeValidWithDeletions("", 0))

    def test_case_10(self):
        self.assertTrue(canMakeValidWithDeletions("(((((())))))", 3))

if __name__ == '__main__':
    unittest.main()