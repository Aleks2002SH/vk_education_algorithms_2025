from array_of_anagramms import create_array_of_anagramms

import unittest

class TestCreateArrayOfAnagramms(unittest.TestCase):
    
    def test_case_1(self):
        out = create_array_of_anagramms(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], key=sorted))

    def test_case_2(self):
        out = create_array_of_anagramms([""])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([[""]], key=sorted))

    def test_case_3(self):
        out = create_array_of_anagramms(["a", "b", "c", "a", "b", "c"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["a", "a"], ["b", "b"], ["c", "c"]], key=sorted))

    def test_case_4(self):
        out = create_array_of_anagramms(["dog", "god", "good", "dogg"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["dog", "god"], ["good"], ["dogg"]], key=sorted))

    def test_case_5(self):
        out = create_array_of_anagramms(["hello", "world", "llheo", "dorlw"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["hello", "llheo"], ["world", "dorlw"]], key=sorted))

    def test_case_6(self):
        out = create_array_of_anagramms(["abc", "acb", "bac", "cab", "cba"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["abc", "acb", "bac", "cab", "cba"]], key=sorted))

    def test_case_7(self):
        out = create_array_of_anagramms(["xyz", "zyx", "yxz", "a", "b", "c"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["xyz", "zyx", "yxz"], ["a"], ["b"], ["c"]], key=sorted))

    def test_case_8(self):
        out = create_array_of_anagramms(["abcd", "dabc", "abdc", "cdab"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["abcd", "dabc", "abdc", "cdab"]], key=sorted))

    def test_case_9(self):
        out = create_array_of_anagramms(["apple", "pale", "peal", "leap", "bake"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["apple"], ["pale", "peal", "leap"], ["bake"]], key=sorted))

    def test_case_10(self):
        out = create_array_of_anagramms(["aab", "aba", "baa", "abc", "bca", "cab"])
        self.assertEqual(sorted(out, key=sorted), 
                         sorted([["aab", "aba", "baa"], ["abc", "bca", "cab"]], key=sorted))

if __name__ == '__main__':
    unittest.main()
