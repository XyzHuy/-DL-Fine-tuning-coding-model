import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create the graph
        graph = defaultdict(list)
        degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Find all leaves (nodes with degree 1)
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        # Trim the leaves until we are left with the cycle
        while leaves:
            leaf = leaves.popleft()
            degree[leaf] = 0
            for neighbor in graph[leaf]:
                if degree[neighbor] > 0:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        # All nodes with degree > 0 are part of the cycle
        cycle = [i for i in range(n) if degree[i] > 0]
        
        # Initialize the result array with -1
        result = [-1] * n
        
        # Set the distance to 0 for all nodes in the cycle
        for node in cycle:
            result[node] = 0
        
        # BFS from all nodes in the cycle to find the shortest distance to the cycle
        queue = deque(cycle)
        distance = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if result[neighbor] == -1:
                        result[neighbor] = distance + 1
                        queue.append(neighbor)
            distance += 1
        
        return result

def distanceToCycle(n: int, edges: List[List[int]]) -> List[int]:
    return Solution().distanceToCycle(n, edges)