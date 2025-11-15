import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        total_distances = [[0] * n for _ in range(m)]
        buildings_reached = [[0] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        total_buildings = 0
        
        def bfs(start_x, start_y):
            visited = [[False] * n for _ in range(m)]
            queue = deque([(start_x, start_y, 0)])
            visited[start_x][start_y] = True
            min_distance = float('inf')
            
            while queue:
                x, y, dist = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        buildings_reached[nx][ny] += 1
                        total_distances[nx][ny] += dist + 1
                        queue.append((nx, ny, dist + 1))
                        if buildings_reached[nx][ny] == total_buildings:
                            min_distance = min(min_distance, total_distances[nx][ny])
            
            return min_distance
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_buildings += 1
                    min_distance = bfs(i, j)
                    if min_distance == float('inf'):
                        return -1
        
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and buildings_reached[i][j] == total_buildings:
                    min_dist = min(min_dist, total_distances[i][j])
        
        return min_dist if min_dist != float('inf') else -1

def shortestDistance(grid: List[List[int]]) -> int:
    return Solution().shortestDistance(grid)