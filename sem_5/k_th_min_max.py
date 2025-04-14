from build_tree import *

def inorderMin(node,k,cnt):
    if node is None:
        return None
    
    leftRes = inorderMin(node.left,k,cnt)

    if leftRes is not None:
        return leftRes
    cnt[0]+=1
    if cnt[0] == k:
        return node.data
    return inorderMin(node.right,k,cnt)

def inorderMax(node,k,cnt):
    if node is None:
        return None
    
    rightRes = inorderMax(node.right,k,cnt)

    if rightRes is not None:
        return rightRes
    cnt[0]+=1
    if cnt[0] == k:
        return node.data
    return inorderMax(node.left,k,cnt)

def inorderMinIterative(node,k):
    stack = []
    cnt = 0
    cur = node
    while len(stack)>0 or cur != None:
        while cur != None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        cnt+=1
        if cnt == k:
            return cur.data
        cur = cur.right
    return None

def inorderMaxIterative(node,k):
    stack = []
    cnt = 0
    cur = node
    while len(stack)>0 or cur != None:
        while cur != None:
            stack.append(cur)
            cur = cur.right
        cur = stack.pop()
        cnt+=1
        if cnt == k:
            return cur.data
        cur = cur.left
    return None