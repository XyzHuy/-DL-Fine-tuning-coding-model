import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing
        start_row, start_col = start
        visited = set()
        queue = deque([(0, grid[start_row][start_col], start_row, start_col)])  # (distance, price, row, col)
        visited.add((start_row, start_col))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []

        while queue:
            dist, price, row, col = queue.popleft()
            
            # Check if the current cell's price is within the range
            if low <= price <= high:
                result.append((dist, price, row, col))
            
            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] != 0 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((dist + 1, grid[new_row][new_col], new_row, new_col))
        
        # Sort the result based on the criteria: distance, price, row, col
        result.sort()
        
        # Return the top k items
        return [[row, col] for _, _, row, col in result[:k]]

def highestRankedKItems(grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
    return Solution().highestRankedKItems(grid, pricing, start, k)