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
from typing import Optional, List

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # Initialize a deque to keep track of the closest k values
        closest_values = deque()
        
        # Perform in-order traversal
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Process the current node
            if len(closest_values) < k:
                closest_values.append(node.val)
            else:
                # Compare the current node with the farthest value in the deque
                if abs(node.val - target) < abs(closest_values[0] - target):
                    closest_values.popleft()
                    closest_values.append(node.val)
                else:
                    # Since the BST is sorted in-order, no need to check further
                    return
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Start the in-order traversal from the root
        inorder(root)
        
        # Convert deque to list and return
        return list(closest_values)

def closestKValues(root: Optional[TreeNode], target: float, k: int) -> List[int]:
    return Solution().closestKValues(root, target, k)