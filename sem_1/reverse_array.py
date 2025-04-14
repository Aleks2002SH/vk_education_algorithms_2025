def reverse(arr):
    left = 0
    right = len(arr)-1

    while left<right:
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp
        left+=1
        right-=1
        