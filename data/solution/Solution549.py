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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            
            inc = dec = 1  # At least the node itself
            
            if node.left:
                left_inc, left_dec = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = left_dec + 1
                elif node.val == node.left.val - 1:
                    inc = left_inc + 1
            
            if node.right:
                right_inc, right_dec = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, right_dec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, right_inc + 1)
            
            self.max_len = max(self.max_len, inc + dec - 1)
            return inc, dec
        
        self.max_len = 0
        dfs(root)
        return self.max_len

def longestConsecutive(root: Optional[TreeNode]) -> int:
    return Solution().longestConsecutive(root)