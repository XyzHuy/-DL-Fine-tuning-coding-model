import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Create an adjacency list for the graph
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        # Array to store color of each node (0: uncolored, 1: color1, -1: color2)
        color = [0] * (n + 1)
        
        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False
            return True
        
        # Try to color each component of the graph
        for i in range(1, n + 1):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        
        return True

def possibleBipartition(n: int, dislikes: List[List[int]]) -> bool:
    return Solution().possibleBipartition(n, dislikes)