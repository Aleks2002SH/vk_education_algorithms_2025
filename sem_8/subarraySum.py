
def subarraySum(nums,k):
    prefixSum = 0
    prefixCount = {0:1}
    count = 0
    for num in nums:
        prefixSum+=num
        if prefixSum-k in prefixCount:
            count += prefixCount[prefixSum-k]
        prefixCount[prefixSum] = prefixCount.get(prefixSum, 0) + 1
    return count