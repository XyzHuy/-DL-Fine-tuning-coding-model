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
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import defaultdict, deque
        
        # Build the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Convert restricted list to a set for O(1) lookups
        restricted_set = set(restricted)
        
        # Initialize BFS
        queue = deque([0])
        visited = set([0])
        
        # Perform BFS
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited and neighbor not in restricted_set:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # The number of visited nodes is the answer
        return len(visited)

def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    return Solution().reachableNodes(n, edges, restricted)