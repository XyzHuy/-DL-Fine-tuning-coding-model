# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    if n == 0:
        return []
    return get_trees(1, n)

def get_trees(start, end):
    # recursive solve this problem
    res = []
    if start > end:
        res.append(None)
        return res
    for i in range(start, end + 1):
        lefts = get_trees(start, i - 1)
        rights = get_trees(i + 1, end)
        for j in range(len(lefts)):
            for k in range(len(rights)):
                # root point
                root = TreeNode(i)
                root.left = lefts[j]
                root.right = rights[k]
                res.append(root)
    return res