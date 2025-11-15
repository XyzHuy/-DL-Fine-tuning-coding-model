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
from collections import defaultdict

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        graph = defaultdict(set)
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)
        
        # Find the node with the maximum degree, which should be the root
        max_degree = max(graph, key=lambda x: len(graph[x]))
        n = len(graph)
        
        # If the number of neighbors of the root is not n-1, there is no valid tree
        if len(graph[max_degree]) != n - 1:
            return 0
        
        # Initialize the result to 1 (we assume there is at least one valid way)
        result = 1
        
        # Process each node in the graph
        for node in graph:
            if node == max_degree:
                continue
            
            # Find the parent of the current node
            parent = None
            for neighbor in graph[node]:
                if len(graph[neighbor]) >= len(graph[node]):
                    if parent is None or len(graph[neighbor]) > len(graph[parent]):
                        parent = neighbor
            
            # If no valid parent is found, return 0
            if parent is None:
                return 0
            
            # Check if the current node can be a child of the parent
            if any(child != parent and child not in graph[parent] for child in graph[node]):
                return 0
            
            # If the current node can have multiple parents, there are multiple ways to form the tree
            if len(graph[node]) == len(graph[parent]):
                result = 2
        
        return result

def checkWays(pairs: List[List[int]]) -> int:
    return Solution().checkWays(pairs)