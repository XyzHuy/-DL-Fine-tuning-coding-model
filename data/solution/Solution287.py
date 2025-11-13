# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convertBST(root):
    total = 0

    node = root
    stack = []
    while stack or node is not None:
        # push all nodes up to (and including) this subtree's maximum on
        # the stack.
        while node is not None:
            stack.append(node)
            node = node.right

        node = stack.pop()
        total += node.val
        node.val = total

        # all nodes with values between the current and its parent lie in
        # the left subtree.
        node = node.left

    return root
