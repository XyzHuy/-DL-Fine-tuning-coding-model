import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # If there are fewer than n-1 cables, we cannot connect all computers
        if len(connections) < n - 1:
            return -1
        
        # Create adjacency list for the graph
        graph = {i: [] for i in range(n)}
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        # DFS function to visit all nodes in a connected component
        def dfs(node, visited):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
        
        # Set to keep track of visited nodes
        visited = set()
        # Number of connected components
        components = 0
        
        # Traverse each node and perform DFS if it hasn't been visited
        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                components += 1
        
        # The number of operations needed is the number of components minus one
        return components - 1

def makeConnected(n: int, connections: List[List[int]]) -> int:
    return Solution().makeConnected(n, connections)