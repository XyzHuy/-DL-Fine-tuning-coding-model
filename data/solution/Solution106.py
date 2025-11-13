# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrderBottom( root):
    if root is None:
        return []
    # use stack
    stack = [[root]]
    res = []
    while len(stack) > 0:
        top = stack.pop()
        res.insert(0, [t.val for t in top])
        temp = []
        for node in top:
            if node.left is not None:
                temp.append(node.left)
            if node.right is not None:
                temp.append(node.right)
        if len(temp) > 0:
            stack.append(temp)
    return res
