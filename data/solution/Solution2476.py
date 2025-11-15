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
from typing import List, Optional
from bisect import bisect_left, bisect_right

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # Perform in-order traversal to get a sorted list of node values
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        sorted_values = in_order_traversal(root)
        
        def find_closest_values(query):
            # Find the largest value <= query
            i = bisect_right(sorted_values, query)
            mini = sorted_values[i - 1] if i > 0 else -1
            
            # Find the smallest value >= query
            j = bisect_left(sorted_values, query)
            maxi = sorted_values[j] if j < len(sorted_values) else -1
            
            return [mini, maxi]
        
        return [find_closest_values(query) for query in queries]

def closestNodes(root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
    return Solution().closestNodes(root, queries)