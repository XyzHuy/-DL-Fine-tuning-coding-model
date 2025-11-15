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
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return float('inf'), float('-inf'), 0  # min, max, size
            
            left_min, left_max, left_size = helper(node.left)
            right_min, right_max, right_size = helper(node.right)
            
            if left_max < node.val < right_min:
                return min(node.val, left_min), max(node.val, right_max), left_size + right_size + 1
            
            return float('-inf'), float('inf'), max(left_size, right_size)
        
        return helper(root)[2]

def largestBSTSubtree(root: Optional[TreeNode]) -> int:
    return Solution().largestBSTSubtree(root)