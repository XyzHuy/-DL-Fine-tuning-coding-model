
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    import sys
    return isValid_helper(root, -sys.maxsize - 1, sys.maxsize)

def isValid_helper(root, minVal, maxVal):
    if root is None:
        return True
    if root.val >= maxVal or root.val <= minVal:
        return False
    return isValid_helper(root.left, minVal, root.val) and isValid_helper(root.right, root.val, maxVal)
