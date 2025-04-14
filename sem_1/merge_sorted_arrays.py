
def merge(nums1, m, nums2, n):

    p1 = len(nums1)-len(nums2)-1
    p2 = len(nums2)-1
    p3 = len(nums1)-1

    while p2>=0:
        if (p1>=0) and (nums1[p1]>nums2[p2]):
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1
        
    return nums1






