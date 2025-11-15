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
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        def find_x(node):
            if not node:
                return None
            if node.val == x:
                return node
            left = find_x(node.left)
            if left:
                return left
            return find_x(node.right)
        
        # Find the node with value x
        x_node = find_x(root)
        
        # Count nodes in the left and right subtree of x
        left_count = count_nodes(x_node.left)
        right_count = count_nodes(x_node.right)
        
        # The rest of the tree (parent's side)
        parent_count = n - (left_count + right_count + 1)
        
        # Check if any of the three parts can be larger than the sum of the other two
        return (left_count > n - left_count or
                right_count > n - right_count or
                parent_count > n - parent_count)

def btreeGameWinningMove(root: Optional[TreeNode], n: int, x: int) -> bool:
    return Solution().btreeGameWinningMove(root, n, x)