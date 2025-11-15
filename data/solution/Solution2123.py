import random
import functools
import collections
import string
import math
import datetime


from collections import deque, defaultdict
from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Directions for 4-directional movement
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Build the bipartite graph
        left = set()  # Nodes at even positions
        right = set()  # Nodes at odd positions
        graph = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i + j) % 2 == 0:
                        left.add((i, j))
                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                                right.add((ni, nj))
                                graph[(i, j)].append((ni, nj))
                    else:
                        right.add((i, j))
        
        # Hopcroft-Karp algorithm
        match = defaultdict(lambda: None)
        dist = defaultdict(lambda: float('inf'))
        
        def bfs():
            queue = deque()
            for node in left:
                if match[node] is None:
                    dist[node] = 0
                    queue.append(node)
                else:
                    dist[node] = float('inf')
            dist[None] = float('inf')
            while queue:
                node = queue.popleft()
                if node is not None:
                    for neighbor in graph[node]:
                        if dist[match[neighbor]] == float('inf'):
                            dist[match[neighbor]] = dist[node] + 1
                            queue.append(match[neighbor])
            return dist[None] != float('inf')
        
        def dfs(node):
            if node is not None:
                for neighbor in graph[node]:
                    if dist[match[neighbor]] == dist[node] + 1:
                        if dfs(match[neighbor]):
                            match[neighbor] = node
                            match[node] = neighbor
                            return True
                dist[node] = float('inf')
                return False
            return True
        
        matching = 0
        while bfs():
            for node in left:
                if match[node] is None and dfs(node):
                    matching += 1
        
        return matching

def minimumOperations(grid: List[List[int]]) -> int:
    return Solution().minimumOperations(grid)