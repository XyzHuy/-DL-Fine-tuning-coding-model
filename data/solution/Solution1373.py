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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            is_left_bst, left_min, left_max, left_sum = dfs(node.left)
            is_right_bst, right_min, right_max, right_sum = dfs(node.right)
            
            if is_left_bst and is_right_bst and left_max < node.val < right_min:
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)
                return True, min(node.val, left_min), max(node.val, right_max), current_sum
            
            return False, float('-inf'), float('inf'), 0
        
        self.max_sum = 0
        dfs(root)
        return self.max_sum

def maxSumBST(root: Optional[TreeNode]) -> int:
    return Solution().maxSumBST(root)