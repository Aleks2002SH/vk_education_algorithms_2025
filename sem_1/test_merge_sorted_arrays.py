import unittest
from merge_sorted_arrays import merge 

class TestMergeSortedArrays(unittest.TestCase):

    def check_merge(self, nums1, m, nums2, n, expected):
        nums1_copy = nums1[:]  
        merge(nums1_copy, m, nums2, n)
        self.assertEqual(nums1_copy, expected)

    def test_merges(self):
        cases = [
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1]),
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([2, 0], 1, [1], 1, [1, 2]),
        ]
        for nums1, m, nums2, n, expected in cases:
            
            self.check_merge(nums1, m, nums2, n, expected)

    def test_already_sorted(self):
        cases = [
            ([1, 2, 3, 0, 0, 0, 0], 3, [4, 5, 6, 7], 4, [1, 2, 3, 4, 5, 6, 7]),
            ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
            ([1, 4, 7, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 4, 5, 6, 7]),
            ([5, 6, 7, 8, 9, 0, 0], 5, [1, 10], 2, [1, 5, 6, 7, 8, 9, 10]),
        ]
        for nums1, m, nums2, n, expected in cases:
            self.check_merge(nums1, m, nums2, n, expected)

    def test_overlapping_and_duplicates(self):
        cases = [
            ([2, 2, 2, 0, 0, 0], 3, [2, 2, 2], 3, [2, 2, 2, 2, 2, 2]),
            ([3, 3, 3, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 3, 3, 3]),
            ([4, 9, 10, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 9, 10]),
            ([7, 8, 9, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 7, 8, 9]),
        ]
        for nums1, m, nums2, n, expected in cases:  
            self.check_merge(nums1, m, nums2, n, expected)

if __name__ == '__main__':
    unittest.main()