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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def contains_one(node):
            if not node:
                return False
            
            # Recursively check left and right subtrees
            left_contains_one = contains_one(node.left)
            right_contains_one = contains_one(node.right)
            
            # Prune left subtree if it does not contain a 1
            if not left_contains_one:
                node.left = None
            
            # Prune right subtree if it does not contain a 1
            if not right_contains_one:
                node.right = None
            
            # Return True if the current node or any of its subtrees contain a 1
            return node.val == 1 or left_contains_one or right_contains_one
        
        # Call the helper function on the root
        return root if contains_one(root) else None

def pruneTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    return Solution().pruneTree(root)