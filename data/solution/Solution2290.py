import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Min-heap to store (obstacles_removed, x, y)
        min_heap = [(0, 0, 0)]
        # Visited set to keep track of visited cells
        visited = set()
        
        while min_heap:
            obstacles_removed, x, y = heapq.heappop(min_heap)
            
            # If we reach the bottom-right corner, return the number of obstacles removed
            if x == m - 1 and y == n - 1:
                return obstacles_removed
            
            # If the cell is already visited, skip it
            if (x, y) in visited:
                continue
            
            # Mark the cell as visited
            visited.add((x, y))
            
            # Explore the neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    # Push the neighbor to the heap with updated obstacles_removed
                    heapq.heappush(min_heap, (obstacles_removed + grid[nx][ny], nx, ny))
        
        # If we exhaust the heap without reaching the destination, return -1 (should not happen with valid input)
        return -1

def minimumObstacles(grid: List[List[int]]) -> int:
    return Solution().minimumObstacles(grid)