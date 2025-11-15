import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1
        
        # Initialize the queue with the starting cell (0, 0)
        queue = deque([(0, 0, 1)])  # (i, j, distance)
        visited = set()
        visited.add((0, 0))
        
        # max_right[i] is the farthest column we can move to in row i
        # max_down[j] is the farthest row we can move to in column j
        max_right = [0] * m
        max_down = [0] * n
        
        while queue:
            i, j, dist = queue.popleft()
            
            # Explore rightward moves
            for k in range(max(max_right[i], j + 1), min(n, grid[i][j] + j + 1)):
                if (i, k) not in visited:
                    visited.add((i, k))
                    if i == m - 1 and k == n - 1:
                        return dist + 1
                    queue.append((i, k, dist + 1))
            max_right[i] = max(max_right[i], grid[i][j] + j)
            
            # Explore downward moves
            for k in range(max(max_down[j], i + 1), min(m, grid[i][j] + i + 1)):
                if (k, j) not in visited:
                    visited.add((k, j))
                    if k == m - 1 and j == n - 1:
                        return dist + 1
                    queue.append((k, j, dist + 1))
            max_down[j] = max(max_down[j], grid[i][j] + i)
        
        return -1

def minimumVisitedCells(grid: List[List[int]]) -> int:
    return Solution().minimumVisitedCells(grid)