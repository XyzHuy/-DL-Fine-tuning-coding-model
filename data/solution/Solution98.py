# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

first = second = None
pre = TreeNode(-sys.maxsize - 1)


def recoverTree(root):
    global first, second
    traverse(root)
    first.val, second.val = second.val, first.val

def traverse(root):
    global first, second, pre
    if root is None:
        return
    traverse(root.left)
    if pre.val >= root.val:
        if first is None:
            first = pre
        if first is not None:
            second = root
    pre = root
    traverse(root.right)
