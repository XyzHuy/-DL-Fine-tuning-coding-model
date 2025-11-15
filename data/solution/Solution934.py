import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n
        
        def dfs(x, y):
            if not is_valid(x, y) or grid[x][y] != 1:
                return
            grid[x][y] = -1  # Mark the cell as visited
            queue.append((x, y))
            for dx, dy in directions:
                dfs(x + dx, y + dy)
        
        # Find the first island and mark it
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        
        # BFS to find the shortest bridge
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and grid[nx][ny] != -1:
                        if grid[nx][ny] == 1:
                            return steps
                        grid[nx][ny] = -1  # Mark the cell as visited
                        queue.append((nx, ny))
            steps += 1
        
        return -1  # Should never reach here if the input is valid

def shortestBridge(grid: List[List[int]]) -> int:
    return Solution().shortestBridge(grid)