def binarySearchSqrt(target):
    if target == 0:
        return 0
    
    l, r = 0, target
    while l <= r:
        mid = (l + r) // 2
        if mid ** 2 == target:
            return mid
        elif mid ** 2 < target:
            l = mid + 1
        else:
            r = mid - 1
    return r

