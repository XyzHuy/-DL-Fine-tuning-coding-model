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
from typing import Optional, List

class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, index):
            # If node is None or index is out of bounds or values do not match
            if not node or index >= len(arr) or node.val != arr[index]:
                return False
            
            # If we are at the last element of the array and it matches the leaf node
            if index == len(arr) - 1 and not node.left and not node.right:
                return True
            
            # Continue the search on the left and right subtree
            return dfs(node.left, index + 1) or dfs(node.right, index + 1)
        
        return dfs(root, 0)

def isValidSequence(root: Optional[TreeNode], arr: List[int]) -> bool:
    return Solution().isValidSequence(root, arr)