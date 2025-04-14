import unittest
from sort_colors import sortColors

class TestSortColors(unittest.TestCase):
    def check_sortColors(self,nums,expected):
        sortColors(nums)
        self.assertEqual(nums, expected)

    def test_basic(self):
        cases = [
        ([2, 0, 1], [0, 1, 2]),
        ([0, 1, 2], [0, 1, 2]),
        ([1, 0, 2], [0, 1, 2]),
        ([1, 2, 0], [0, 1, 2]),
        ([1, 2, 0], [0, 1, 2]),
        ([2, 1, 0], [0, 1, 2]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ]
        for nums,expected in cases:
            self.check_sortColors(nums,expected)
    
    def test_short(self):
        cases  = [
        ([1, 0], [0, 1]),
        ([0], [0]),
        ([1], [1]),
        ([2], [2]),
        ]
        for nums,expected in cases:
            self.check_sortColors(nums,expected)
    
    def test_long(self):
        cases = [
         ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
       
        ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),
      
        ([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2]),
        
        ([0, 1, 0, 2, 1, 2], [0, 0, 1, 1, 2, 2]),
        
        ]
        for nums,expected in cases:
            self.check_sortColors(nums,expected)

if __name__ == '__main__':
    unittest.main()
