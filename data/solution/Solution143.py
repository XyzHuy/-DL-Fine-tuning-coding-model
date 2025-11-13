# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def postorderTraversal(root):
    if root is None:
        return []
    res = []; stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        if not isinstance(curr, TreeNode):
            res.append(curr)
            continue
        stack.append(curr.val)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return res
