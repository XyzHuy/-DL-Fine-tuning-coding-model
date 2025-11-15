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
from collections import deque, defaultdict
from typing import Optional, List

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Dictionary to store nodes' values by their column index
        column_table = defaultdict(list)
        
        # Queue to perform BFS; each element is a tuple (node, column_index)
        queue = deque([(root, 0)])
        
        # Track the range of column indices
        min_col = max_col = 0
        
        while queue:
            node, column_index = queue.popleft()
            
            if node is not None:
                # Update the range of column indices
                min_col = min(min_col, column_index)
                max_col = max(max_col, column_index)
                
                # Append the node's value to the corresponding column
                column_table[column_index].append(node.val)
                
                # Add the node's children to the queue with updated column indices
                queue.append((node.left, column_index - 1))
                queue.append((node.right, column_index + 1))
        
        # Collect the results column by column, from min_col to max_col
        return [column_table[x] for x in range(min_col, max_col + 1)]

def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    return Solution().verticalOrder(root)