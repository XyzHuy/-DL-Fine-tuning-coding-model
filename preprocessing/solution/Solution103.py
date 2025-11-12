# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    ld = maxDepth(root.left)
    rd = maxDepth(root.right)
    return 1 + max(ld, rd)
