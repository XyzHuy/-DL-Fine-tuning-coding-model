# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findLeaves(root):
    res = []
    findLeaves_helper(root, res)
    return res

def findLeaves_helper(node, res):
    if node is None:
        return -1
    level = 1 + max(findLeaves_helper(node.left, res), findLeaves_helper(node.right, res))
    if len(res) < level + 1:
        res.append([])
    res[level].append(node.val)
    return level
