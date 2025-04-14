from build_tree import *

def calculateHeightAndBalance(node):
    if node == None:
        return 0
    
    leftHeight = calculateHeightAndBalance(node.left)
    rightHeight = calculateHeightAndBalance(node.right)
    node.balanceFactor = leftHeight-rightHeight
    return 1 + max(leftHeight,rightHeight)
