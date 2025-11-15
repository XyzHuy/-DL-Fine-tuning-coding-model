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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def tree_sum(node):
            if not node:
                return 0
            return node.val + tree_sum(node.left) + tree_sum(node.right)
        
        def dfs(node):
            if not node:
                return 0
            current_sum = node.val + dfs(node.left) + dfs(node.right)
            self.max_product = max(self.max_product, current_sum * (total_sum - current_sum))
            return current_sum
        
        total_sum = tree_sum(root)
        self.max_product = 0
        dfs(root)
        
        return self.max_product % (10**9 + 7)

def maxProduct(root: Optional[TreeNode]) -> int:
    return Solution().maxProduct(root)