import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Count the number of paths from (0, 0) to (m-1, n-1)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        # If there are no paths from (0, 0) to (m-1, n-1), flipping one cell won't disconnect the grid
        if dp[m-1][n-1] == 0:
            return True
        
        # Step 2: Check if there is a unique path from (0, 0) to (m-1, n-1)
        # If dp[m-1][n-1] is 1, it means there is a unique path
        if dp[m-1][n-1] == 1:
            return True
        
        # Step 3: Try to find a cell that, if flipped, disconnects the path
        # We need to ensure that after flipping one cell, there is no path from (0, 0) to (m-1, n-1)
        
        # Temporarily block (0, 0) and (m-1, n-1)
        temp = grid[0][1]
        grid[0][1] = 0
        if not self.hasPath(grid, m, n):
            grid[0][1] = temp
            return True
        grid[0][1] = temp
        
        temp = grid[1][0]
        grid[1][0] = 0
        if not self.hasPath(grid, m, n):
            grid[1][0] = temp
            return True
        grid[1][0] = temp
        
        # Try flipping each cell (except (0, 0) and (m-1, n-1)) and check if it disconnects the path
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0) or (i, j) == (m-1, n-1):
                    continue
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not self.hasPath(grid, m, n):
                        grid[i][j] = 1
                        return True
                    grid[i][j] = 1
        
        return False
    
    def hasPath(self, grid, m, n):
        visited = [[False] * n for _ in range(m)]
        stack = [(0, 0)]
        
        while stack:
            x, y = stack.pop()
            if (x, y) == (m-1, n-1):
                return True
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                    stack.append((nx, ny))
        
        return False

def isPossibleToCutPath(grid: List[List[int]]) -> bool:
    return Solution().isPossibleToCutPath(grid)