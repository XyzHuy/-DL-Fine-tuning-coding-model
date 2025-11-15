import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # If the destination node has outgoing edges, it cannot be a destination
        if graph[destination]:
            return False
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        states = [0] * n
        
        def dfs(node):
            if states[node] == 1:  # Cycle detected
                return False
            if states[node] == 2:  # Node already visited and valid
                return True
            if not graph[node]:  # If there are no outgoing edges, it must be the destination
                return node == destination
            
            states[node] = 1  # Mark node as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            states[node] = 2  # Mark node as visited
            return True
        
        return dfs(source)

def leadsToDestination(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    return Solution().leadsToDestination(n, edges, source, destination)