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
from collections import deque
from typing import Optional

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            prev_val = None if level % 2 == 0 else float('inf')
            
            for _ in range(size):
                node = queue.popleft()
                
                # Check even-odd condition
                if level % 2 == 0:  # Even level
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                else:  # Odd level
                    if node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val):
                        return False
                
                # Update previous value
                prev_val = node.val
                
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Move to the next level
            level += 1
        
        return True

def isEvenOddTree(root: Optional[TreeNode]) -> bool:
    return Solution().isEvenOddTree(root)