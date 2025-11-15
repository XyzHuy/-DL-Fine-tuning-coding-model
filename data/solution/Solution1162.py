import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        
        # Add all land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        # If there are no land cells or no water cells, return -1
        if not queue or len(queue) == n * n:
            return -1
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = -1
        
        # Perform BFS from all land cells simultaneously
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1  # Mark the cell as visited by setting it to land
                        queue.append((nx, ny))
        
        return distance

def maxDistance(grid: List[List[int]]) -> int:
    return Solution().maxDistance(grid)