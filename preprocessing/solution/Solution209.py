# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def closestValue(root, target):
    # compare kids' result with root
    kid = root.left if target < root.val else root.right
    if not kid:
        return root.val
    kid_min = closestValue(kid, target)
    return min((kid_min, root.val), key=lambda x: abs(target - x))
