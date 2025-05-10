def findMaxLength(nums):
    prefixSum = 0
    maxLen = 0
    indexMap = {0:-1}

    for i in range(0,len(nums)):
        num = nums[i]

        if num == 0:
            prefixSum += -1
        else:
            prefixSum += 1
        
        if prefixSum in indexMap:
            maxLen = max(maxLen,i - indexMap[prefixSum])
        else:
            indexMap[prefixSum]=i
    
    return maxLen
        
