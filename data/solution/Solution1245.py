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
    def treeDiameter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            max_depth = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    max_depth = max(max_depth, dfs(neighbor, node) + 1)
            return max_depth
        
        # First DFS to find the farthest node from node 0
        _, farthest_node = max((dfs(node, -1), node) for node in range(len(edges) + 1))
        
        # Second DFS from the farthest node to find the diameter
        diameter = dfs(farthest_node, -1)
        
        return diameter

def treeDiameter(edges: List[List[int]]) -> int:
    return Solution().treeDiameter(edges)