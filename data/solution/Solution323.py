import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Helper function to perform DFS
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor)
        
        # Create adjacency list for the graph
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Initialize visited array
        visited = [False] * n
        components = 0
        
        # Iterate through each node
        for node in range(n):
            if not visited[node]:
                dfs(node)
                components += 1
        
        return components

def countComponents(n: int, edges: List[List[int]]) -> int:
    return Solution().countComponents(n, edges)