import heapq
import itertools
from sortedcontainers import SortedList
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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, current_sum):
            if not node:
                return None
            
            # Calculate the new sum including the current node's value
            current_sum += node.val
            
            # If it's a leaf node, check if the path sum meets the limit
            if not node.left and not node.right:
                return node if current_sum >= limit else None
            
            # Recursively check left and right subtrees
            node.left = dfs(node.left, current_sum)
            node.right = dfs(node.right, current_sum)
            
            # If both left and right subtrees are pruned, prune this node as well
            return node if node.left or node.right else None
        
        return dfs(root, 0)

def sufficientSubset(root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
    return Solution().sufficientSubset(root, limit)