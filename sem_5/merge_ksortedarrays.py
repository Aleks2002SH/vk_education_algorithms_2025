from build_tree import *

def mergeKSortedArrays(sortedArrays):
    mergedArray = []

    minHeap = MinHeap_ksorted()
    for i in range(0,len(sortedArrays)):
        curArr = sortedArrays[i]
        if len(curArr)>0:
            minHeap.heappush(curArr[0],i,0)
    while not minHeap.is_empty():
        val,arrIdx,elIdx = minHeap.heappop()
        mergedArray.append(val)
        if elIdx+1 < len(sortedArrays[arrIdx]):
            next_el = sortedArrays[arrIdx][elIdx+1]
            minHeap.heappush(next_el,arrIdx,elIdx+1)
    return mergedArray
    

