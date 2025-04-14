

def shell_sort(arr):
    n = len(arr)
    gap = len(arr)//2
    while gap>0:
        for cur_pos in range(gap,n):
            m_gap = cur_pos
            while m_gap>=gap and arr[m_gap]<arr[m_gap-gap]:
                arr[m_gap],arr[m_gap-gap] = arr[m_gap-gap],arr[m_gap]
                m_gap -= gap
        gap = gap//2
    return arr