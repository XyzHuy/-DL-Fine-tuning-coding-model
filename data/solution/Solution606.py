import random
import functools
import collections
import string
import math
import datetime


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: list):
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return ""
            
            # Start with the node's value
            result = str(node.val)
            
            # If there is a left child, process it
            if node.left:
                result += "(" + preorder(node.left) + ")"
            # If there is no left child but there is a right child, we need empty parentheses
            elif node.right:
                result += "()"
            
            # If there is a right child, process it
            if node.right:
                result += "(" + preorder(node.right) + ")"
            
            return result
        
        return preorder(root)

def tree2str(root: Optional[TreeNode]) -> str:
    return Solution().tree2str(root)