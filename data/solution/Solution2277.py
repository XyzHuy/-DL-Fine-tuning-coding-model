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
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Build the adjacency list for the tree
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Helper function to perform DFS and find the path from start to end
        def find_path(start, end):
            stack = [(start, [start])]
            visited = set()
            while stack:
                node, path = stack.pop()
                if node == end:
                    return path
                if node not in visited:
                    visited.add(node)
                    for neighbor in adj_list[node]:
                        if neighbor not in visited:
                            stack.append((neighbor, path + [neighbor]))
            return []
        
        # Helper function to perform BFS and find shortest path distances from a given node
        def bfs_shortest_distances(start):
            distances = {i: float('inf') for i in range(n)}
            distances[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in adj_list[node]:
                    if distances[neighbor] == float('inf'):
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)
            return distances
        
        # Process each query
        result = []
        for start, end, node in query:
            path = find_path(start, end)
            shortest_distances = bfs_shortest_distances(node)
            closest_node = min(path, key=lambda x: shortest_distances[x])
            result.append(closest_node)
        
        return result

def closestNode(n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
    return Solution().closestNode(n, edges, query)