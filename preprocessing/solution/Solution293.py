# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    s_res = preorder(s, True)
    t_res = preorder(t, True)
    return t_res in s_res

def preorder(root, isLeft):
    if root is None:
        if isLeft:
            return "lnull"
        else:
            return "rnull"
    return "#" + str(root.val) + " " + preorder(root.left, True) + " " + preorder(root.right, False)