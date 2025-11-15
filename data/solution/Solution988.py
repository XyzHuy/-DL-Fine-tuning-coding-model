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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return None
            
            # Convert node value to corresponding character
            path = chr(ord('a') + node.val) + path
            
            # If it's a leaf node, return the path
            if not node.left and not node.right:
                return path
            
            # Recur for left and right children
            left_path = dfs(node.left, path)
            right_path = dfs(node.right, path)
            
            # Return the lexicographically smaller path
            if left_path and right_path:
                return min(left_path, right_path)
            elif left_path:
                return left_path
            else:
                return right_path
        
        return dfs(root, "")

def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    return Solution().smallestFromLeaf(root)