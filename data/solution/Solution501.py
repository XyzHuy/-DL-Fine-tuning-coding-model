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
from collections import defaultdict
from typing import Optional, List

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(node):
            if node:
                yield from inorder_traversal(node.left)
                yield node.val
                yield from inorder_traversal(node.right)
        
        # Dictionary to store the frequency of each value
        frequency = defaultdict(int)
        
        # Perform inorder traversal to populate the frequency dictionary
        for value in inorder_traversal(root):
            frequency[value] += 1
        
        # Find the maximum frequency
        max_freq = max(frequency.values())
        
        # Collect all values with the maximum frequency
        modes = [key for key, count in frequency.items() if count == max_freq]
        
        return modes

def findMode(root: Optional[TreeNode]) -> List[int]:
    return Solution().findMode(root)