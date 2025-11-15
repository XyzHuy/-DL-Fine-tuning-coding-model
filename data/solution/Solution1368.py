import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Priority queue to store (cost, x, y)
        pq = [(0, 0, 0)]
        # Visited set to keep track of visited cells
        visited = set()
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            # If we reach the bottom-right corner, return the cost
            if x == m - 1 and y == n - 1:
                return cost
            
            # If the cell is already visited, skip it
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            
            # Try all four possible directions
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    # If the direction matches the grid's sign, no cost
                    if i + 1 == grid[x][y]:
                        heapq.heappush(pq, (cost, nx, ny))
                    else:
                        # Otherwise, there's a cost of 1
                        heapq.heappush(pq, (cost + 1, nx, ny))
        
        return -1  # This line should never be reached if the grid is valid

def minCost(grid: List[List[int]]) -> int:
    return Solution().minCost(grid)