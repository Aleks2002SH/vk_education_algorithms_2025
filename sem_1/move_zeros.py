
def move_zeroes(nums):
    n = len(nums)
    non_zero_ind = 0
    for i in range(n):
        if nums[i]!=0:
            nums[i],nums[non_zero_ind] = nums[non_zero_ind],nums[i]
            non_zero_ind+=1
        