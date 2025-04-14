class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.data = val
        self.left = left
        self.right = right

def buildTree(arr,i):
    if i>=len(arr) or arr[i]==None:
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr,2*i+1)
    root.right = buildTree(arr,2*i+2)
    return root

def depthTraversal(root,res):
    if root == None:
        return res
    depthTraversal(root.left,res)
    res.append(root.data)
    depthTraversal(root.right,res)
    return res
