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
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Initialize the count of valid components
        valid_components = 0
        
        # Define the DFS function
        def dfs(node, parent):
            nonlocal valid_components
            # Start with the value of the current node
            total = values[node]
            for neighbor in tree[node]:
                if neighbor != parent:
                    # Recursively calculate the sum of the subtree
                    total += dfs(neighbor, node)
            
            # If the total value of the subtree is divisible by k, it's a valid component
            if total % k == 0:
                valid_components += 1
                # Return 0 to indicate that this subtree is already counted as a valid component
                return 0
            else:
                # Otherwise, return the total value to be part of the parent's subtree
                return total
        
        # Start DFS from node 0 (or any node, as it's a tree)
        dfs(0, -1)
        
        return valid_components

def maxKDivisibleComponents(n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    return Solution().maxKDivisibleComponents(n, edges, values, k)