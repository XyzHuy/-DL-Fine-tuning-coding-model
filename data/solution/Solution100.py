# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    return mirrorVisit(root.left, root.right)

def mirrorVisit(left, right):
    if left is None and right is None:
        return True
    try:
        if left.val == right.val:
            if mirrorVisit(left.left, right.right) and mirrorVisit(left.right, right.left):
                return True
        return False
    except:
        return False