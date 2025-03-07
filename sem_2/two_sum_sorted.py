class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        while (left<right):
            sum_val = nums[left]+nums[right]
            if sum_val == target:
                return [left,right]
            elif sum_val<target:
                left += 1
            else:
                right-=1
        return []