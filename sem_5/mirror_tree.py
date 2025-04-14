from build_tree import *
from queue import Queue

def mirrorTree(node):
    if node == None:
        return None
    node.left,node.right = node.right,node.left
    mirrorTree(node.left)
    mirrorTree(node.right)
    return node

def mirrorTreeIterative(node):
    if node == None:
        return None
    Q = [node]
    while len(Q)>0:
        cur = Q.pop(0)
        temp =cur.left
        cur.left = cur.right
        cur.right = temp

        if cur.left!=None:
            Q.append(cur.left)
        if cur.right!=None:
            Q.append(cur.right)
    return node
    