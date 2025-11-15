import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Step 1: Create adjacency list for the graph
        graph = defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        
        # Step 2: Find all connected components using DFS
        def dfs(node):
            if visited[node]:
                return []
            visited[node] = True
            component = [node]
            for neighbor in graph[node]:
                component.extend(dfs(neighbor))
            return component
        
        visited = [False] * len(s)
        components = []
        for i in range(len(s)):
            if not visited[i]:
                components.append(dfs(i))
        
        # Step 3: For each component, sort the indices and the corresponding characters
        result = list(s)
        for component in components:
            indices = sorted(component)
            letters = sorted(result[i] for i in component)
            for i, letter in zip(indices, letters):
                result[i] = letter
        
        return ''.join(result)

def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    return Solution().smallestStringWithSwaps(s, pairs)