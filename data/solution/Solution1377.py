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
from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to calculate the probability
        queue = deque([(1, 1.0, 0)])  # (current node, current probability, current time)
        visited = set([1])
        
        while queue:
            current, prob, time = queue.popleft()
            
            # Get all unvisited neighbors
            neighbors = [neighbor for neighbor in graph[current] if neighbor not in visited]
            num_neighbors = len(neighbors)
            
            # If we reach the target
            if current == target:
                # If we have no more time or no more neighbors to jump to
                if time == t or not neighbors:
                    return prob
                else:
                    return 0.0
            
            # If we run out of time but haven't reached the target
            if time == t:
                continue
            
            # Explore neighbors
            for neighbor in neighbors:
                visited.add(neighbor)
                queue.append((neighbor, prob / num_neighbors, time + 1))
        
        return 0.0

def frogPosition(n: int, edges: List[List[int]], t: int, target: int) -> float:
    return Solution().frogPosition(n, edges, t, target)