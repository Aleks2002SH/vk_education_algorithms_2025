class Solution(object):
    def reverse(self,arr):
        left = 0
        right = len(arr)-1

        while left<right:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
            left+=1
            right-=1
        return arr
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums = self.reverse(nums)
        nums[:k] = self.reverse(nums[:k])
        nums[k:] = self.reverse(nums[k:])

