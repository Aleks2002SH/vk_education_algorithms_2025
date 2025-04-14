from queue import Queue

def isMaxHeap(arr):
    n = len(arr)
    for i in range(0,(n-2)//2+1):
        left = 2*i+1
        right = 2*i+2
        if (left<n) and (arr[i]<arr[left]):
            return False
        if (right<n) and (arr[i]<arr[right]):
            return False 
        
    return True

def isMaxHeap_tree(root):
    if root is None:
        return True 
    Q = [root]
    shouldBeLeaf = False
    while len(Q)>0:
        cur = Q.pop(0)
        if cur.left!=None:
            if shouldBeLeaf or cur.left.data > cur.data:
                return False
            Q.append(cur.left)
        else:
            shouldBeLeaf = True
        
        if cur.right!=None:
            if shouldBeLeaf or cur.right.data > cur.data:
                return False
            Q.append(cur.right)
        else:
            shouldBeLeaf = True

    return True
