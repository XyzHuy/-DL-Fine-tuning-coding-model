# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root is None:
        return False
    sum = sum - root.val
    if sum == 0 and root.left is None and root.right is None:
        return True
    # check left
    left = hasPathSum(root.left, sum)
    # check right
    right = hasPathSum(root.right, sum)
    return (left or right)
