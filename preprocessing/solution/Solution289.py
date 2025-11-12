# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    ans = 1
    def depth(node):
        if not node: return 0
        L = depth(node.left)
        R = depth(node.right)
        ans = max(ans, L+R+1)
        return max(L, R) + 1

    depth(root)
    # number of nodes - 1 = length
    return ans - 1
