import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = {i: [] for i in range(n)}
        
        # Build the graph
        for i in range(n):
            for j in range(n):
                if i != j:
                    xi, yi, ri = bombs[i]
                    xj, yj, _ = bombs[j]
                    distance_squared = (xi - xj) ** 2 + (yi - yj) ** 2
                    if distance_squared <= ri ** 2:
                        graph[i].append(j)
        
        def bfs(start):
            queue = deque([start])
            visited = set([start])
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)
        
        max_detonations = 0
        for bomb in range(n):
            max_detonations = max(max_detonations, bfs(bomb))
        
        return max_detonations

def maximumDetonation(bombs: List[List[int]]) -> int:
    return Solution().maximumDetonation(bombs)