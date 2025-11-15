import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid or not grid[0]:
            return False
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y, prev_x, prev_y, char):
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == char:
                    if not visited[nx][ny]:
                        if dfs(nx, ny, x, y, char):
                            return True
                    elif (nx, ny) != (prev_x, prev_y):
                        return True
            return False
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False

def containsCycle(grid: List[List[str]]) -> bool:
    return Solution().containsCycle(grid)