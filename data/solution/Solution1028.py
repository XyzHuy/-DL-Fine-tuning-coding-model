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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def parse(traversal, index, depth):
            if index >= len(traversal):
                return None, index
            
            # Calculate the current depth based on dashes
            current_depth = 0
            while index < len(traversal) and traversal[index] == '-':
                current_depth += 1
                index += 1
            
            # If the current depth does not match the expected depth, return None
            if current_depth != depth:
                return None, index - current_depth
            
            # Parse the node value
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            
            # Create the current node
            node = TreeNode(value)
            
            # Recursively parse the left and right children
            node.left, index = parse(traversal, index, depth + 1)
            node.right, index = parse(traversal, index, depth + 1)
            
            return node, index
        
        root, _ = parse(traversal, 0, 0)
        return root

def recoverFromPreorder(traversal: str) -> Optional[TreeNode]:
    return Solution().recoverFromPreorder(traversal)