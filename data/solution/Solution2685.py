import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Helper function to perform DFS and find all nodes in the connected component
        def dfs(node):
            if node in visited:
                return []
            visited.add(node)
            component = [node]
            for neighbor in graph[node]:
                component.extend(dfs(neighbor))
            return component
        
        visited = set()
        complete_components = 0
        
        # Iterate over all nodes
        for node in range(n):
            if node not in visited:
                # Find all nodes in the current connected component
                component = dfs(node)
                k = len(component)
                # Check if the component is complete
                if all(len(graph[node]) == k - 1 for node in component):
                    complete_components += 1
        
        return complete_components

def countCompleteComponents(n: int, edges: List[List[int]]) -> int:
    return Solution().countCompleteComponents(n, edges)