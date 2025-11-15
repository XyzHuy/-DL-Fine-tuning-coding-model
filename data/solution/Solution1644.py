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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findLCA(node):
            nonlocal found_p, found_q
            
            if not node:
                return None
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            # Check if current node is either p or q
            if node == p or node == q:
                if node == p:
                    found_p = True
                if node == q:
                    found_q = True
                return node
            
            # If both left and right are not None, current node is the LCA
            if left and right:
                return node
            
            return left if left else right
        
        found_p, found_q = False, False
        lca = findLCA(root)
        
        # Ensure both p and q are found in the tree
        if found_p and found_q:
            return lca
        else:
            return None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    return Solution().lowestCommonAncestor(root, p, q)