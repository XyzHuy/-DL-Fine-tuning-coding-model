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
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def findLCA(node):
            if not node or node.val == p or node.val == q:
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if left and right:
                return node
            return left or right
        
        def findDistanceFromNode(node, target, depth=0):
            if not node:
                return -1
            if node.val == target:
                return depth
            left = findDistanceFromNode(node.left, target, depth + 1)
            if left != -1:
                return left
            return findDistanceFromNode(node.right, target, depth + 1)
        
        lca = findLCA(root)
        distance_p = findDistanceFromNode(lca, p)
        distance_q = findDistanceFromNode(lca, q)
        
        return distance_p + distance_q

def findDistance(root: Optional[TreeNode], p: int, q: int) -> int:
    return Solution().findDistance(root, p, q)