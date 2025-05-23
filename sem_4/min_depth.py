from build_tree import *

def minDepth(root):
    if root == None:
        return 0
    if (root.left == None) and (root.right==None):
        return 1
    
    if (root.left != None) and (root.right!=None):
        return 1+min(minDepth(root.left),minDepth(root.right))
    
    if(root.left!=None):
        return 1+minDepth(root.left)
    if (root.right!=None):
        return 1+minDepth(root.right)
    