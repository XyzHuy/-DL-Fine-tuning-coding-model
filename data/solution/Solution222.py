# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestConsecutive(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return longestConsecutive_helper(root, -10000, 1)

def longestConsecutive_helper(root, previous, curr):
    # Top down recursion
    if root is None:
        return 0
    if root.val - 1 == previous:
        curr += 1
    else:
        curr = 1
    l_res = longestConsecutive_helper(root.left, root.val, curr)
    r_res = longestConsecutive_helper(root.right, root.val, curr)
    return max(curr, l_res, r_res)
