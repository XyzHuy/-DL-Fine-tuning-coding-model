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
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        
        # Dictionary to hold the mapping from original nodes to their copies
        self.node_map = {}
        
        # Helper function to perform the deep copy
        def copy_node(node):
            if not node:
                return None
            if node in self.node_map:
                return self.node_map[node]
            
            # Create a new node copy and store it in the map
            node_copy = NodeCopy(node.val)
            self.node_map[node] = node_copy
            
            # Recursively copy the left, right and random pointers
            node_copy.left = copy_node(node.left)
            node_copy.right = copy_node(node.right)
            node_copy.random = copy_node(node.random)
            
            return node_copy
        
        # Start the deep copy from the root
        return copy_node(root)

def copyRandomBinaryTree(root: 'Optional[Node]') -> 'Optional[NodeCopy]':
    return Solution().copyRandomBinaryTree(root)