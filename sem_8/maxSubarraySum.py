def maxSubarraySum(arr,k):
    if len(arr)<k:
        return None
    
    cur_sum = 0
    for i in range(k):
        cur_sum += arr[i]
    
    max_sum = cur_sum 
    for i in range(k,len(arr)):
        cur_sum = cur_sum-arr[i-k]+arr[i]
        max_sum = max(max_sum,cur_sum)

    return max_sum