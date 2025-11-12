# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # Bottom-up recursion with sentinel -1
    if root is None:
        return True
    if getDepth(root) < 0:
        return False
    return True

def getDepth(node):
    if node is None:
        return 1
    ld = getDepth(node.left)
    if ld < 0:
        return -1
    rd = getDepth(node.right)
    if rd < 0:
        return -1
    elif abs(ld - rd) > 1:
        return -1
    else:
        return max(ld, rd) + 1