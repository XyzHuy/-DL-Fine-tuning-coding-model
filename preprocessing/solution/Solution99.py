# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p == q:
        return True
    try:
        left = right = True
        if p.val == q.val:
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)
            return (left and right)
    except:
        return False
    return False
