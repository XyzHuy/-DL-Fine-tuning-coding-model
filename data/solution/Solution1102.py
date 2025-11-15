import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Max-heap to store the cells, using negative values for max-heap behavior
        max_heap = [(-grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        
        while max_heap:
            # Get the cell with the maximum value
            val, x, y = heapq.heappop(max_heap)
            
            # If we reached the bottom-right corner, return the minimum value in the path
            if x == m - 1 and y == n - 1:
                return -val
            
            # Explore the 4 cardinal directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    # Push the neighboring cell onto the heap with the minimum value in the path
                    heapq.heappush(max_heap, (max(val, -grid[nx][ny]), nx, ny))
        
        return -1  # This should never be reached if the grid is valid

def maximumMinimumPath(grid: List[List[int]]) -> int:
    return Solution().maximumMinimumPath(grid)