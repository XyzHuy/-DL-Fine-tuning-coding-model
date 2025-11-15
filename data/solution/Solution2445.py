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
from typing import List

class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        # Use a set to track the nodes that need to be flipped
        flip = set()
        
        # For each query, flip the node by adding or removing it from the set
        for query in queries:
            if query in flip:
                flip.remove(query)
            else:
                flip.add(query)
        
        # Initialize the count of nodes with value 1
        count_ones = 0
        
        # Function to perform DFS and count the nodes with value 1
        def dfs(node: int, flipped: bool) -> None:
            nonlocal count_ones
            
            # Flip the current node if it is in the flip set
            if node in flip:
                flipped = not flipped
            
            # Count the node if it has value 1
            if flipped:
                count_ones += 1
            
            # Calculate the left and right children
            left_child = node * 2
            right_child = node * 2 + 1
            
            # Perform DFS on the left child if it exists
            if left_child <= n:
                dfs(left_child, flipped)
            
            # Perform DFS on the right child if it exists
            if right_child <= n:
                dfs(right_child, flipped)
        
        # Start DFS from the root node (1) with initial flipped state as False
        dfs(1, False)
        
        return count_ones

def numberOfNodes(n: int, queries: List[int]) -> int:
    return Solution().numberOfNodes(n, queries)