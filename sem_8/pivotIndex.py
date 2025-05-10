def pivotIndex(nums):
    totalSum = 0
    leftSum = 0

    for i in range(len(nums)):
        totalSum += nums[i]
    
    for i in range(len(nums)):
        if leftSum == totalSum-leftSum-nums[i]:
            return i
        leftSum += nums[i]
    return -1