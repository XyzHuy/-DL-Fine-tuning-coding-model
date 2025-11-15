import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Memoization table to store the number of paths from each cell
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(x, y):
            if memo[x][y] != -1:
                return memo[x][y]
            
            # Every cell is a path of length 1
            paths = 1
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                    paths = (paths + dfs(nx, ny)) % MOD
            
            memo[x][y] = paths
            return paths
        
        total_paths = 0
        for i in range(m):
            for j in range(n):
                total_paths = (total_paths + dfs(i, j)) % MOD
        
        return total_paths

def countPaths(grid: List[List[int]]) -> int:
    return Solution().countPaths(grid)