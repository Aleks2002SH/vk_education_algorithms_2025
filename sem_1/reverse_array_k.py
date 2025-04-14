
def reverse(arr):
    left = 0
    right = len(arr)-1

    while left<right:
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp
        left+=1
        right-=1
    return arr
def rotate( nums, k):
    n = len(nums)
    k = k%n
    nums = reverse(nums)
    nums[:k] = reverse(nums[:k])
    nums[k:] = reverse(nums[k:])

