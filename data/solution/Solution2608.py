import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict, deque

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(start):
            # Distance array to keep track of the shortest distance from start node
            dist = [-1] * n
            # Parent array to keep track of the parent node
            parent = [-1] * n
            dist[start] = 0
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if dist[neighbor] == -1:  # Not visited
                        dist[neighbor] = dist[node] + 1
                        parent[neighbor] = node
                        queue.append(neighbor)
                    elif parent[node] != neighbor and parent[neighbor] != node:
                        # Found a back edge
                        return dist[node] + dist[neighbor] + 1
            return float('inf')
        
        min_cycle_length = float('inf')
        for i in range(n):
            cycle_length = bfs(i)
            min_cycle_length = min(min_cycle_length, cycle_length)
        
        return min_cycle_length if min_cycle_length < float('inf') else -1

def findShortestCycle(n: int, edges: List[List[int]]) -> int:
    return Solution().findShortestCycle(n, edges)