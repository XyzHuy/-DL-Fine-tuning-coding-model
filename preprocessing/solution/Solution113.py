# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flatten(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    current = root
    stack = [root]
    while stack:
        node = stack.pop()
        appendNode(stack, node.right)
        appendNode(stack, node.left)
        if current != node:
            current.right = node
            current.left = None
            current = node

def appendNode(stack, node):
    if node:
        stack.append(node)