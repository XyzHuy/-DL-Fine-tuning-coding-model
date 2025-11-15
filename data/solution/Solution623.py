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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            # If depth is 1, we need to add a new root with the given value
            return TreeNode(val=val, left=root, right=None)
        
        # Use a queue to perform level order traversal
        queue = deque([root])
        current_depth = 1
        
        while queue:
            # If we reached the level just before the target depth, add new nodes
            if current_depth == depth - 1:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    # Insert new nodes with the given value
                    node.left = TreeNode(val=val, left=node.left, right=None)
                    node.right = TreeNode(val=val, left=None, right=node.right)
            else:
                # Otherwise, continue traversing the tree level by level
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            current_depth += 1
        
        return root

def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    return Solution().addOneRow(root, val, depth)