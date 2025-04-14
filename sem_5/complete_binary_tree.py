from build_tree import *
from queue import Queue

def isCompleteTree(root):
    if root == None:
        return True
    Q = [root]
    seenNull = False
    while len(Q)>0:
        node = Q.pop(0)
        if node == None:
            seenNull = True
        else:
            if seenNull:
                return False
            Q.append(node.left)
            Q.append(node.right)
    return True
    