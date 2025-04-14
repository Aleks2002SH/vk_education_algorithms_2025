from build_tree import *


def dfs(left,right):
    if (left == None) or (right == None):
        return 0
    if left.data == None or right.data==None:
        return 0
    cnt = 0

    if left.data == right.data:
        cnt=1
    
    cnt+=dfs(left.left,right.right)
    cnt+=dfs(left.right,right.left)
    return cnt

def CountMirrorTwins(root):
    if root == None:
        return 0
    return dfs(root.left,root.right)