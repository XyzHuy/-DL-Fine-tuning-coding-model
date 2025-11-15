import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        
        def can_move(x, y, nx, ny):
            return 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]
        
        def dfs(x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            
            max_moves = 0
            for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if can_move(x, y, nx, ny):
                    max_moves = max(max_moves, 1 + dfs(nx, ny))
            
            dp[x][y] = max_moves
            return max_moves
        
        max_total_moves = 0
        for i in range(m):
            max_total_moves = max(max_total_moves, dfs(i, 0))
        
        return max_total_moves

def maxMoves(grid: List[List[int]]) -> int:
    return Solution().maxMoves(grid)