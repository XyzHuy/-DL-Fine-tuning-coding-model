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
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # Build the adjacency list for the tree
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize the total fuel cost
        total_fuel = 0
        
        # Depth-first search to calculate the fuel cost
        def dfs(node: int, parent: int) -> int:
            nonlocal total_fuel
            representatives = 1  # Start with the representative from the current city
            
            # Visit all the neighboring cities
            for neighbor in graph[node]:
                if neighbor != parent:
                    # Recursively count the representatives from the subtree
                    representatives_from_child = dfs(neighbor, node)
                    # Calculate the fuel cost for the trip to the current city
                    total_fuel += (representatives_from_child + seats - 1) // seats  # Equivalent to ceil(representatives_from_child / seats)
                    # Add the representatives from the subtree to the current count
                    representatives += representatives_from_child
            
            return representatives
        
        # Start DFS from the capital city (city 0)
        dfs(0, -1)
        
        return total_fuel

def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    return Solution().minimumFuelCost(roads, seats)