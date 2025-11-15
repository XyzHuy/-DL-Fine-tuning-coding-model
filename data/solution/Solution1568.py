import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        if self.isDisconnected(grid):
            return 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.isDisconnected(grid):
                        return 1
                    grid[i][j] = 1
        
        return 2
    
    def isDisconnected(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
        
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    if island_count > 0:
                        return True
                    visited[i][j] = True
                    dfs(i, j)
                    island_count += 1
        
        return island_count != 1

def minDays(grid: List[List[int]]) -> int:
    return Solution().minDays(grid)