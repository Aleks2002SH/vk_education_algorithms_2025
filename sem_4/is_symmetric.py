from build_tree import *

def isSymmetricBFS(root):
    if root == None:
        return True
    Q = [root]
    while len(Q)>0:
        Q_len = len(Q)
        for i in range(Q_len):
            if (Q[i]==None) and (Q[Q_len-i-1]==None):
                continue
            if (Q[i]==None) or (Q[Q_len-i-1]==None):
                return False
            if (Q[i].data!=Q[Q_len-i-1].data):
                return False
            Q.append(Q[i].left)
            Q.append(Q[i].right)
        Q = Q[Q_len:]
    return True

def isSymmetricDFS(root):
    if root == None:
        return True
    data = []
    data = depthTraversal(root,data)
    j = len(data)-1
    for i in range(0,len(data)//2):
        if data[i]!=data[j]:
            return False
        j-=1
    return True
