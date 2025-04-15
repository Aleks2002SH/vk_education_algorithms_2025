def isMinHeap(arr):
    n = len(arr)
    for i in range(0, (n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        if (left < n) and (arr[i] > arr[left]):
            return False
        if (right < n) and (arr[i] > arr[right]):
            return False
    return True


def isMinHeap_tree(root):
    if root is None:
        return True

    Q = [root]
    shouldBeLeaf = False

    while Q:
        cur = Q.pop(0)

        if cur.left:
            if shouldBeLeaf or cur.left.data < cur.data:
                return False
            Q.append(cur.left)
        else:
            shouldBeLeaf = True

        if cur.right:
            if shouldBeLeaf or cur.right.data < cur.data:
                return False
            Q.append(cur.right)
        else:
            shouldBeLeaf = True

    return True
