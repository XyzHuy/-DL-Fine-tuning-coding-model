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
from typing import List, Optional
import heapq

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Dictionary to store the nodes' values by their (column, row)
        node_map = defaultdict(list)
        
        # Queue for BFS: stores tuples of (node, row, col)
        queue = [(root, 0, 0)]
        
        # Perform BFS to populate the node_map
        while queue:
            node, row, col = queue.pop(0)
            if node:
                # Use a heap to store values to maintain order by row and node value
                heapq.heappush(node_map[col], (row, node.val))
                # Add child nodes to the queue
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        # Extract the sorted column indices
        sorted_cols = sorted(node_map.keys())
        
        # Prepare the result list
        result = []
        for col in sorted_cols:
            # Extract and sort nodes by row first, then by value
            col_nodes = [heapq.heappop(node_map[col])[1] for _ in range(len(node_map[col]))]
            result.append(col_nodes)
        
        return result

def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    return Solution().verticalTraversal(root)