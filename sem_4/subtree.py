from build_tree import *
from same_trees import isSameTree

def isSubtree(a,b):
    if b == None:
        return True
    if a == None:
        return False
    if (isSameTree(a,b)):
        return True
    
    return isSubtree(a.left,b) or isSubtree(a.right,b)
